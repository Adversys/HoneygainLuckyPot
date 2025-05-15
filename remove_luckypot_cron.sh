#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SCRIPT_PATH="$SCRIPT_DIR/luckypot.py"
LOG_PATH="$SCRIPT_DIR/luckypot.log"

(crontab -l 2>/dev/null | grep -v "$SCRIPT_PATH") | crontab -
rm -f "$LOG_PATH"
echo "✅ Cron et log supprimés."
