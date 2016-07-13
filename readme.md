###Script for validating individual IIIF manifests or folder of manifests

**WIP**

* ManifestFactory, Loader and most of main script copied from the main Presentation API implementations GitHub rep: https://github.com/IIIF/presentation-api/tree/master/implementations
* Very much a work in progress, but generally works.

Usage:

    $ python ./local_validator.py [--folder] [--file path/to/file]

* When using --folder flag, files should be placed in 'static' folder in the same dir as script.
