# PRD: Agency Launchpad 90 (AdBlueprint)

Version: 1.1 | Date: 2026-04-08 | Status: Active | Owner: Leo Tan

## 1. Introduction

Agency Launchpad 90, internally known as **AdBlueprint**, is a Meta ads management platform. It integrates with the Meta Marketing API v21.0 to enable campaign creation and management across Facebook and Instagram, client account management (multi-tenant), lead generation tools, and ad analytics/reporting. **CRITICAL: This app connects to real ad accounts with real billing -- never activate or unpause campaigns without explicit approval.**

## 2. Goals

| ID | Goal | Success Metric |
|----|------|---------------|
| G-01 | Centralize Meta ad campaign management for advisory teams | All campaigns managed through AdBlueprint |
| G-02 | Simplify multi-client ad account management | Advisors manage 5+ client accounts from one dashboard |
| G-03 | Provide actionable ad performance analytics | Key metrics visible within 10 seconds of dashboard load |
| G-04 | Generate leads through Meta ad campaigns | Lead cost tracked and optimized per campaign |

## 3. User Roles

| Role | Description |
|------|------------|
| Ad Manager | Creates and manages campaigns, monitors performance |
| Client Account Owner | Views their own campaign performance and leads |
| Admin | Manages client accounts, billing connections, safety settings |

## 4. Core Features

| Feature | Description |
|---------|------------|
| Meta Marketing API v21.0 | Full integration for campaign CRUD operations |
| Campaign Management | Create, edit, pause campaigns for Facebook and Instagram |
| Multi-Tenant Clients | Manage multiple client ad accounts from one interface |
| Lead Generation | Lead forms, tracking, and qualification tools |
| Ad Analytics | Performance reporting with spend, reach, conversions, ROAS |
| Safety Controls | Guards against accidental campaign activation/spend |
| Framer Motion | Polished animations and transitions throughout the UI |

## 5. Safety Documentation

| Rule | Detail |
|------|--------|
| Never auto-activate campaigns | All campaign activations require manual confirmation |
| Real billing connected | Ad accounts have real payment methods -- treat as production |
| Budget safeguards | Maximum daily budget limits enforced at app level |
| Pause-only defaults | New campaigns default to paused state |

## 6. Technical Architecture

| Aspect | Detail |
|--------|--------|
| Stack | React + TypeScript + Vite + Tailwind + shadcn/ui |
| Backend | Supabase |
| API | Meta Marketing API v21.0 |
| Animations | Framer Motion |
| Deployment | Vercel |

## 7. Contributors

| Contributor | Commits | Role |
|------------|---------|------|
| `lovable-dev[bot]` | ~15 | AI builder |
| `jiliangarette` | 756 | **Main developer** -- built the vast majority of the app |
| `leotansingapore` | 20 | Owner, product direction |
| Total | 791 | |

## 8. Non-Goals

- Google Ads management (separate tooling)
- Organic social media management
- CRM or full lead pipeline management (handled by lead-scraper)

## 9. Success Metrics

| Metric | Target |
|--------|--------|
| Campaign creation time | Under 5 minutes |
| Dashboard load time | Under 10 seconds |
| Client account onboarding | Under 15 minutes |
| Zero accidental campaign activations | 0 incidents |

## 10. Current Status

| Feature | Status |
|---------|--------|
| Meta API integration | Production |
| Campaign management | Production |
| Multi-tenant clients | Production |
| Lead generation tools | Production |
| Ad analytics | Production |
| Safety controls | Production |
| Framer Motion UI | Production |

## 11. Open Questions

1. Should the platform expand to support Google Ads alongside Meta?
2. How will lead data from Meta campaigns feed into other ecosystem apps?
3. What is the escalation path if a campaign is accidentally activated?
