#!/bin/bash

echo "before comment"
: <<'=cut'
SSHPASS='raspberry'
#https://stackoverflow.com/questions/35545774/get-latest-file-from-sftp-to-local-machine
fileName=$(echo "ls -1rt" | sftp -oIdentityFile=$SSHPASS pi@192.168.0.8:/var/lib/motion | tail -1) 
echo "get $fileName" | sftp -oIdentityFile=$SSHPASS pi@192.168.0.8:/var/lib/motion  
=cut
echo "after comment"

#https://stackoverflow.com/questions/5386482/how-to-run-the-sftp-command-with-a-password-from-bash-script
export SSHPASS='raspberry'
sshpass -e sftp -oBatchMode=no -b - pi@192.168.0.8 << !
   cd /var/lib/motion
   lcd /mnt/d/Develop
#   latest_file=$(ls -t | head -n 1)
#   get $latest_file
   get *.jpg
   bye
!
