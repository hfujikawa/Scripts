#!/bin/bash

msg=`curl -s http://api.openweathermap.org/data/2.5/weather?q=Tokyo,jp | jq .message`
echo ${msg//\"/}

str_msg="message string"
echo $str_msg

adr=`cat config.json | jq .remote_ip`
rslt=${adr//\"/}
echo $rslt
