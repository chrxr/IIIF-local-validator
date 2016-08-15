#!/usr/bin/env python
# encoding: utf-8

from local_validator import validator

different_folder_path = "manifests/child"
validator(folder=True, folder_path=different_folder_path)
