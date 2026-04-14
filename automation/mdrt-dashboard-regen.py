#!/usr/bin/python3
"""
Regenerate index.html for the mdrt-apps-dashboard GitHub Pages site.
"""
from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path

REPO = Path.home() / ".local/share/mdrt-meeting/dashboard-repo"
APPS = [
    {"name": "Quick Schedule Pal", "slug": "quick-schedule-pal", "desc": "Meeting scheduler for advisors."},
    {"name": "Growing Age Calculator", "slug": "growing-age-calculator", "desc": "Life insurance age calculator tool."},
    {"name": "Agency Launchpad 90", "slug": "agency-launchpad-90", "desc": "90-day agency onboarding playbook."},
    {"name": "AIA Product Compass Hub", "slug": "aia-product-compass-hub", "desc": "AIA product navigator for advisors."},
    {"name": "Tracker Attendance", "slug": "trackerattendance", "desc": "Event and session attendance tracker."},
    {"name": "Activity Tracker", "slug": "remix-of-activity-tracker", "desc": "Daily activity + KPI tracker."},
    {"name": "Agent Rank Dash", "slug": "agent-rank-dash", "desc": "Agent performance leaderboard."},
    {"name": "Bee Hive Finance Hub", "slug": "bee-hive-finance-hub", "desc": "Team finance + commission portal."},
    {"name": "Loyalty Link Access", "slug": "loyalty-link-access", "desc": "Client loyalty + referral portal."},
]
MEET_URL = "https://meet.google.com/pjz-jeuo-iuk"
SHEET_URL = "https://docs.google.com/spreadsheets/d/1ZmbroGZKQYS1Wu-RWFxvOw0unzvah5Fs_DTApGGMODo"


def list_swarm_reports():
    swarm = REPO / "swarm-reports"
    if not swarm.exists():
        return []
    return sorted(swarm.glob("*.md"), reverse=True)[:8]


def extract_summary(md_path: Path) -> str:
    try:
        text = md_path.read_text()
    except Exception:
        return ""
    m = re.search(r"^##\s+Summary\s*$\n+(.+?)(?=^##\s|\Z)", text, re.M | re.S)
    if m:
        summary = m.group(1).strip()
        return summary[:300] + ("..." if len(summary) > 300 else "")
    return text.split("\n", 1)[0].lstrip("# ").strip()[:200]


def apps_cards() -> str:
    parts = []
    for a in APPS:
        prd_path = f"prds/{a['slug']}/PRD.md"
        prd_exists = (REPO / prd_path).exists()
        prd_link = f'<a class="pill" href="{prd_path}">PRD</a>' if prd_exists else '<span class="pill muted">PRD soon</span>'
        parts.append(f"""
  <div class="card">
    <h3>{a['name']}</h3>
    <p>{a['desc']}</p>
    <div class="links">
      {prd_link}
      <a class="pill" href="https://github.com/leotansingapore/{a['slug']}">Repo</a>
    </div>
  </div>""")
    return "".join(parts)


def meetings_list() -> str:
    reports = list_swarm_reports()
    if not reports:
        return '<p class="sub">No meeting logs yet. Check back after Tuesday 17:00 SGT.</p>'
    rows = [f'<div class="card"><h3><a href="swarm-reports/{r.name}">{r.stem}</a></h3><p>{extract_summary(r) or "No summary available."}</p></div>' for r in reports]
    return '<div class="grid grid-2">' + "".join(rows) + "</div>"


