# PRD: BeeHive Finance Hub

Version: 1.0 | Date: 2026-04-08 | Status: Active | Owner: Leo Tan

## 1. Introduction

BeeHive Finance Hub is a Singapore-specific financial planning simulator with over 4,275 commits. It enables financial advisors to model client portfolios covering CPF projections, HDB planning, MediShield, SRS, IRAS tax calculations, insurance planning (AIA products), and retirement/property/education goals. An AI chatbot powered by Gemini 2.5 Pro provides conversational planning assistance.

## 2. Goals

| ID | Goal | Success Metric |
|----|------|---------------|
| G-01 | Accurately model Singapore-specific financial scenarios | Calculations match government sources (CPF, IRAS, HDB) |
| G-02 | Help advisors build comprehensive client financial profiles | Advisors create 5+ profiles per month |
| G-03 | Reduce financial planning preparation time | 50% faster than manual spreadsheet-based planning |
| G-04 | Provide AI-assisted planning conversations | 80% of AI chatbot responses rated helpful |
| G-05 | Maintain zero critical bugs in financial calculations | Bug fix waves resolve all P0 issues within 48 hours |

## 3. User Roles

| Role | Description |
|------|------------|
| Financial Advisor | Creates client profiles, runs projections, uses AI chatbot |
| Client (view-only) | Views shared financial plans and projections |
| Admin | Manages product data, tax brackets, CPF rates |

## 4. User Stories

| ID | Story | Acceptance Criteria |
|----|-------|-------------------|
| US-01 | As an advisor, I want to create a client financial profile so I can track their net worth | Profile captures income, assets, liabilities, insurance, CPF balances |
| US-02 | As an advisor, I want to project CPF balances so I can advise on retirement readiness | CPF OA/SA/MA projections match CPF Board formulas for given contribution rates |
| US-03 | As an advisor, I want to calculate IRAS tax liability so I can recommend SRS contributions | Tax calculation matches IRAS brackets for the current assessment year |
| US-04 | As an advisor, I want to model HDB purchase scenarios so I can advise on property decisions | HDB model includes loan eligibility, grant qualification, and CPF usage limits |
| US-05 | As an advisor, I want to chat with the AI assistant about a client's plan so I can explore options | Chatbot responds with context-aware suggestions referencing the client's profile data |

## 5. Functional Requirements

| ID | Requirement |
|----|------------|
| FR-01 | Client financial profile management (create, edit, archive) |
| FR-02 | Net worth tracking with asset and liability categories |
| FR-03 | CPF projection engine (OA, SA, MA, RA) with contribution and interest calculations |
| FR-04 | HDB planning: BTO eligibility, resale analysis, loan-to-value, grants |
| FR-05 | MediShield Life and Integrated Shield plan comparison |
| FR-06 | SRS contribution optimizer with tax savings projection |
| FR-07 | IRAS tax bracket calculator (resident and non-resident) |
| FR-08 | Insurance planning with AIA product integration |
| FR-09 | Retirement, property, and education goal planners |
| FR-10 | AI chatbot (Gemini 2.5 Pro) with client context awareness |
| FR-11 | Supabase Edge Functions for server-side calculations |
| FR-12 | Playwright E2E test suite for critical calculation paths |

## 6. Non-Goals

- Policy application or e-submission (out of scope)
- CRM or lead management (handled by lead-scraper)
- Activity tracking or gamification (handled by Activity Tracker)

## 7. Technical Considerations

| Aspect | Detail |
|--------|--------|
| Stack | React + TypeScript + Vite + Tailwind + shadcn/ui |
| Backend | Supabase (Postgres, Auth, Edge Functions) |
| AI | Gemini 2.5 Pro via API |
| Testing | Playwright E2E |
| Development | Wave-based bug fix cycles |
| Deployment | Vercel |

## 8. Success Metrics

| Metric | Target |
|--------|--------|
| Financial profiles created per advisor per month | 5+ |
| Calculation accuracy vs. government sources | 100% for CPF, IRAS, HDB |
| AI chatbot satisfaction | 80% helpful rating |
| E2E test pass rate | 95%+ |
| P0 bug resolution time | Under 48 hours |

## 9. Current Status

| Feature | Status |
|---------|--------|
| Client financial profiles | Shipped |
| Net worth tracking | Shipped |
| CPF projections | Shipped |
| HDB planning | Shipped |
| MediShield / Shield plans | Shipped |
| SRS optimizer | Shipped |
| IRAS tax calculator | Shipped |
| Insurance planning (AIA) | Shipped |
| Goal planners (retirement, property, education) | Shipped |
| AI chatbot (Gemini 2.5 Pro) | Shipped |
| Playwright E2E tests | Shipped |

## 10. Open Questions

1. How frequently should CPF rates and IRAS tax brackets be updated in the system?
2. What is the data retention policy for client financial profiles?
3. Should the AI chatbot support multi-turn planning sessions with memory?
4. How will AIA product data be kept in sync with actual product offerings?
5. Is there a plan to support non-AIA insurance products?

### Contributors

| Contributor | Commits |
|------------|---------|
| lovable-dev[bot] | 4,275 |
| jiliangarette | 162 |
| leotansingapore | 7 |
| chixka000 | 4 |
