#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SCRIPT_PATH="$SCRIPT_DIR/luckypot.py"
LOG_PATH="$SCRIPT_DIR/luckypot.log"

(crontab -l 2>/dev/null | grep -v "$SCRIPT_PATH") | crontab -
(crontab -l 2>/dev/null; echo "*/15 * * * * /usr/bin/python3 $SCRIPT_PATH >> $LOG_PATH 2>&1") | crontab -

echo "✅ Cron installé toutes les 15 min."
/usr/bin/python3 "$SCRIPT_PATH"
