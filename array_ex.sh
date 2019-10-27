#!/bin/bash
#
# set the word in array region
#
ARRAY1=(zone symolism dancing meetinghouse justice)
ARRAY1[5]="information"
#
# display array size
#
echo -n "array size: "
echo ${#ARRAY1[*]}