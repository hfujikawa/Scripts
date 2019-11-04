#!/bin/bash

python pandas_datetime.py
# $? =  is the exit status of the most recently-executed command; by convention, 0 means success and anything else indicates failure. 
if [ $? -eq 0 ]
then
  echo "Successfully executed script"
else
  # Redirect stdout from echo command to stderr.
  echo "Script exited with error." >&2
fi