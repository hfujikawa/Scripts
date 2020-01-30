#!/bin/bash

json=$(cat list.json)
len=$(echo $json | jq length)
for i in $( seq 0 $(($len - 1)) ); do
  row=$(echo $json | jq .[$i])
  echo $row
done

json=$(cat example2.json)
len=$(echo $json | jq length)
echo $len
