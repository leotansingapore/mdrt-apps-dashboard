# PRD: Agent Rank Dash

Version: 1.0 | Date: 2026-04-08 | Status: Active | Owner: Leo Tan

## 1. Introduction

Agent Rank Dash is a performance tracking and management application with over 1,371 commits. It provides agency leaders with EPS (Employee Performance System) dashboards, pledge sheet management, incentive tracking, and team vs. individual performance analytics. The app was built entirely by Lovable Bot.

## 2. Goals

| ID | Goal | Success Metric |
|----|------|---------------|
| G-01 | Centralize EPS tracking for the agency | All advisors' EPS data visible in one dashboard |
| G-02 | Streamline pledge sheet management | Pledge submission and approval cycle under 24 hours |
| G-03 | Drive performance through visible incentives | 80% of advisors aware of active incentive targets |
| G-04 | Enable data-driven performance reviews | Leaders reference dashboards in all review meetings |

## 3. User Roles

| Role | Description |
|------|------------|
| Advisor | Submits pledges, views own EPS data and rank |
| Agency Leader | Views team dashboards, approves pledges, manages incentives |
| Admin | Configures EPS tiers, incentive rules, approval workflows |

## 4. User Stories

| ID | Story | Acceptance Criteria |
|----|-------|-------------------|
| US-01 | As an agency leader, I want to see team EPS standings so I can identify top performers and those needing support | Dashboard shows ranked list with EPS scores, trend arrows, and filters |
| US-02 | As an advisor, I want to submit my pledge sheet so my targets are recorded | Pledge form captures targets by product line; confirmation shown on submit |
| US-03 | As an agency leader, I want to approve or return pledge submissions so targets are finalized | Approval queue with approve/reject/comment actions per submission |
| US-04 | As an advisor, I want to see active incentives and my progress so I stay motivated | Incentives page shows target, current progress, deadline, and reward |
| US-05 | As an agency leader, I want to compare team vs. individual performance so I can coach effectively | Side-by-side view of team aggregate vs. individual advisor metrics |

## 5. Functional Requirements

| ID | Requirement |
|----|------------|
| FR-01 | EPS tracking dashboard with individual and team views |
| FR-02 | Pledge sheet creation, submission, and approval workflow |
| FR-03 | Incentive and challenge configuration with progress tracking |
| FR-04 | Team vs. individual performance comparison analytics |
| FR-05 | Data entry forms with validation and approval states |
| FR-06 | Historical performance data with trend visualization |
| FR-07 | Export capabilities for reporting |

## 6. Non-Goals

- Activity logging or gamification beyond incentives (handled by Activity Tracker)
- Financial planning or calculations (handled by BeeHive Finance Hub)
- Personality assessments (handled by Loyalty Link Access)

## 7. Technical Considerations

| Aspect | Detail |
|--------|--------|
| Stack | React + TypeScript + Vite + Tailwind + shadcn/ui |
| Backend | Supabase |
| Auth | Supabase Auth |
| Builder | 100% Lovable Bot |
| Deployment | Vercel |

## 8. Success Metrics

| Metric | Target |
|--------|--------|
| Pledge submission rate | 100% of advisors per cycle |
| Approval turnaround | Under 24 hours |
| Dashboard weekly views by leaders | 3+ per leader |
| Incentive awareness | 80% of advisors |

## 9. Current Status

| Feature | Status |
|---------|--------|
| EPS tracking dashboard | Shipped |
| Pledge sheet management | Shipped |
| Incentive tracking | Shipped |
| Team vs. individual analytics | Shipped |
| Data entry with approval workflow | Shipped |

## 10. Open Questions

1. How should EPS data sync with the Activity Tracker's EPS module to avoid duplication?
2. What is the archive/retention policy for historical pledge sheets?
3. Should incentive rules support automatic reward distribution or remain manual?
4. Is there a need for push notifications when pledges require approval?
5. How will performance data be used in formal HR reviews?
