# PRD: Activity Tracker

Version: 1.0 | Date: 2026-04-08 | Status: Active | Owner: Leo Tan

## 1. Introduction

Activity Tracker is the flagship application in the MDRT Team Apps ecosystem with over 7,010 commits. It provides financial advisors with a gamified activity tracking system that integrates DISC personality assessments, coaching workflows, commission calculations, and employee performance tracking. A mobile app is available via Capacitor for Android and iOS.

## 2. Goals

| ID | Goal | Success Metric |
|----|------|---------------|
| G-01 | Track daily advisor activities with gamification | 90% of team logs activities daily |
| G-02 | Drive performance through achievements, clubs, and challenges | 70% of advisors earn at least one achievement per quarter |
| G-03 | Enable coaches to monitor and guide advisors | Coaches review advisor dashboards weekly |
| G-04 | Provide accurate commission projections | Commission calculator matches actual payouts within 5% |
| G-05 | Deliver a native mobile experience | Mobile app ratings above 4.0 on both stores |

## 3. User Roles

| Role | Description |
|------|------------|
| Advisor | Logs activities, tracks progress, views achievements and commissions |
| Coach | Monitors team activities, provides feedback, manages challenges |
| Agency Leader | Views aggregate performance, manages EPS, configures gamification |
| Admin | Manages users, roles, system configuration |

## 4. User Stories

| ID | Story | Acceptance Criteria |
|----|-------|-------------------|
| US-01 | As an advisor, I want to log my daily activities so I can track my progress toward goals | Activity logged with type, count, date; reflected in dashboard within 5 seconds |
| US-02 | As an advisor, I want to see my achievements and club status so I stay motivated | Achievements page shows earned and locked badges; club tier updates in real time |
| US-03 | As a coach, I want to view my team's activity summaries so I can identify who needs support | Team dashboard shows activity counts, streaks, and flagged advisors |
| US-04 | As an advisor, I want to calculate my projected commissions so I can plan my income | Commission calculator accepts policy inputs and returns projected amounts |
| US-05 | As an admin, I want to manage challenges so I can drive specific behaviors | Create/edit/archive challenges with targets, date ranges, and rewards |
| US-06 | As an advisor, I want to complete my DISC assessment so my coach can personalize guidance | DISC questionnaire completes in under 10 minutes; results stored and visible to coach |

## 5. Functional Requirements

| ID | Requirement |
|----|------------|
| FR-01 | Activity logging with configurable activity types and daily/weekly/monthly views |
| FR-02 | Gamification engine: achievements, clubs, challenges with progress tracking |
| FR-03 | DISC personality assessment with result storage and coach visibility |
| FR-04 | Coaching dashboard with team-level and individual advisor views |
| FR-05 | Commission calculator supporting multiple product types and tiers |
| FR-06 | EPS (Employee Performance System) tracking and reporting |
| FR-07 | Drag-and-drop UI via dnd-kit for reordering and organizing |
| FR-08 | Rich text content editing via Editor.js |
| FR-09 | Mobile app (Android/iOS) via Capacitor with push notifications |
| FR-10 | Clerk authentication with role-based access control |

## 6. Non-Goals

- Financial planning or product recommendations (handled by BeeHive and AIA Product Compass)
- Event attendance tracking (handled by Tracker Attendance)
- Detailed personality reports with PDF export (handled by Loyalty Link Access)

## 7. Technical Considerations

| Aspect | Detail |
|--------|--------|
| Stack | React + TypeScript + Vite + Tailwind + shadcn/ui |
| Auth | Clerk |
| Database | Supabase |
| Mobile | Capacitor (Android + iOS) |
| Drag-and-Drop | dnd-kit |
| Rich Text | Editor.js |
| Deployment | Vercel (remix-of-activity-tracker.vercel.app) |

## 8. Success Metrics

| Metric | Target |
|--------|--------|
| Daily active users | 80% of team |
| Activity log completion rate | 90% daily |
| Mobile app adoption | 60% of users on mobile |
| Coach dashboard usage | Weekly by all coaches |
| Achievement unlock rate | 70% earn 1+ per quarter |

## 9. Current Status

| Feature | Status |
|---------|--------|
| Activity logging | Shipped |
| Gamification (achievements, clubs, challenges) | Shipped |
| DISC assessment | Shipped |
| Coaching dashboard | Shipped |
| Commission calculator | Shipped |
| EPS tracking | Shipped |
| Mobile app (Capacitor) | Shipped |
| Editor.js content | Shipped |
| Drag-and-drop (dnd-kit) | Shipped |

## 10. Open Questions

1. What is the retention strategy for historical activity data (archiving vs. permanent storage)?
2. How will push notification content be managed for the mobile app?
3. Should the DISC assessment be migrated to Loyalty Link Access or remain embedded?
4. What is the plan for offline-first support on mobile?
5. How will EPS data sync with Agent Rank Dash to avoid duplication?

### Contributors

| Contributor | Commits |
|------------|---------|
| lovable-dev[bot] | 6,983 |
| haroldcalayan | 67 |
| leotansingapore | 51 |
| Jehu-RND | 9 |
