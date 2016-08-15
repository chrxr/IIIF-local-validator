###Script for validating individual IIIF manifests or folder of manifests

**WIP**

* ManifestFactory, Loader and most of main script copied from the main Presentation API implementations GitHub rep: https://github.com/IIIF/presentation-api/tree/master/implementations
* Very much a work in progress, but generally works.

Usage:

    $ python ./local_validator.py [--folder] [--file path/to/file] [--write path/to/file/to/write/results]

* When using --folder flag, files should be placed in 'static' folder in the same dir as script.
* Results file is overwritten each time the script is run

####To Do:

* [ ] Flag to only return validation failures
* [ ] Flag to only return failures and warnings
* [ ] Investigate getting line numbers in their (pull request to main IIIF manifest_factory)
