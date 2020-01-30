#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 19:43:56 2020

@author: i2m
"""

import json

with open('example.json', 'rt') as fp:
    dict = json.load(fp)

print("RESP:\n{} ".format(json.dumps(dict, indent=2)))
