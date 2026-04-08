#!/usr/bin/env python3
"""MDRT Team Apps Weekly Scrum -- Google Sheet Agenda"""

import json
import os
import subprocess
import sys
from datetime import datetime, timedelta

sys.path.insert(0, os.path.join(os.environ["HOME"], "Documents/New project/tools"))
from lib.sheets import get_sheets_client

SHEET_ID_FILE = os.path.join(os.environ["HOME"], ".local/share/mdrt-meeting/sheet_id.txt")
STATE_FILE = os.path.join(os.environ["HOME"], ".local/share/mdrt-meeting/state.json")
TODAY = datetime.now().strftime("%Y-%m-%d")
SINCE = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%dT00:00:00Z")

APPS = [
    {"name": "Quick Schedule Pal", "repo": "quick-schedule-pal", "owner": ""},
    {"name": "Growing Age Calculator", "repo": "growing-age-calculator", "owner": ""},
    {"name": "Agency Launchpad 90", "repo": "agency-launchpad-90", "owner": ""},
    {"name": "AIA Product Compass Hub", "repo": "aia-product-compass-hub", "owner": ""},
    {"name": "TrackerAttendance", "repo": "trackerattendance", "owner": ""},
    {"name": "Activity Tracker", "repo": "remix-of-activity-tracker", "owner": ""},
    {"name": "Agent Rank Dash", "repo": "agent-rank-dash", "owner": ""},
    {"name": "BeeHive Finance Hub", "repo": "bee-hive-finance-hub", "owner": ""},
    {"name": "Loyalty Link Access", "repo": "loyalty-link-access", "owner": ""},
]


def load_action_items():
    try:
        with open(STATE_FILE) as f:
            state = json.load(f)
        return [a for a in state.get("action_items", []) if a.get("status") != "done"]
    except Exception:
        return []


def get_commit_summary(repo):
    try:
        r = subprocess.run(
            ["gh", "api", f"repos/leotansingapore/{repo}/commits?since={SINCE}&per_page=20",
             "--jq", '.[] | "\(.commit.author.name): \(.commit.message | split("\\n")[0])"'],
            capture_output=True, text=True, timeout=15
        )
        commits = [c.strip() for c in r.stdout.strip().split("\n") if c.strip()]
        if commits:
            by_author = {}
            for c in commits:
                parts = c.split(": ", 1)
                author = parts[0] if len(parts) > 1 else "Unknown"
                msg = parts[1] if len(parts) > 1 else c
                by_author.setdefault(author, []).append(msg)
            parts = []
            for author, msgs in by_author.items():
                parts.append(f"{author}: " + "; ".join(msgs[:3]))
            return ". ".join(parts)
        return "(no commits this week)"
    except Exception:
        return "(could not fetch)"


