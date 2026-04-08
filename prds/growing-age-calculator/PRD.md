# PRD: Growing Age Calculator

Version: 1.0 | Date: 2026-04-08 | Status: Active | Owner: Leo Tan

## 1. Introduction

Growing Age Calculator is an age-based financial planning calculator that helps financial advisors illustrate how a client's financial needs, insurance coverage gaps, and investment horizons change across life stages. It provides visual timelines tied to Singapore milestones such as CPF withdrawal ages, retirement thresholds, and insurance coverage limits.

## 2. Goals

| ID | Goal | Success Metric |
|----|------|---------------|
| G-01 | Visualize financial milestones by age for clients | Advisors use the tool in 50%+ of client presentations |
| G-02 | Identify coverage gaps at each life stage | Tool flags gaps for 100% of incomplete profiles |
| G-03 | Simplify complex age-based financial concepts | Client comprehension rating above 4/5 |

## 3. User Roles

| Role | Description |
|------|------------|
| Advisor | Inputs client age and profile; presents age-based projections |
| Client (view-only) | Views personalized age-based financial timeline |

## 4. User Stories

| ID | Story | Acceptance Criteria |
|----|-------|-------------------|
| US-01 | As an advisor, I want to input a client's age and profile so I can show their financial timeline | Form accepts age, income, dependents; timeline renders immediately |
| US-02 | As an advisor, I want to highlight key age milestones so the client understands critical deadlines | Timeline marks CPF withdrawal ages, retirement age, insurance expiry |
| US-03 | As a client, I want to see a visual timeline of my financial journey so I can understand my plan | Clear, readable chart showing milestones from current age to retirement |

## 5. Functional Requirements

| ID | Requirement |
|----|------------|
| FR-01 | Age-based financial timeline visualization |
| FR-02 | Singapore milestone markers (CPF ages 55/65, retirement 62/65, MediShield) |
| FR-03 | Insurance coverage gap detection by age band |
| FR-04 | Input form for client demographics and financial basics |
| FR-05 | Shareable/printable timeline output |

## 6. Non-Goals

- Detailed financial planning or projections (handled by BeeHive Finance Hub)
- Product recommendations (handled by AIA Product Compass Hub)
- Commission calculations

## 7. Technical Considerations

| Aspect | Detail |
|--------|--------|
| Stack | React + TypeScript + Vite + Tailwind + shadcn/ui |
| Backend | Supabase |
| Deployment | Vercel |

## 8. Success Metrics

| Metric | Target |
|--------|--------|
| Advisor usage in client meetings | 50%+ |
| Client comprehension rating | 4/5 or higher |
| Timeline generation time | Under 3 seconds |

## 9. Current Status

| Feature | Status |
|---------|--------|
| Age-based timeline | MVP |
| Singapore milestones | MVP |
| Coverage gap detection | Planned |
| Shareable output | Planned |

## 10. Open Questions

1. Should the calculator integrate with BeeHive Finance Hub for deeper projections?
2. What age-specific products or events should be configurable by admin?
3. Is there demand for a printable PDF version of the timeline?
