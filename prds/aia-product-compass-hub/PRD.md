# PRD: AIA Product Compass Hub

Version: 1.0 | Date: 2026-04-08 | Status: Active | Owner: Leo Tan

## 1. Introduction

AIA Product Compass Hub is a product reference, comparison, and recommendation tool for AIA insurance and investment products. It helps financial advisors quickly find the right product for a client's needs, compare plan features side-by-side, and generate recommendation rationales.

## 2. Goals

| ID | Goal | Success Metric |
|----|------|---------------|
| G-01 | Provide instant access to AIA product details | Advisor finds product info in under 30 seconds |
| G-02 | Enable side-by-side product comparison | Advisors use comparison in 40%+ of client meetings |
| G-03 | Improve recommendation accuracy | Product-client fit score above 80% |

## 3. User Roles

| Role | Description |
|------|------------|
| Advisor | Searches products, runs comparisons, generates recommendations |
| Admin | Maintains product catalog, updates features and pricing |

## 4. User Stories

| ID | Story | Acceptance Criteria |
|----|-------|-------------------|
| US-01 | As an advisor, I want to search for AIA products by category so I can quickly find relevant options | Search returns filtered results by category (life, health, investment, etc.) |
| US-02 | As an advisor, I want to compare two or more products side-by-side so I can explain differences to clients | Comparison table highlights key differences in features, premiums, and coverage |
| US-03 | As an advisor, I want to get a product recommendation based on client needs so I can present the best fit | Recommendation engine accepts client profile and returns ranked products with rationale |
| US-04 | As an admin, I want to update product details so the catalog stays current | Product editor with version history and publish/draft states |

## 5. Functional Requirements

| ID | Requirement |
|----|------------|
| FR-01 | AIA product catalog with search and filtering |
| FR-02 | Side-by-side product comparison (up to 3 products) |
| FR-03 | Needs-based product recommendation engine |
| FR-04 | Product detail pages with features, benefits, premiums, exclusions |
| FR-05 | Admin product catalog management |
| FR-06 | Shareable comparison/recommendation output |

## 6. Non-Goals

- Policy application or e-submission
- Financial planning or projections (handled by BeeHive Finance Hub)
- Non-AIA product coverage

## 7. Technical Considerations

| Aspect | Detail |
|--------|--------|
| Stack | React + TypeScript + Vite + Tailwind + shadcn/ui |
| Backend | Supabase |
| Deployment | Vercel |

## 8. Success Metrics

| Metric | Target |
|--------|--------|
| Product lookup time | Under 30 seconds |
| Comparison usage in meetings | 40%+ |
| Product catalog currency | Updated within 7 days of AIA changes |

## 9. Current Status

| Feature | Status |
|---------|--------|
| Product catalog | MVP |
| Search and filtering | MVP |
| Product comparison | MVP |
| Recommendation engine | Planned |
| Admin management | Planned |

## 10. Open Questions

1. How will AIA product data be sourced and kept up-to-date?
2. Should the recommendation engine use AI or rule-based logic?
3. Is there a compliance review requirement before recommendations are shown?
