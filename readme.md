###Script for validating individual IIIF manifests or folder of manifests

**WIP**

ManifestFactory, Loader and most of main script copied from the main Presentation API implementations GitHub repo: https://github.com/IIIF/presentation-api/tree/master/implementations, so thanks to them.

###Usage

####Command line

    $ python ./local_validator.py [--folder] [--file path/to/single/manifest/file] [--write path/to/file/to/write/results]

* `--folder` flag validates all json files in the 'static' directory.
* `--file` takes a path to a single manifest file for validation
* `--write` takes a path to a file to write results to (or creates file if it doesn't already exist)
* 'Static' folder should be in the in the same directory as local_validator.py.
* Results file is overwritten each time the script is run

####As a module

The script can be imported into other python scripts:

    from local_validator import module

It should be called with the following variables:

    validator([single_file_path], [folder = True], [results_file_path], [raw=True])

The `raw` option returns the validation results as a list of dictionaries.

The example below would validate a single file and save to `more_results.txt`

    validator('manifests/test1.json', 'more_results.txt')

The example below would validate a folder of files, but only display the results in the console:

    validator(folder=True)

The example below would validate a folder of files, and return the results as a list of dictionaries:

    results = validator(folder=True, raw=True)

When using as a module, you can also define an alternative folder path:

    different_folder_path = "manifests/child"
    validator(folder=True, folder_path=different_folder_path)

### Breaking down the results

The following script would print each of the fields as the individual manifest results:

  from local_validator import validator

  results = validator(folder=True, raw=True)

  for result in results:
      print result['warnings']
      print result['error']
      print result['okay']
      print result['filename']

* `result['filename']`: The path and filename of the file that has been validated
* `result['warnings']`: A list of all warnings for the manifest
* `result['error']`: The first error that the validator encounters (it stops at that point)
* `result['okay']`: Returns '1' if the manifest is valid, or '0' if it's invalid

####To Do:

* [ ] Flag to only return validation failures
* [ ] Flag to only return failures and warnings
* [ ] Investigate getting line numbers in their (pull request to main IIIF manifest_factory)