def render() -> str:
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>MDRT Apps Dashboard</title>
<style>
:root{{--bg:#0b0d12;--panel:#12151c;--panel-2:#171b24;--border:#232834;--text:#e6e8ee;--muted:#8a92a3;--accent:#6ea8ff;--accent-2:#7ae0b6}}
*{{box-sizing:border-box}}html,body{{margin:0;padding:0;background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,system-ui,sans-serif;font-size:15px;line-height:1.55}}
a{{color:var(--accent);text-decoration:none}}a:hover{{text-decoration:underline}}
.wrap{{max-width:1100px;margin:0 auto;padding:32px 20px 80px}}
header{{display:flex;align-items:baseline;justify-content:space-between;flex-wrap:wrap;gap:8px;margin-bottom:28px}}
h1{{font-size:24px;margin:0}}
.sub{{color:var(--muted);font-size:13px}}
h2{{font-size:14px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);margin:32px 0 12px;font-weight:600}}
.grid{{display:grid;gap:12px}}.grid-2{{grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}}.grid-3{{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}}
.card{{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:14px 16px}}
.card h3{{margin:0 0 4px;font-size:15px;font-weight:600}}.card p{{margin:0;color:var(--muted);font-size:13px}}
.links{{display:flex;gap:10px;flex-wrap:wrap;margin-top:10px;font-size:13px}}
.pill{{background:var(--panel-2);border:1px solid var(--border);padding:4px 10px;border-radius:6px}}.pill.muted{{color:var(--muted)}}
.quick{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px}}
.quick a{{display:block;background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:14px 16px;color:var(--text)}}
.quick a .l{{font-size:13px;color:var(--muted);display:block;margin-bottom:2px}}
.quick a:hover{{border-color:var(--accent);text-decoration:none}}
footer{{margin-top:48px;color:var(--muted);font-size:12px;text-align:center}}
.badge{{display:inline-block;font-size:11px;background:var(--panel-2);border:1px solid var(--border);padding:2px 8px;border-radius:999px;color:var(--muted);margin-left:8px}}
</style></head><body><div class="wrap">
<header><div><h1>MDRT Apps Dashboard <span class="badge">weekly meeting hub</span></h1>
<div class="sub">9 financial advisory team apps -- PRDs, weekly scrum, meeting logs, automation.</div></div></header>
<h2>Quick Links</h2>
<div class="quick">
<a href="{MEET_URL}" target="_blank"><span class="l">Weekly sync</span>Google Meet &rarr;</a>
<a href="{SHEET_URL}" target="_blank"><span class="l">Tracking</span>Meeting Sheet &rarr;</a>
<a href="prds/"><span class="l">Strategy</span>All PRDs &rarr;</a>
<a href="swarm-reports/"><span class="l">Weekly</span>Swarm Reports &rarr;</a>
<a href="https://github.com/leotansingapore/mdrt-apps-dashboard"><span class="l">Source</span>GitHub repo &rarr;</a>
</div>
<h2>The 9 Apps</h2>
<div class="grid grid-2">{apps_cards()}</div>
<h2>Recent Meetings</h2>
{meetings_list()}
<h2>Weekly Automation</h2>
<div class="grid grid-3">
<div class="card"><h3>Tue 16:30 reminder</h3><p>Pre-meeting ping with last week's action items.</p></div>
<div class="card"><h3>Tue 17:00 agenda</h3><p>Scrum master: 7-day GitHub activity summary across 9 repos.</p></div>
<div class="card"><h3>Tue post-meeting log</h3><p>Fireflies transcript &rarr; sheet Meeting Log tab + swarm-reports/*.md.</p></div>
<div class="card"><h3>Sun 20:00 swarm</h3><p>Cross-repo weekly swarm scan, GitHub issues, Lark report.</p></div>
</div>
<p class="sub" style="margin-top:10px">Scripts in <a href="automation/">automation/</a>, scheduled via launchd.</p>
<footer>Auto-generated {now} &middot; <a href="https://github.com/leotansingapore/mdrt-apps-dashboard">leotansingapore/mdrt-apps-dashboard</a></footer>
</div></body></html>
"""


def main():
    if not REPO.exists():
        print(f"Dashboard repo not found at {REPO}", file=sys.stderr)
        sys.exit(1)
    (REPO / "index.html").write_text(render())
    print(f"Wrote {REPO / 'index.html'}")


if __name__ == "__main__":
    main()
