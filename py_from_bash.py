# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:27:49 2019

@author: hfuji
"""
# https://stackoverflow.com/questions/34171568/return-value-from-python-script-to-shell-script

import sys
if sys.argv[1]=='hi':
    print('Salaam')
sys.exit(0)
#return 0