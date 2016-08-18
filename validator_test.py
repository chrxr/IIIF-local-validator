#!/usr/bin/env python
# encoding: utf-8

from local_validator import validator

results = validator(folder=True, folder_path='manifests/child', raw=True)


for result in results:
    print result
    print result['warnings']
    print result['error']
    print result['okay']
    print result['filename']
