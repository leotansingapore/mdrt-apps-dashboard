# MDRT Apps Dashboard

Central hub for the MDRT Team Apps ecosystem -- product requirements, architecture diagrams, and weekly meeting automation.

## Quick Links

| What | Link |
|------|------|
| **Google Meet (weekly)** | https://meet.google.com/pjz-jeuo-iuk |
| **Meeting Sheet** | https://docs.google.com/spreadsheets/d/1ZmbroGZKQYS1Wu-RWFxvOw0unzvah5Fs_DTApGGMODo |
| **Ecosystem PRD** | [prds/ECOSYSTEM-PRD.md](prds/ECOSYSTEM-PRD.md) |
| **All PRDs** | [prds/](prds/) |

| App PRD | Repo |
|---------|------|
| [Quick Schedule Pal](prds/quick-schedule-pal/PRD.md) | [quick-schedule-pal](https://github.com/leotansingapore/quick-schedule-pal) |
| [Growing Age Calculator](prds/growing-age-calculator/PRD.md) | [growing-age-calculator](https://github.com/leotansingapore/growing-age-calculator) |
| [Agency Launchpad 90](prds/agency-launchpad-90/PRD.md) | [agency-launchpad-90](https://github.com/leotansingapore/agency-launchpad-90) |
| [AIA Product Compass Hub](prds/aia-product-compass-hub/PRD.md) | [aia-product-compass-hub](https://github.com/leotansingapore/aia-product-compass-hub) |
| [TrackerAttendance](prds/trackerattendance/PRD.md) | [trackerattendance](https://github.com/leotansingapore/trackerattendance) |
| [Activity Tracker](prds/remix-of-activity-tracker/PRD.md) | [remix-of-activity-tracker](https://github.com/leotansingapore/remix-of-activity-tracker) |
| [Agent Rank Dash](prds/agent-rank-dash/PRD.md) | [agent-rank-dash](https://github.com/leotansingapore/agent-rank-dash) |
| [BeeHive Finance Hub](prds/bee-hive-finance-hub/PRD.md) | [bee-hive-finance-hub](https://github.com/leotansingapore/bee-hive-finance-hub) |
| [Loyalty Link Access](prds/loyalty-link-access/PRD.md) | [loyalty-link-access](https://github.com/leotansingapore/loyalty-link-access) |

## The Ecosystem

Nine apps that support MDRT-level financial advisory team operations:

| App | What it does | Key Contributors | Status |
|-----|-------------|-----------------|--------|
| **Activity Tracker** | Activity tracking, gamification, DISC assessment, coaching, commissions | Harold, Jilian, Leo | Very Active |
| **BeeHive Finance Hub** | Singapore financial planning simulator -- CPF, HDB, insurance, retirement | Jilian, Leo | Very Active |
| **Agent Rank Dash** | Agent performance tracking, EPS, pledge sheets, incentives | Lovable Bot | Active |
| **TrackerAttendance** | Training event attendance tracking and check-in | -- | Active |
| **Agency Launchpad 90** | Agency building and launch management | -- | Active |
| **AIA Product Compass Hub** | AIA product reference and comparison tool | -- | Active |
| **Quick Schedule Pal** | Appointment scheduling for advisors | -- | Active |
| **Growing Age Calculator** | Age-based financial planning calculator | -- | Active |
| **Loyalty Link Access** | DISC + Enneagram personality assessments, PDF reports | Lovable Bot | Moderate |

### Common themes across apps

- **Financial advisory tools** -- calculators, product comparison, client profiling
- **Team management** -- attendance, performance tracking, coaching
- **Gamification** -- achievements, challenges, clubs, ranking
- **Singapore-specific** -- CPF, HDB, MediShield, SRS, IRAS tax brackets

## Weekly Meeting Automation

Every Tuesday, automations run for the MDRT Team Apps weekly scrum call:

| Time (SGT) | What happens | Script |
|------------|-------------|--------|
| **4:00 PM** | Lark reminder with Google Meet link | `mdrt-meeting-reminder.sh` |
| **4:30 PM** | Scrum agenda posted to Lark (GitHub activity from all 9 repos) + Google Sheet updated | `mdrt-scrum-master.sh` |
| **5:00-6:00 PM** | Meeting on Google Meet (Fireflies records) | -- |

### What the automation does

1. **Pre-meeting** -- Fetches commits, PRs, and issues from all 9 repos. Uses Claude CLI to generate a scrum-style agenda. Posts to Lark with clickable repo links and a Google Meet button.

2. **Meeting sheet** -- Creates a Google Sheet tab for each meeting with sections for team updates (pre-filled with GitHub commits), PRD progress tracking, discussion topics, action items, and AI agent task requests.

### Setup

All scripts are in [`automation/`](automation/) and scheduled via macOS launchd.

**Requirements:**
- `gh` CLI authenticated with repo access
- `claude` CLI (Claude Max subscription)
- `LARK_MDRT_WEBHOOK` in `.env`
- Google Sheets service account (`credentials.json`)
- macOS (launchd scheduling)

**Manual run:**
```bash
# Send reminder now
~/.local/bin/mdrt-meeting-reminder.sh

# Generate agenda now
~/.local/bin/mdrt-scrum-master.sh
```

## Tech Stack (common across apps)

- **Frontend:** React 18 + TypeScript + Vite + Tailwind + shadcn/ui + Radix UI
- **Backend:** Supabase (where applicable)
- **AI Dev:** Lovable / GPT Engineer for rapid prototyping
- **Deployment:** Lovable Cloud / Vercel
- **Mobile:** Capacitor (Activity Tracker)
- **Notifications:** Lark webhooks
- **Scheduling:** macOS launchd

## Workflow SOP

Full documentation: [automation/co_apps_meeting.md](automation/co_apps_meeting.md) *(uses same pattern as CO Apps)*
