# PRD: MDRT Team Apps Ecosystem

Version: 1.1 | Date: 2026-04-08 | Status: Active | Owner: Leo Tan

## 1. Introduction

The MDRT Team Apps Ecosystem is a comprehensive toolkit built for MDRT-level financial advisory teams operating in Singapore. It spans nine purpose-built applications covering financial planning, team management, gamification, performance tracking, and personality assessments. All apps are designed to support the daily workflows of financial advisors, agency leaders, and their support staff.

## 2. The Nine Apps

| # | App | Repository | Purpose | Commits |
|---|-----|-----------|---------|---------|
| 1 | Activity Tracker | `remix-of-activity-tracker` | Activity tracking with gamification, coaching, DISC, commissions | 7,010 |
| 2 | Growing Age Calculator | `growing-age-calculator` | VitalHealth plan features, age-based financial planning | 7,817 |
| 3 | Tracker Attendance | `trackerattendance` | Full attendance tracking, QR check-in, leave requests, pet gamification | 6,803 |
| 4 | BeeHive Finance Hub | `bee-hive-finance-hub` | Singapore financial planning simulator (CPF, HDB, tax, insurance) | 4,275 |
| 5 | AIA Product Compass Hub (FINternship) | `aia-product-compass-hub` | Financial advisory training, AI roleplay, CMFAS exam prep | 3,085 |
| 6 | Agent Rank Dash | `agent-rank-dash` | EPS performance tracking, pledges, incentives | 1,371 |
| 7 | Agency Launchpad 90 (AdBlueprint) | `agency-launchpad-90` | Meta ads management, campaign creation, lead gen | 791 |
| 8 | Loyalty Link Access | `loyalty-link-access` | DISC and Enneagram personality assessments | 754 |
| 9 | Quick Schedule Pal | `quick-schedule-pal` | Coaching session booking with Google Calendar integration | 109 |

## 3. Common Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | React + TypeScript |
| Build | Vite |
| Styling | Tailwind CSS + shadcn/ui |
| Backend | Supabase (Postgres, Auth, Edge Functions) |
| Auth | Clerk (Activity Tracker), Supabase Auth (others) |
| AI Builder | Lovable AI |
| Hosting | Vercel |
| Mobile | Capacitor (Activity Tracker, Tracker Attendance) |

## 4. Shared Themes

- **Financial Advisory**: Tools purpose-built for insurance and wealth management workflows in Singapore
- **Team Management**: Agency-level dashboards, performance tracking, pledge management
- **Gamification**: Achievements, clubs, challenges, leaderboards, pet systems across multiple apps
- **Singapore-Specific**: CPF, HDB, MediShield, SRS, IRAS tax brackets, AIA product integration
- **Personality-Driven**: DISC and Enneagram assessments integrated into coaching and team building
- **AI-Powered**: Claude CLI integration, AI roleplay training, self-improving scheduling

## 5. Key Contributors

| Contributor | Commits | Primary Apps |
|------------|---------|-------------|
| `lovable-dev[bot]` | Primary builder | All apps (AI builder, highest commit count across ecosystem) |
| `jiliangarette` | 756 + others | Agency Launchpad (756!), BeeHive (162), TrackerAttendance (64), AIA Compass (49), Activity Tracker |
| `haroldcalayan` | 169 | Activity Tracker (67), TrackerAttendance (102) |
| `joshua0006` | 35 | AIA Compass (32), Growing Age Calculator (3) |
| `r123198` | 10 | TrackerAttendance (10) |
| `Jehu-RND` | 9 | Activity Tracker (9) |
| `j-casimiro` | 7 | Growing Age Calculator (7) |
| `leotansingapore` (Leo) | Owner | Owner and contributor across all apps |
| `avyldemesa` | 3 | TrackerAttendance (3) |
| `claude` | 25 | AIA Compass (18), Quick Schedule Pal (7) |

## 6. Current Status

| App | Status | Maturity |
|-----|--------|----------|
| Activity Tracker | Active, flagship | Production -- mobile apps via Capacitor |
| Growing Age Calculator | Active | Production -- 7,817 commits |
| Tracker Attendance | Active | Production -- mobile via Capacitor, 35+ Edge Functions |
| BeeHive Finance Hub | Active | Production -- wave-based bug fix cycles |
| AIA Product Compass Hub (FINternship) | Active | Production -- 90+ custom hooks |
| Agent Rank Dash | Active | Production |
| Agency Launchpad 90 (AdBlueprint) | Active | Production -- real Meta ad accounts, safety-critical |
| Loyalty Link Access | Active | Production |
| Quick Schedule Pal | Active | MVP -- self-improving AI system |

## 7. Goals

| ID | Goal | Success Metric |
|----|------|---------------|
| G-01 | Provide a unified toolkit for MDRT-level advisory teams | All 9 apps actively used by team members |
| G-02 | Reduce manual admin work for agency leaders | 50% reduction in time spent on tracking and reporting |
| G-03 | Increase advisor engagement through gamification | Monthly active usage above 80% of team |
| G-04 | Deliver Singapore-specific financial planning accuracy | CPF/HDB/tax calculations validated against government sources |
| G-05 | Enable data-driven coaching and performance management | Coaches can access advisor metrics in under 30 seconds |

## 8. Architecture Principles

- Each app is an independent, self-contained deployment -- no cross-app imports
- Supabase provides the shared data layer where needed
- Lovable AI is the primary builder; human developers handle complex features and integrations
- Mobile-first responsive design across all apps
- Dark mode support via Tailwind/shadcn design tokens

## 9. Open Questions

1. Should apps share a single Supabase project or maintain separate databases?
2. What is the SSO/unified login strategy across the ecosystem?
3. How will cross-app data (e.g., DISC results used in Activity Tracker coaching) be synchronized?
4. Is there a plan for a unified dashboard that aggregates data from all 9 apps?
5. What is the deprecation strategy for apps that overlap in functionality?
