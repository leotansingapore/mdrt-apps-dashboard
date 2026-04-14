#!/bin/zsh
# MDRT Apps Dashboard Sync -- pushes latest scripts + regenerates index.html + Lark notify
set -euo pipefail

DASHBOARD_DIR="$HOME/.local/share/mdrt-meeting/dashboard-repo"
LOG_FILE="$HOME/.local/log/mdrt-meeting.log"
ENV_FILE="$HOME/.config/agents.env"; [[ -r "$ENV_FILE" ]] || ENV_FILE="$HOME/Documents/New project/.env"
DASHBOARD_URL="https://leotansingapore.github.io/mdrt-apps-dashboard/"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] [sync] $1" >> "$LOG_FILE"; }

set -a; source "$ENV_FILE"; set +a

if [[ ! -d "$DASHBOARD_DIR/.git" ]]; then
  git clone https://github.com/leotansingapore/mdrt-apps-dashboard.git "$DASHBOARD_DIR" 2>> "$LOG_FILE"
fi

cd "$DASHBOARD_DIR"
git pull --rebase 2>> "$LOG_FILE" || true

mkdir -p automation automation/launchd

for src in \
  mdrt-meeting-reminder.sh \
  mdrt-scrum-master.sh \
  mdrt-meeting-sheet.py \
  mdrt-meeting-log.py \
  mdrt-sync-dashboard.sh \
  mdrt-dashboard-regen.py; do
  cp "$HOME/.local/bin/$src" automation/ 2>/dev/null || true
done
cp ~/Library/LaunchAgents/com.leo.mdrt-*.plist automation/launchd/ 2>/dev/null || true

# Run meeting-log (pulls Fireflies, writes sheet + swarm-reports/*.md)
if [[ -n "${FIREFLIES_API_KEY:-}" ]]; then
  /usr/bin/python3 "$HOME/.local/bin/mdrt-meeting-log.py" 2>> "$LOG_FILE" || log "meeting-log skipped"
fi

# Regenerate index.html
/usr/bin/python3 "$HOME/.local/bin/mdrt-dashboard-regen.py" 2>> "$LOG_FILE" || log "dashboard regen failed"

# Commit and push if changed
if git diff --quiet && git diff --cached --quiet && [[ -z "$(git ls-files --others --exclude-standard)" ]]; then
  log "Dashboard repo already up to date"
  exit 0
fi

CHANGELOG=$(git status --porcelain | awk '{
  s=$1; f=substr($0, index($0,$2))
  tag = "changed"
  if (s ~ /A|\?\?/) tag = "added"
  else if (s ~ /D/) tag = "removed"
  else if (s ~ /M/) tag = "updated"
  printf "- %s: %s\n", tag, f
}' | head -20)
CHANGED_COUNT=$(git status --porcelain | wc -l | tr -d ' ')

git add -A
git commit -m "sync: dashboard auto-update ($(date '+%Y-%m-%d %H:%M')) -- $CHANGED_COUNT files" 2>> "$LOG_FILE"
git push 2>> "$LOG_FILE"

log "Dashboard synced ($CHANGED_COUNT files)"

if [[ -n "${LARK_MDRT_WEBHOOK:-}" ]]; then
  /usr/bin/python3 - <<PYEOF 2>> "$LOG_FILE" || true
import json, os, urllib.request
webhook = os.environ.get("LARK_MDRT_WEBHOOK", "")
if not webhook:
    raise SystemExit(0)
changelog = """$CHANGELOG""".strip() or "(no file-level details)"
count = "$CHANGED_COUNT"
content = f"""**Dashboard auto-synced** ({count} files)

[Open dashboard]($DASHBOARD_URL)

**Changes:**
{changelog}
"""
payload = {
    "msg_type": "interactive",
    "card": {
        "header": {"title": {"tag": "plain_text", "content": "MDRT Apps Dashboard updated"}, "template": "blue"},
        "elements": [{"tag": "markdown", "content": content}],
    },
}
req = urllib.request.Request(webhook, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
urllib.request.urlopen(req, timeout=5).read()
print("Lark notified")
PYEOF
fi

echo "Dashboard synced and Lark notified"
