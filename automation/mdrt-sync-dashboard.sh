#!/bin/zsh
# MDRT Apps Dashboard Sync -- pushes latest scripts to GitHub
set -euo pipefail

DASHBOARD_DIR="$HOME/.local/share/mdrt-meeting/dashboard-repo"
LOG_FILE="$HOME/.local/log/mdrt-meeting.log"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] [sync] $1" >> "$LOG_FILE"; }

if [[ ! -d "$DASHBOARD_DIR/.git" ]]; then
  git clone https://github.com/leotansingapore/mdrt-apps-dashboard.git "$DASHBOARD_DIR" 2>> "$LOG_FILE"
fi

cd "$DASHBOARD_DIR"
git pull --rebase 2>> "$LOG_FILE" || true

mkdir -p automation automation/launchd

cp ~/.local/bin/mdrt-meeting-reminder.sh automation/ 2>/dev/null || true
cp ~/.local/bin/mdrt-scrum-master.sh automation/ 2>/dev/null || true
cp ~/.local/bin/mdrt-meeting-sheet.py automation/ 2>/dev/null || true
cp ~/.local/bin/mdrt-sync-dashboard.sh automation/ 2>/dev/null || true
cp ~/Library/LaunchAgents/com.leo.mdrt-*.plist automation/launchd/ 2>/dev/null || true

if git diff --quiet && git diff --cached --quiet && [[ -z "$(git ls-files --others --exclude-standard)" ]]; then
  log "Dashboard repo already up to date"
  exit 0
fi

git add -A
git commit -m "sync: auto-update automation scripts ($(date '+%Y-%m-%d %H:%M'))" 2>> "$LOG_FILE"
git push 2>> "$LOG_FILE"

log "Dashboard repo synced to GitHub"
echo "Dashboard synced"
