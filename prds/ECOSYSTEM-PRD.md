# PRD: MDRT Team Apps Ecosystem

Version: 1.0 | Date: 2026-04-08 | Status: Active | Owner: Leo Tan

## 1. Introduction

The MDRT Team Apps Ecosystem is a comprehensive toolkit built for MDRT-level financial advisory teams operating in Singapore. It spans nine purpose-built applications covering financial planning, team management, gamification, performance tracking, and personality assessments. All apps are designed to support the daily workflows of financial advisors, agency leaders, and their support staff.

## 2. The Nine Apps

| # | App | Repository | Purpose | Commits |
|---|-----|-----------|---------|---------|
| 1 | Activity Tracker | `remix-of-activity-tracker` | Activity tracking with gamification, coaching, DISC, commissions | 7,010 |
| 2 | BeeHive Finance Hub | `bee-hive-finance-hub` | Singapore financial planning simulator (CPF, HDB, tax, insurance) | 4,275 |
| 3 | Agent Rank Dash | `agent-rank-dash` | EPS performance tracking, pledges, incentives | 1,371 |
| 4 | Loyalty Link Access | `loyalty-link-access` | DISC and Enneagram personality assessments | 754 |
| 5 | Quick Schedule Pal | `quick-schedule-pal` | Appointment scheduling for financial advisors | -- |
| 6 | Growing Age Calculator | `growing-age-calculator` | Age-based financial planning calculator | -- |
| 7 | Agency Launchpad 90 | `agency-launchpad-90` | 90-day agency building launch program | -- |
| 8 | AIA Product Compass Hub | `aia-product-compass-hub` | AIA product reference and recommendation tool | -- |
| 9 | Tracker Attendance | `trackerattendance` | Training event attendance and check-in system | -- |

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

## 4. Shared Themes

- **Financial Advisory**: Tools purpose-built for insurance and wealth management workflows in Singapore
- **Team Management**: Agency-level dashboards, performance tracking, pledge management
- **Gamification**: Achievements, clubs, challenges, leaderboards across multiple apps
- **Singapore-Specific**: CPF, HDB, MediShield, SRS, IRAS tax brackets, AIA product integration
- **Personality-Driven**: DISC and Enneagram assessments integrated into coaching and team building

## 5. Key Contributors

| Contributor | Role | Primary Apps |
|------------|------|-------------|
| Leo Tan (`leotansingapore`) | Owner, product direction | All apps |
| Harold Calayan (`haroldcalayan`) | Developer | Activity Tracker |
| Jilian Garette (`jiliangarette`) | Developer | BeeHive Finance Hub |
| Jehu (`Jehu-RND`) | Developer | Activity Tracker |
| `chixka000` | Developer | BeeHive Finance Hub |
| Lovable Bot (`lovable-dev[bot]`) | AI builder | All apps (primary author) |

## 6. Current Status

| App | Status | Maturity |
|-----|--------|----------|
| Activity Tracker | Active, flagship | Production -- mobile apps via Capacitor |
| BeeHive Finance Hub | Active | Production -- wave-based bug fix cycles |
| Agent Rank Dash | Active | Production |
| Loyalty Link Access | Active | Production |
| Quick Schedule Pal | Active | MVP |
| Growing Age Calculator | Active | MVP |
| Agency Launchpad 90 | Active | MVP |
| AIA Product Compass Hub | Active | MVP |
| Tracker Attendance | Active | MVP |

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
