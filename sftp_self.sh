#!/bin/bash

set -e

SSHUSER="i2m"
SSHHOST=localhost
SSHPASS="cxp0728"

export SSHPASS

# Ping to check remote server status
ping -c 1 $SSHHOST
if [ $? -ne 0 ] ; then
    echo "Unable to connect"
    exit 2
fi

: <<'END'
#sshpass -e sftp -oBatchMode=no -b "sftp_ls.bat" $SSHUSER@$SSHHOST
sshpass -e sftp -oBatchMode=no $SSHUSER@$SSHHOST <<TEST | grep -v 'sffp>' >cmds.txt
cd /home/i2m/Develop
ls *.zip
bye
TEST
echo ${PIPESTATUS[@]}
RET=$?
if [ $RET -ne 0 ] ; then
  echo "error: $RET"
else
  echo "No error"
fi


# https://unix.stackexchange.com/questions/520993/test-if-any-file-was-downloaded-with-sftp-command
echo "ls /home/i2m/Develop/Scripts/*.sh" | sftp -b - $SSHUSER@$SSHHOST
if [ $? -eq 0 ] ; then
    echo "Files exist, can download now"

    echo 'get /home/i2m/Develop/Scripts/*.sh /local/path/' | sftp -b - $SSHUSER@$SSHHOST
    if [ $? -eq 0 ] ; then
        echo "Files successfully downloaded"
    else
        echo "Files exist, but failed to download"
    fi
else
    echo "Files do not exist"
fi
END

# https://unix.stackexchange.com/questions/190128/capture-errors-in-a-sftp-script
set -e
mkdir myserver
sshfs $SSHUSER@$SSHHOST / myserver
