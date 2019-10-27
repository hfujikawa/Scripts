#!/bin/bash

SECONDS=0
LOGFILE="./tmp/backup-`date +%w`.log"
exec > "${LOGFILE}"
exec 2>&1

bash ./count_down_sec.sh

echo "[INFO] Script time is ${SECONDS}sec."