def main():
    sheet_id = None
    if os.path.exists(SHEET_ID_FILE):
        sheet_id = open(SHEET_ID_FILE).read().strip()

    gc = get_sheets_client()

    if not sheet_id:
        # Create new sheet
        spreadsheet = gc.create("MDRT Team Apps Weekly Meeting")
        spreadsheet.share("tanjunsing8@gmail.com", perm_type="user", role="writer")
        with open(SHEET_ID_FILE, "w") as f:
            f.write(spreadsheet.id)
        sheet_id = spreadsheet.id
    else:
        spreadsheet = gc.open_by_key(sheet_id)

    action_items = load_action_items()

    tab_name = TODAY
    try:
        ws = spreadsheet.worksheet(tab_name)
        ws.clear()
    except Exception:
        ws = spreadsheet.add_worksheet(title=tab_name, rows=140, cols=6)

    rows = []
    r = rows.append

    r([f"MDRT Team Apps Weekly Scrum -- {TODAY}", "", "", "", "", ""])
    r(['=HYPERLINK("https://meet.google.com/pjz-jeuo-iuk","Meeting: 5:00-6:00 PM SGT | Click to join Google Meet")', "", "", "", "", ""])
    r(["", "", "", "", "", ""])

    # Follow-ups
    r(["FOLLOW-UPS FROM LAST WEEK", "Owner", "Status", "Done?", "Notes", ""])
    if action_items:
        for item in action_items:
            r([item.get("title", ""), item.get("assignee", ""), item.get("status", "open"), "", "", ""])
    else:
        r(["Nothing outstanding -- all clear", "", "", "", "", ""])
    r(["", "", "", "", "", ""])

    # Team updates
    r(["TEAM UPDATES", "", "", "", "", ""])
    r(["", "What I did last week", "What I'm doing this week", "Any blockers?", "Help needed?", ""])
    for app in APPS:
        owner = app["owner"] if app["owner"] else "(unassigned)"
        summary = get_commit_summary(app["repo"])
        r([f"{owner} -- {app['name']}", summary, "", "", "", ""])
    r(["Leo -- Overall / Cross-app", "", "", "", "", ""])
    r(["", "", "", "", "", ""])

    # PRD Progress
    prd_links = {app["name"]: f'https://github.com/leotansingapore/mdrt-apps-dashboard/blob/main/prds/{app["repo"]}/PRD.md' for app in APPS}

    r(["PRD PROGRESS -- WHERE WE ARE vs WHERE WE WANT TO BE", "", "", "", "", ""])
    r(["App", "Current state (where we are)", "Next milestone (where we want to be)", "% complete", "What's blocking us?", "PRD link"])
    for app in APPS:
        link = prd_links.get(app["name"], "")
        formula = f'=HYPERLINK("{link}","View PRD")' if link else ""
        summary = get_commit_summary(app["repo"])
        current = summary[:200] if summary != "(no commits this week)" else "No activity this week"
        r([app["name"], current, "", "", "", formula])
    r(["", "", "", "", "", ""])

    # Decisions
    r(["DECISIONS TO MAKE", "Options", "Decision", "Owner", "Deadline", ""])
    for _ in range(4):
        r(["", "", "", "", "", ""])
    r(["", "", "", "", "", ""])

    # Open Discussion
    r(["OPEN DISCUSSION", "Raised by", "Discussed?", "Notes / Outcome", "", ""])
    for _ in range(5):
        r(["", "", "", "", "", ""])
    r(["", "", "", "", "", ""])

    # Action Items
    r(["NEW ACTION ITEMS (fill in during meeting)", "Owner", "App", "Due by", "Notes", ""])
    for _ in range(8):
        r(["", "", "", "", "", ""])
    r(["", "", "", "", "", ""])

    # AI Agent Tasks
    r(["TASKS FOR THE AI AGENT", "App", "Priority", "Status", "Describe what you want done", ""])
    r(["(The AI agent will read this section after the meeting and work on these)", "", "", "", "", ""])
    for _ in range(6):
        r(["", "", "", "", "", ""])

    # Write rows
    ws.update(range_name="A1", values=rows, value_input_option="USER_ENTERED")

    # Formatting
    ws.format("A1:F1", {
        "backgroundColor": {"red": 0.6, "green": 0.3, "blue": 0.0},
        "textFormat": {"bold": True, "fontSize": 14,
                       "foregroundColor": {"red": 1, "green": 1, "blue": 1}},
    })
    ws.format("A2:F2", {
        "backgroundColor": {"red": 0.95, "green": 0.9, "blue": 0.8},
        "textFormat": {"fontSize": 10, "italic": True},
    })

    section_labels = [
        "FOLLOW-UPS FROM LAST WEEK",
        "TEAM UPDATES",
        "PRD PROGRESS -- WHERE WE ARE vs WHERE WE WANT TO BE",
        "DECISIONS TO MAKE",
        "OPEN DISCUSSION",
        "NEW ACTION ITEMS (fill in during meeting)",
        "TASKS FOR THE AI AGENT",
    ]
    for i, row in enumerate(rows):
        if row[0] in section_labels:
            row_num = i + 1
            ws.format(f"A{row_num}:F{row_num}", {
                "backgroundColor": {"red": 0.15, "green": 0.15, "blue": 0.15},
                "textFormat": {"bold": True,
                               "foregroundColor": {"red": 1, "green": 1, "blue": 1}},
            })

    # Dropdowns
    app_choices = [app["name"] for app in APPS] + ["General / Cross-app"]
    priority_choices = ["High", "Medium", "Low"]
    status_choices = ["To Do", "In Progress", "Done", "Blocked"]
    percent_choices = ["0%", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

    agent_task_rows = []
    action_item_rows = []
    prd_progress_rows = []
    for i, row in enumerate(rows):
        if row[0] == "TASKS FOR THE AI AGENT":
            agent_task_rows = list(range(i + 2, i + 2 + 6))
        if row[0] == "NEW ACTION ITEMS (fill in during meeting)":
            action_item_rows = list(range(i + 1, i + 1 + 8))
        if row[0] == "PRD PROGRESS -- WHERE WE ARE vs WHERE WE WANT TO BE":
            prd_progress_rows = list(range(i + 2, i + 2 + len(APPS)))

    def make_dropdown(sheet_id, row_start, row_end, col, values):
        return {
            "setDataValidation": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": row_start - 1,
                    "endRowIndex": row_end,
                    "startColumnIndex": col,
                    "endColumnIndex": col + 1,
                },
                "rule": {
                    "condition": {
                        "type": "ONE_OF_LIST",
                        "values": [{"userEnteredValue": v} for v in values],
                    },
                    "showCustomUi": True,
                    "strict": False,
                },
            }
        }

    dropdown_requests = []

    if agent_task_rows:
        first = agent_task_rows[0] + 1
        last = agent_task_rows[-1] + 1
        dropdown_requests.append(make_dropdown(ws.id, first, last, 1, app_choices))
        dropdown_requests.append(make_dropdown(ws.id, first, last, 2, priority_choices))
        dropdown_requests.append(make_dropdown(ws.id, first, last, 3, status_choices))

    if action_item_rows:
        first = action_item_rows[0] + 1
        last = action_item_rows[-1] + 1
        dropdown_requests.append(make_dropdown(ws.id, first, last, 2, app_choices))
        dropdown_requests.append({
            "setDataValidation": {
                "range": {"sheetId": ws.id, "startRowIndex": first - 1, "endRowIndex": last, "startColumnIndex": 3, "endColumnIndex": 4},
                "rule": {"condition": {"type": "DATE_IS_VALID"}, "showCustomUi": True, "strict": False},
            }
        })

    if prd_progress_rows:
        first = prd_progress_rows[0] + 1
        last = prd_progress_rows[-1] + 1
        dropdown_requests.append(make_dropdown(ws.id, first, last, 3, percent_choices))

    body = {
        "requests": dropdown_requests + [
            {"updateDimensionProperties": {
                "range": {"sheetId": ws.id, "dimension": "COLUMNS", "startIndex": 0, "endIndex": 1},
                "properties": {"pixelSize": 350}, "fields": "pixelSize"}},
            {"updateDimensionProperties": {
                "range": {"sheetId": ws.id, "dimension": "COLUMNS", "startIndex": 1, "endIndex": 6},
                "properties": {"pixelSize": 220}, "fields": "pixelSize"}},
        ]
    }
    spreadsheet.batch_update(body)

    # Quick Links tab
    try:
        ql = spreadsheet.worksheet("Quick Links")
        ql.clear()
    except Exception:
        ql = spreadsheet.add_worksheet(title="Quick Links", rows=40, cols=3)

    links = [
        ["MDRT Team Apps -- Quick Links", "", ""],
        ["", "", ""],
        ["Weekly Meeting", "", ""],
        ['=HYPERLINK("https://meet.google.com/pjz-jeuo-iuk","Join Google Meet")', "Tuesdays 5:00-6:00 PM SGT", ""],
        [f'=HYPERLINK("{spreadsheet.url}","Meeting Sheet")', "Auto-filled after each meeting", ""],
        ["", "", ""],
        ["Product Requirements (PRDs)", "", ""],
        ['=HYPERLINK("https://github.com/leotansingapore/mdrt-apps-dashboard/blob/main/prds/ECOSYSTEM-PRD.md","Ecosystem PRD")', "How all 9 apps connect", ""],
    ]
    for app in APPS:
        links.append([
            f'=HYPERLINK("https://github.com/leotansingapore/mdrt-apps-dashboard/blob/main/prds/{app["repo"]}/PRD.md","{app["name"]} PRD")',
            "", "",
        ])
    links.append(["", "", ""])
    links.append(["GitHub Repos", "", ""])
    links.append(['=HYPERLINK("https://github.com/leotansingapore/mdrt-apps-dashboard","MDRT Apps Dashboard")', "PRDs, automation, diagrams", ""])
    for app in APPS:
        links.append([
            f'=HYPERLINK("https://github.com/leotansingapore/{app["repo"]}","{app["name"]}")',
            app["owner"] or "", "",
        ])

    ql.update(range_name="A1", values=links, value_input_option="USER_ENTERED")
    ql.format("A1:C1", {
        "backgroundColor": {"red": 0.6, "green": 0.3, "blue": 0.0},
        "textFormat": {"bold": True, "fontSize": 14, "foregroundColor": {"red": 1, "green": 1, "blue": 1}},
    })
    for label in ["Weekly Meeting", "Product Requirements (PRDs)", "GitHub Repos"]:
        for i, row in enumerate(links):
            if row[0] == label:
                ql.format(f"A{i+1}:C{i+1}", {
                    "backgroundColor": {"red": 0.15, "green": 0.15, "blue": 0.15},
                    "textFormat": {"bold": True, "foregroundColor": {"red": 1, "green": 1, "blue": 1}},
                })
    spreadsheet.batch_update({"requests": [
        {"updateDimensionProperties": {"range": {"sheetId": ql.id, "dimension": "COLUMNS", "startIndex": 0, "endIndex": 1}, "properties": {"pixelSize": 300}, "fields": "pixelSize"}},
        {"updateDimensionProperties": {"range": {"sheetId": ql.id, "dimension": "COLUMNS", "startIndex": 1, "endIndex": 2}, "properties": {"pixelSize": 350}, "fields": "pixelSize"}},
    ]})

    try:
        spreadsheet.del_worksheet(spreadsheet.worksheet("Sheet1"))
    except Exception:
        pass

    print(spreadsheet.url)


if __name__ == "__main__":
    main()
