# PRD: Growing Age Calculator

Version: 1.1 | Date: 2026-04-08 | Status: Active | Owner: Leo Tan

## 1. Introduction

Growing Age Calculator is an age-based financial planning calculator with VitalHealth plan features. It helps financial advisors illustrate how a client's financial needs, insurance coverage gaps, and investment horizons change across life stages. It features dark mode support and responsive design. With 7,817 commits, it has the highest commit count of any app in the ecosystem.

## 2. Goals

| ID | Goal | Success Metric |
|----|------|---------------|
| G-01 | Visualize financial milestones by age for clients | Advisors use the tool in 50%+ of client presentations |
| G-02 | Showcase VitalHealth plan features clearly | Clients understand VitalHealth benefits after one session |
| G-03 | Identify coverage gaps at each life stage | Tool flags gaps for 100% of incomplete profiles |
| G-04 | Simplify complex age-based financial concepts | Client comprehension rating above 4/5 |

## 3. User Roles

| Role | Description |
|------|------------|
| Advisor | Inputs client age and profile; presents age-based projections and VitalHealth features |
| Client (view-only) | Views personalized age-based financial timeline |

## 4. Core Features

| Feature | Description |
|---------|------------|
| Age-Based Timeline | Visual financial journey from current age to retirement |
| VitalHealth Plan Features | Integrated VitalHealth product education and illustration |
| Singapore Milestones | CPF withdrawal ages, retirement thresholds, MediShield, insurance limits |
| Coverage Gap Detection | Identifies insurance gaps by age band |
| Dark Mode | Full dark mode support via design tokens |
| Responsive Design | Mobile-first layout for use in client meetings |
| Shareable Output | Printable/shareable timeline for clients |

## 5. Technical Architecture

| Aspect | Detail |
|--------|--------|
| Stack | React + TypeScript + Vite + Tailwind + shadcn/ui |
| Backend | Supabase |
| Dark Mode | Tailwind dark mode with design tokens |
| Deployment | Vercel |

## 6. Contributors

| Contributor | Commits | Role |
|------------|---------|------|
| `lovable-dev[bot]` | ~7,798 | Primary AI builder |
| `leotansingapore` | 7 | Owner, product direction |
| `j-casimiro` | 7 | Developer |
| `joshua0006` | 3 | Developer |
| `Jehu-RND` | 1 | Contributor |
| `jiliangarette` | 1 | Contributor |
| Total | 7,817 | |

## 7. Non-Goals

- Detailed financial planning or projections (handled by BeeHive Finance Hub)
- Product recommendations beyond VitalHealth (handled by AIA Product Compass Hub)
- Commission calculations

## 8. Success Metrics

| Metric | Target |
|--------|--------|
| Advisor usage in client meetings | 50%+ |
| Client comprehension rating | 4/5 or higher |
| Timeline generation time | Under 3 seconds |
| VitalHealth feature clarity score | 4/5 or higher |

## 9. Current Status

| Feature | Status |
|---------|--------|
| Age-based timeline | Production |
| VitalHealth plan features | Production |
| Singapore milestones | Production |
| Coverage gap detection | Production |
| Dark mode | Production |
| Responsive design | Production |
| Shareable output | Production |

## 10. Open Questions

1. Should the calculator integrate with BeeHive Finance Hub for deeper projections?
2. What age-specific products or events should be configurable by admin?
3. Is there demand for a printable PDF version of the timeline?
