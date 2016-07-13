#!/usr/bin/env python
# encoding: utf-8
"""Local IIIF Presentation Validation Service"""

import argparse
import json
import os
import sys

from loader import ManifestReader

def main():
    file_path = 'static'

    parser = argparse.ArgumentParser(description=__doc__.strip(),
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--folder', action='store_true', help='Add this flag to process a folder of manifests')

    parser.add_argument('--file',
                        help='Location of IIIF manifest file to validate')

    args = parser.parse_args()

    if args.file != None:
        results = [read_file(args.file)]

    if args.folder:
        paths = [os.path.join(file_path,fn) for fn in next(os.walk(file_path))[2]]
        results = []
        for each in paths:
            result = read_file(each)
            results.append(result)

    if results:
        print results

def read_file(manifest):
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


    infojson = {'okay': okay, 'warnings': warnings, 'error': str(err)}
    # print infojson
    return infojson

if __name__ == "__main__":
    main()
