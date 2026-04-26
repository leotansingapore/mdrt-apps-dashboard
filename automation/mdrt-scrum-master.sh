#!/bin/bash
# MDRT Team Apps Scrum Master -- Tuesday 4:30 PM SGT -> Lark
set -euo pipefail
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

REPOS=(
  "leotansingapore/quick-schedule-pal"
  "leotansingapore/growing-age-calculator"
  "leotansingapore/agency-launchpad-90"
  "leotansingapore/aia-product-compass-hub"
  "leotansingapore/trackerattendance"
  "leotansingapore/remix-of-activity-tracker"
  "leotansingapore/agent-rank-dash"
  "leotansingapore/bee-hive-finance-hub"
  "leotansingapore/loyalty-link-access"
)

ENV_FILE="$HOME/.config/agents.env"; [[ -r "$ENV_FILE" ]] || ENV_FILE="$HOME/Documents/New project/.env"
STATE_FILE="$HOME/.local/share/mdrt-meeting/state.json"
LOG_FILE="$HOME/.local/log/mdrt-meeting.log"
TODAY=$(date '+%Y-%m-%d')
SINCE=$(date -v-7d '+%Y-%m-%dT00:00:00Z')

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] [scrum] $1" >> "$LOG_FILE"; }
log "Starting MDRT scrum master report"

set -a; source "$ENV_FILE"; set +a

TMPDIR_REPORT=$(mktemp -d)
trap "rm -rf $TMPDIR_REPORT" EXIT

# ── 1. Fetch GitHub data per repo ─────────────────────────────────
echo "=== MDRT TEAM APPS WEEKLY STATUS ===" > "$TMPDIR_REPORT/context.txt"
echo "Report date: $TODAY" >> "$TMPDIR_REPORT/context.txt"
echo "Period: last 7 days (since $SINCE)" >> "$TMPDIR_REPORT/context.txt"
echo "" >> "$TMPDIR_REPORT/context.txt"

TOTAL_COMMITS=0

for REPO in "${REPOS[@]}"; do
  REPO_NAME="${REPO#*/}"
  log "Fetching data for $REPO_NAME"

  echo "--- REPO: $REPO_NAME (https://github.com/${REPO}) ---" >> "$TMPDIR_REPORT/context.txt"

  COMMITS=$(gh api "repos/${REPO}/commits?since=${SINCE}&per_page=50" \
    --jq '.[] | "- \(.commit.message | split("\n")[0]) (\(.commit.author.name), \(.commit.author.date[:10]))"' 2>/dev/null || echo "")

  if [[ -n "$COMMITS" ]]; then
    COMMIT_COUNT=$(echo "$COMMITS" | wc -l | tr -d ' ')
    TOTAL_COMMITS=$((TOTAL_COMMITS + COMMIT_COUNT))
    echo "Commits ($COMMIT_COUNT):" >> "$TMPDIR_REPORT/context.txt"
    echo "$COMMITS" >> "$TMPDIR_REPORT/context.txt"
  else
    echo "Commits: None in last 7 days" >> "$TMPDIR_REPORT/context.txt"
  fi

  OPEN_PRS=$(gh pr list --repo "$REPO" --state open --json number,title,author \
    --jq '.[] | "- #\(.number): \(.title) (@\(.author.login))"' 2>/dev/null || echo "")
  if [[ -n "$OPEN_PRS" ]]; then
    echo "Open PRs:" >> "$TMPDIR_REPORT/context.txt"
    echo "$OPEN_PRS" >> "$TMPDIR_REPORT/context.txt"
  fi

  OPEN_ISSUES=$(gh api "repos/${REPO}/issues?state=open&per_page=20" \
    --jq '.[] | select(.pull_request == null) | "- #\(.number): \(.title)"' 2>/dev/null || echo "")
  if [[ -n "$OPEN_ISSUES" ]]; then
    echo "Open Issues:" >> "$TMPDIR_REPORT/context.txt"
    echo "$OPEN_ISSUES" >> "$TMPDIR_REPORT/context.txt"
  fi

  PUSHED_AT=$(gh repo view "$REPO" --json pushedAt --jq '.pushedAt' 2>/dev/null || echo "")
  if [[ -n "$PUSHED_AT" ]]; then
    echo "Last push: $PUSHED_AT" >> "$TMPDIR_REPORT/context.txt"
    PUSH_EPOCH=$(date -j -f "%Y-%m-%dT%H:%M:%SZ" "${PUSHED_AT}" "+%s" 2>/dev/null || echo "0")
    NOW_EPOCH=$(date "+%s")
    DAYS_AGO=$(( (NOW_EPOCH - PUSH_EPOCH) / 86400 ))
    if [[ $DAYS_AGO -gt 5 ]]; then
      echo "** STALE: No activity for ${DAYS_AGO} days **" >> "$TMPDIR_REPORT/context.txt"
    fi
  fi

  echo "" >> "$TMPDIR_REPORT/context.txt"
  sleep 1
