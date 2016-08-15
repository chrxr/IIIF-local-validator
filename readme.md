###Script for validating individual IIIF manifests or folder of manifests

**WIP**

ManifestFactory, Loader and most of main script copied from the main Presentation API implementations GitHub repo: https://github.com/IIIF/presentation-api/tree/master/implementations, so thanks to them.

Usage:

    $ python ./local_validator.py [--folder] [--file path/to/single/manifest/file] [--write path/to/file/to/write/results]

* `--folder` flag validates all json files in the 'static' directory.
* `--file` takes a path to a single manifest file for validation
* `--write` takes a path to a file to write results to (or creates file if it doesn't already exist)
* 'Static' folder should be in the in the same directory as local_validator.py.
* Results file is overwritten each time the script is run

####To Do:

* [ ] Flag to only return validation failures
* [ ] Flag to only return failures and warnings
* [ ] Investigate getting line numbers in their (pull request to main IIIF manifest_factory)
