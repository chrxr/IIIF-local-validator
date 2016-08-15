#!/usr/bin/env python
# encoding: utf-8

import argparse
import json
import os
import sys
from local_validator import validator

validator({'folder':True,'write': 'new_results.txt'})
