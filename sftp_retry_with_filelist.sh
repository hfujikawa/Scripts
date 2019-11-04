#!/bin/bash

# ファイル・ディレクトリ一覧
# http://wordpress.honobono-life.info/code/bash%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%88%E3%81%A7%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%88%E3%83%AA%E5%86%85%E3%81%AE%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E4%B8%80%E8%A6%A7%E3%81%A8/
files="/home/i2m/id*"
fileary=()
dirary=()
for filepath in $files; do
  if [ -f $filepath ] ; then
#    filename="$(basename $filepath)"
    filename=`basename $filepath`
    fileary+=("$filename")
  elif [ -d $filepath ] ; then
    dirary+=("$filepath")
  fi
done
# ファイルリスト出力
# https://eng-entrance.com/linux-shellscript-newline
{
  echo "file list"
  for i in ${fileary[@]}; do
    echo $i
  done
} > file_list.txt

# バッチファイル生成
cat <<EOF > test.txt
cd /home/pi
quit
EOF

# 引数チェック
if [ $# -ne 1 ] ; then
  echo "Usage:"
  echo "sftp_retry.sh batchfile"
  exit 1
fi

# http://www.allguru.net/os/retry-sftp-connection-shell-script/
SFTP_USER=pi
SFTP_SERVER=192.168.0.9
SFTP_RETRY_COUNT=0
SFTP_RETRY_SECOND=60
#SFTP_BATCH_FILE="sftp_ls.bat"
SFTP_BATCH_FILE=$1
export SSHPASS=raspi


# Ping to check remote server status
ping -c 3 $SFTP_SERVER
if [ $? -ne 0 ] ; then
  echo "Unable to connect"
  exit 2
fi

: <<'END'
Script="$( cat <<'HERE'
cd /home/pi
ls
quit
HERE
)"
END

while [ $SFTP_RETRY_COUNT != 3 ]
do
  # Establish SFTP
  # https://stackoverflow.com/questions/5386482/how-to-run-the-sftp-command-with-a-password-from-bash-script
#  SFTP_CONNECT=`sshpass -e sftp -oBatchMode=no -b "sftp_ls.bat" pi@192.168.0.9 2> /tmp/sftp_error.log`
  sshpass -e sftp -oBatchMode=no -b $SFTP_BATCH_FILE $SFTP_USER@$SFTP_SERVER 2> /tmp/sftp_error.log
  if [ -f /tmp/sftp_error.log ] ; then
    TRAP_SFTP_ERROR=`cat /tmp/sftp_error.log | grep "Connection closed"`
    if echo "$TRAP_SFTP_ERROR" | grep "Connection closed" ; then
      echo "SFTP Fail"
      SFTP_RETRY_COUNT=$[$SFTP_RETRY_COUNT+1]
      if [ $SFTP_RETRY_COUNT == 3 ] ; then
        echo "Maximum Retry Reached"
        exit 2
      fi
      sleep $SFTP_RETRY_SECOND
    else
      echo "Success"
      SFTP_RETRY_COUNT=3
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