done

log "Fetched data for ${#REPOS[@]} repos ($TOTAL_COMMITS total commits)"

# ── 2. Load previous action items ─────────────────────────────────
if [[ -f "$STATE_FILE" ]]; then
  PREV_ACTIONS=$(python3 -c "
import json
d = json.load(open('$STATE_FILE'))
items = [a for a in d.get('action_items', []) if a.get('status') != 'done']
if items:
    print('OUTSTANDING ACTION ITEMS FROM PREVIOUS MEETING:')
    for a in items:
        repo = a.get('repo', 'general')
        title = a.get('title', 'No title')
        issue = a.get('issue_number', '')
        assignee = a.get('assignee', 'unassigned')
        status = a.get('status', 'open')
        issue_str = f' (#{issue})' if issue else ''
        print(f'- [{repo}] {title}{issue_str} -- {assignee} ({status})')
else:
    print('No outstanding action items from previous meeting.')
" 2>/dev/null || echo "No action item history available.")
  echo "$PREV_ACTIONS" >> "$TMPDIR_REPORT/context.txt"
fi

# ── 3. Generate agenda via Claude CLI ──────────────────────────────
log "Generating agenda via Claude CLI"

AGENDA=$(claude -p --model sonnet "$(cat "$TMPDIR_REPORT/context.txt")

You are a scrum master preparing a weekly meeting agenda for the MDRT Team Apps. Based on the GitHub activity above, write a concise weekly agenda with these exact sections (use ** for bold headings, no # headers, no code blocks):

IMPORTANT: When mentioning a repo name, always hyperlink it using Lark markdown format: [repo-name](https://github.com/leotansingapore/repo-name).

**Per-App Progress**
For each of the 9 apps, write 1-2 bullet points summarizing what was accomplished this week. Group by themes. Name contributors where visible. Hyperlink each repo name.

**Stale Apps**
Flag any apps with no activity in 5+ days. Suggest whether to discuss or deprioritize.

**Open Blockers**
List all open issues and PRs across repos. Highlight bugs and blocked items.

**Outstanding Action Items**
List any action items carried over from last week.

**Discussion Points**
Suggest 3-5 discussion topics based on patterns in the activity.

**Proposed Focus This Week**
For each active app, suggest 1-2 priorities based on current momentum and open issues.

Keep the entire agenda under 80 lines. Be direct, no fluff. Use bullet points. Format for Lark markdown.")

log "Agenda generated (${#AGENDA} chars)"

# ── 3b. Detect blockers and append to Google Sheet Blockers tab ────
log "Scanning for blockers"
SHEET_ID=$(cat "$HOME/.local/share/mdrt-meeting/sheet_id.txt" 2>/dev/null || echo "")
if [[ -n "$SHEET_ID" ]]; then
  /usr/bin/python3 << PYEOF 2>> "$LOG_FILE" || true
import os, sys, warnings, re
warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.expanduser("~/Documents/New project/tools"))
from datetime import datetime
try:
    from lib.sheets import get_sheets_client
except Exception as e:
    print(f"Blockers: lib.sheets import failed: {e}")
    sys.exit(0)

SHEET_ID = "$SHEET_ID"
CONTEXT_PATH = "$TMPDIR_REPORT/context.txt"
AGENDA = r"""$AGENDA"""
now = datetime.now().strftime("%Y-%m-%d %H:%M")

blockers = []

# 1. Stale repos (from context.txt)
try:
    ctx = open(CONTEXT_PATH).read()
    current_repo = None
    for line in ctx.splitlines():
        m = re.match(r"--- REPO: (\S+)", line)
        if m:
            current_repo = m.group(1)
        if "STALE:" in line and current_repo:
            blockers.append([now, current_repo, "Scrum Master", "MEDIUM",
                             line.strip().strip("*").strip(), "",
                             "Discuss at standup or deprioritize", "No"])
except Exception as e:
    print(f"Blockers: context parse failed: {e}")

# 2. 'Open Blockers' section of the agenda
if "Open Blockers" in AGENDA:
    tail = AGENDA.split("Open Blockers", 1)[1]
    for line in tail.splitlines():
        s = line.strip().lstrip("-*").strip()
        if not s or len(s) < 10:
            continue
        if s.startswith("**") or s.lower().startswith("outstanding"):
            break
        repo = ""
        m = re.search(r"\[([a-z0-9-]+)\]", s)
        if m: repo = m.group(1)
        blockers.append([now, repo or "(multi)", "AI Agenda", "LOW",
                         s[:400], "", "Raise at weekly scrum", "No"])

if not blockers:
    print("Blockers: none detected")
    sys.exit(0)

try:
    gc = get_sheets_client()
    ss = gc.open_by_key(SHEET_ID)
    try:
        ws = ss.worksheet("Blockers")
    except Exception:
        ws = ss.add_worksheet(title="Blockers", rows=500, cols=8)
        ws.append_row(["Date","Repo","Source","Severity","Blocker","Issue/PR","Action Needed","Resolved"])
    for row in blockers:
        ws.append_row(row)
    print(f"Blockers: appended {len(blockers)} row(s)")
except Exception as e:
    print(f"Blockers append failed: {e}")
PYEOF
fi


# ── 4. Update Google Sheet ─────────────────────────────────────────
log "Updating Google Sheet"
SHEET_URL=$(cd "$HOME/Documents/New project" && python3 "$HOME/.local/bin/mdrt-meeting-sheet.py" 2>/dev/null || echo "")
if [[ -n "$SHEET_URL" ]]; then
  log "Google Sheet updated: $SHEET_URL"
else
  log "Google Sheet update failed (non-fatal)"
  SHEET_ID_FILE="$HOME/.local/share/mdrt-meeting/sheet_id.txt"
  if [[ -f "$SHEET_ID_FILE" ]]; then
    SHEET_URL="https://docs.google.com/spreadsheets/d/$(cat "$SHEET_ID_FILE")"
  else
    SHEET_URL=""
  fi
fi

# ── 5. Send to Lark ────────────────────────────────────────────────
LARK_TEXT=$(echo "$AGENDA" | sed 's/\[\[\([^]|]*\)\]\]/\1/g; s/\[\[[^|]*|\([^]]*\)\]\]/\1/g')

LARK_TEXT="${LARK_TEXT}

---
**Join:** [Google Meet](https://meet.google.com/pjz-jeuo-iuk) | 5:00 - 6:00 PM SGT"

if [[ -n "$SHEET_URL" ]]; then
  LARK_TEXT="${LARK_TEXT}
**Meeting Sheet:** [Open Google Sheet](${SHEET_URL}) -- check off items, add comments, and drop tasks for the AI agent"
fi

curl -s -X POST "$LARK_MDRT_WEBHOOK" \
  -H "Content-Type: application/json" \
  -d "$(cat <<PAYLOAD
{
  "msg_type": "interactive",
  "card": {
    "header": {
      "title": {
        "tag": "plain_text",
        "content": "MDRT Apps Weekly Agenda -- $TODAY"
      },
      "template": "orange"
    },
    "elements": [
      {
        "tag": "markdown",
        "content": $(echo "$LARK_TEXT" | python3 -c 'import sys,json; print(json.dumps(sys.stdin.read()))')
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

log "Agenda sent successfully ($TOTAL_COMMITS commits across ${#REPOS[@]} repos)"

# ── 6. Sync dashboard repo ─────────────────────────────────────────
"$HOME/.local/bin/mdrt-sync-dashboard.sh" 2>> "$LOG_FILE" || log "Dashboard sync failed (non-fatal)"

/usr/bin/python3 -c "
import sys, os, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0, os.path.expanduser('~/Documents/New project/tools'))
from lib.heartbeat import beat
beat('mdrt-scrum-master', {'commits': $TOTAL_COMMITS})
" 2>> "$LOG_FILE" || true

echo "MDRT scrum master agenda sent: $TODAY"
