#!/bin/zsh
# MDRT Team Apps Meeting Reminder -- Tuesday 4:00 PM SGT -> Lark
set -euo pipefail

ENV_FILE="$HOME/.config/agents.env"; [[ -r "$ENV_FILE" ]] || ENV_FILE="$HOME/Documents/New project/.env"
LOG_FILE="$HOME/.local/log/mdrt-meeting.log"
STATE_FILE="$HOME/.local/share/mdrt-meeting/state.json"
TODAY=$(date '+%Y-%m-%d')

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] [reminder] $1" >> "$LOG_FILE"; }
log "Starting MDRT meeting reminder"

set -a; source "$ENV_FILE"; set +a

OUTSTANDING=0
if [[ -f "$STATE_FILE" ]]; then
  OUTSTANDING=$(python3 -c "
import json
d = json.load(open('$STATE_FILE'))
print(len([a for a in d.get('action_items', []) if a.get('status') != 'done']))
" 2>/dev/null || echo 0)
fi

if [[ "$OUTSTANDING" -gt 0 ]]; then
  ACTION_LINE="We have **${OUTSTANDING} action item(s)** to follow up on from last week."
else
  ACTION_LINE="No outstanding items from last week -- clean slate!"
fi

REMINDER_TEXT="Hey team! Our weekly MDRT Apps catch-up is in **1 hour**.

**When:** 5:00 - 6:00 PM SGT (today)
**Where:** [Click here to join Google Meet](https://meet.google.com/pjz-jeuo-iuk)

${ACTION_LINE}

The full agenda will be posted here at 4:30 PM -- see you soon!"

curl -s -X POST "$LARK_MDRT_WEBHOOK" \
  -H "Content-Type: application/json" \
  -d "$(cat <<PAYLOAD
{
  "msg_type": "interactive",
  "card": {
    "header": {
      "title": {
        "tag": "plain_text",
        "content": "MDRT Apps Weekly Catch-Up -- Today at 5 PM"
      },
      "template": "orange"
    },
    "elements": [
      {
        "tag": "markdown",
        "content": $(echo "$REMINDER_TEXT" | python3 -c 'import sys,json; print(json.dumps(sys.stdin.read()))')
      },
      {
        "tag": "action",
        "actions": [
          {
            "tag": "button",
            "text": {
              "tag": "plain_text",
              "content": "Join Google Meet"
            },
            "url": "https://meet.google.com/pjz-jeuo-iuk",
            "type": "primary"
          }
        ]
      }
    ]
  }
}
PAYLOAD
)" > /dev/null 2>&1

log "Reminder sent successfully"

/usr/bin/python3 -c "
import sys, os, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0, os.path.expanduser('~/Documents/New project/tools'))
from lib.heartbeat import beat
beat('mdrt-meeting-reminder')
" 2>/dev/null || true

echo "MDRT meeting reminder sent: $TODAY"
