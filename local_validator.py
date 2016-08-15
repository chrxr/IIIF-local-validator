#!/usr/bin/env python
# encoding: utf-8
"""Local IIIF Presentation Validation Service"""

import argparse
import json
import os
import sys

from loader import ManifestReader

def validator():
    file_path = 'static'

    parser = argparse.ArgumentParser(description=__doc__.strip(),
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--folder', action='store_true', help='Add this flag to process a folder of manifests')

    parser.add_argument('--file',
                        help='Location of IIIF manifest file to validate')

    parser.add_argument('--write',
                        help='Specify a file name to write the results of the validation to')

    # ADDITIONAL ARGUMENTS TO ADD LATER
    #
    # parser.add_argument('--fails', action='store_true',
    #                     help='Only gives details re manifests that have failed')
    #
    # parser.add_argument('--warnings', action='store_true',
    #                     help='Only gives details re manifests that have failed or have warnings')

    # parser.add_argument('--raw', action='store_true',
    #                     help='Just delivers the raw JSON response')

    args = parser.parse_args()

    if args.file != None:
        results = [read_file_and_validate(args.file)]

    if args.folder:
        paths = [os.path.join(file_path,fn) for fn in next(os.walk(file_path))[2]]
        results = []
        for each in paths:
            if each.endswith('.json'):
                result = read_file_and_validate(each)
                results.append(result)

    if results:
        formatted_results = []
        summary = {'passed':0, 'failed':0}
        for manifest in results:
            if manifest['okay'] == 1:
                summary['passed'] += 1
            else:
                summary['failed'] += 1
            formatted_result = format_results(manifest)
            formatted_results.append(formatted_result)

        print "Summary\nPassed: "+str(summary['passed'])+"\nFailed: "+str(summary['failed'])+"\n"

        if args.write:
            filename = args.write
            f = open(filename, 'w')
            for result in formatted_results:
                f.write(str(result))
            f.close

        else:
            for each in formatted_results:
                print each



def format_results(manifest):
    filename = manifest['filename']
    okay = manifest['okay']
    warnings = manifest['warnings']
    errors = manifest['error']
    if okay == 1:
        status = 'Passed!'
    else:
        status = 'Failed :('
    formatted_results = 'File name: '+filename+'\nStatus: '+status+'\nWarnings: '+str(warnings)+'\nErrors: '+errors+'\n\n'
    return formatted_results


def read_file_and_validate(manifest, fails_only=False, warnings_only=False):
    json_data=open(manifest).read()

    data = json.loads(json_data)

    reader = ManifestReader(data, version='2.0')
    err = None
    try:
        mf = reader.read()
        mf.toJSON()
        # Passed!
        okay = 1
    except Exception, err:
        # Failed
        okay = 0

    warnings = []
    warnings.extend(reader.get_warnings())

    infojson = {'filename': manifest, 'okay': okay, 'warnings': warnings, 'error': str(err)}
    return infojson

if __name__ == "__main__":
    validator()
