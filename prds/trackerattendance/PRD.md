# PRD: Tracker Attendance

Version: 1.1 | Date: 2026-04-08 | Status: Active | Owner: Leo Tan

## 1. Introduction

Tracker Attendance is a full-featured attendance tracking and team management platform for Win Financial Group. It handles event attendance via QR code scanning and geolocation, leave request workflows, pet gamification, org chart visualization, analytics dashboards, and Lark webhook notifications. The app runs as a mobile app via Capacitor 7.4 (iOS/Android) and as a web app.

## 2. Goals

| ID | Goal | Success Metric |
|----|------|---------------|
| G-01 | Replace manual attendance sheets with digital QR check-in | 100% of events use digital check-in |
| G-02 | Provide real-time attendance visibility with geolocation | Attendance count updates within 5 seconds of check-in |
| G-03 | Streamline leave request and approval workflows | Leave requests processed within 24 hours |
| G-04 | Increase engagement through pet gamification | 70%+ of users interact with pet system weekly |
| G-05 | Generate compliance reports for management | Reports exportable within 1 minute of event end |

## 3. User Roles

| Role | Description |
|------|------------|
| Consultant | Checks in to events via QR code, manages leave requests, interacts with pet system |
| Manager | Monitors team attendance, approves leave requests, views analytics |
| Admin | Manages events, org chart, compliance rules, user access, system configuration |

## 4. Core Features

| Feature | Description |
|---------|------------|
| QR Code Check-in | Scan-based event check-in with confirmation |
| Geolocation Tracking | Location verification during check-in |
| Event Management | Create, edit, and manage training/meeting events |
| Leave Request Workflow | Submit, approve, reject leave requests with audit trail |
| Pet Gamification | Virtual pet system tied to attendance and engagement |
| Org Chart | Visual team hierarchy and reporting structure |
| Analytics Dashboards | Attendance rates, trends, team comparisons |
| Lark Webhooks | Real-time notifications to Lark for check-ins and events |
| Report Export | CSV/PDF attendance reports for compliance |

## 5. Technical Architecture

| Aspect | Detail |
|--------|--------|
| Stack | React + TypeScript + Vite + Tailwind + shadcn/ui |
| Backend | Supabase (project: eqgopcqmcjyqliwhmsbf) |
| Edge Functions | 35+ Supabase Edge Functions |
| Custom Hooks | 90+ React hooks |
| Mobile | Capacitor 7.4 (iOS + Android) |
| Testing | Playwright (E2E) + Vitest (unit) |
| Notifications | Lark webhook integration |
| Deployment | Vercel |

## 6. Contributors

| Contributor | Commits | Role |
|------------|---------|------|
| `lovable-dev[bot]` | ~6,627 | Primary AI builder |
| `haroldcalayan` | 102 | Developer -- core features |
| `jiliangarette` | 64 | Developer -- feature work |
| `r123198` | 10 | Developer |
| `avyldemesa` | 3 | Contributor |
| Total | 6,803 | |

## 7. Non-Goals

- Training content delivery or LMS functionality
- Activity tracking or gamification beyond attendance (handled by Activity Tracker)
- Scheduling or calendar management (handled by Quick Schedule Pal)

## 8. Success Metrics

| Metric | Target |
|--------|--------|
| Digital check-in adoption | 100% of events |
| Check-in to confirmation time | Under 5 seconds |
| Leave request processing | Under 24 hours |
| Report generation time | Under 1 minute |
| Attendance data accuracy | 99%+ |

## 9. Current Status

| Feature | Status |
|---------|--------|
| QR code check-in | Production |
| Geolocation tracking | Production |
| Event management | Production |
| Leave request workflow | Production |
| Pet gamification | Production |
| Org chart | Production |
| Analytics dashboards | Production |
| Lark webhooks | Production |
| Report export | Production |
| Capacitor mobile app | Production |

## 10. Open Questions

1. Should attendance data integrate with Activity Tracker for CPD credits?
2. How will attendance data be used for compliance reporting to AIA or MAS?
3. Plans for offline check-in support when connectivity is poor?
