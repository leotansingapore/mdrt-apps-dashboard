# PRD: Agency Launchpad 90

Version: 1.0 | Date: 2026-04-08 | Status: Active | Owner: Leo Tan

## 1. Introduction

Agency Launchpad 90 is a 90-day agency building and launch program management tool. It guides new agency leaders through a structured onboarding plan with milestones, task checklists, and progress tracking designed to accelerate time-to-productivity for newly promoted or recruited agency leaders.

## 2. Goals

| ID | Goal | Success Metric |
|----|------|---------------|
| G-01 | Structure the first 90 days for new agency leaders | 100% of new leaders enrolled in a 90-day plan |
| G-02 | Increase agency leader retention through structured support | 90-day retention rate above 85% |
| G-03 | Track milestone completion to identify at-risk leaders early | At-risk leaders flagged by day 30 |

## 3. User Roles

| Role | Description |
|------|------------|
| New Agency Leader | Follows the 90-day plan, completes milestones and tasks |
| Mentor / Senior Leader | Monitors progress, provides coaching, reviews milestones |
| Admin | Configures 90-day plan templates and milestone definitions |

## 4. User Stories

| ID | Story | Acceptance Criteria |
|----|-------|-------------------|
| US-01 | As a new leader, I want to see my 90-day plan so I know exactly what to do each week | Plan view shows weekly tasks, milestones, and deadlines |
| US-02 | As a mentor, I want to see which milestones my mentees have completed so I can coach proactively | Mentor dashboard shows per-mentee progress with overdue flags |
| US-03 | As a new leader, I want to check off completed tasks so my progress is tracked | Task completion updates progress bar and notifies mentor |
| US-04 | As an admin, I want to create plan templates so new leaders get a consistent onboarding experience | Template editor with week-by-week task and milestone configuration |

## 5. Functional Requirements

| ID | Requirement |
|----|------------|
| FR-01 | 90-day plan with weekly breakdown (Weeks 1-4, 5-8, 9-12) |
| FR-02 | Milestone definitions with completion criteria |
| FR-03 | Task checklists per week with check-off tracking |
| FR-04 | Mentor dashboard with multi-mentee progress view |
| FR-05 | At-risk flagging when milestones are overdue |
| FR-06 | Plan template management for admins |

## 6. Non-Goals

- Ongoing performance tracking beyond 90 days (handled by Agent Rank Dash)
- Activity logging or gamification (handled by Activity Tracker)
- Financial planning tools

## 7. Technical Considerations

| Aspect | Detail |
|--------|--------|
| Stack | React + TypeScript + Vite + Tailwind + shadcn/ui |
| Backend | Supabase |
| Deployment | Vercel |

## 8. Success Metrics

| Metric | Target |
|--------|--------|
| Plan enrollment rate | 100% of new leaders |
| 90-day milestone completion | 80%+ |
| 90-day retention | 85%+ |
| Mentor check-in frequency | Weekly |

## 9. Current Status

| Feature | Status |
|---------|--------|
| 90-day plan view | MVP |
| Task checklists | MVP |
| Milestone tracking | MVP |
| Mentor dashboard | Planned |
| Plan templates | Planned |

## 10. Open Questions

1. Should the 90-day plan be customizable per agency or standardized across all?
2. How will completion data feed into Agent Rank Dash for long-term tracking?
3. Is there a need for automated reminders or nudges for overdue tasks?
