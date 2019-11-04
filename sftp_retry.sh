#!/bin/bash

# http://www.allguru.net/os/retry-sftp-connection-shell-script/
SFTP_USER=pi
SFTP_SERVER=192.168.0.9
SFTP_RETRY_COUNT=0
SFTP_RETRY_SECOND=60
export SSHPASS=raspi

# Ping to check remote server status
ping -c 3 $SFTP_SERVER
if [ $? -ne 0 ] ; then
    echo "Unable to connect"
    exit 2
fi

while [ $SFTP_RETRY_COUNT != 10 ]
do
    # Establish SFTP
    # https://stackoverflow.com/questions/5386482/how-to-run-the-sftp-command-with-a-password-from-bash-script
    SFTP_CONNECT=`sshpass -e sftp -oBatchMode=no -b "sftp_ls.bat" pi@192.168.0.9 2> /tmp/sftp_error.log`
    if [ -f /tmp/sftp_error.log ] ; then
        TRAP_SFTP_ERROR=`cat /tmp/sftp_error.log | grep "Connection closed"`
        if echo "$TRAP_SFTP_ERROR" | grep "Connection closed" ; then
            echo "SFTP Fail"
            SFTP_RETRY_COUNT=$[$SFTP_RETRY_COUNT+1]
            sleep $SFTP_RETRY_SECOND
            if [ $SFTP_RETRY_COUNT == 10 ] ; then
                echo "Maximum Retry Reached"
            fi
        else
            echo "Success"
            SFTP_RETRY_COUNT=10
        fi
    fi
done

: <<'!!!'
# https://stackoverflow.com/questions/32787603/how-do-i-automatically-retry-an-sftp-connection-attempt
counter=1
while [ $counter -gt 0 ]; do 
    sftp pi@192.168.0.9
    if [ $? -ne 0 ] ; then
        counter=$(($counter-1))
    else
        echo "Sucsess"
        break
    fi
done
!!!