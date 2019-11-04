#!/bin/bash
# script for tesing
clear
echo "............script started............"
sleep 1
result=`python py_from_bash.py "hi"`
if [ "$result" == "Salaam" ]; then
    echo "script return correct response"
fi
