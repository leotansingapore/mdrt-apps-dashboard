# PRD: AIA Product Compass Hub (FINternship)

Version: 1.1 | Date: 2026-04-08 | Status: Active | Owner: Leo Tan

## 1. Introduction

AIA Product Compass Hub, internally known as **FINternship**, is a financial advisory training platform. It provides product education for AIA insurance and investment products, AI roleplay scenarios for advisor training, CMFAS exam study tools, progress tracking with gamification, AI-powered product guidance, and accessible chat (WCAG 2.1 AA). Deployed at aia-product-compass-hub.vercel.app.

## 2. Goals

| ID | Goal | Success Metric |
|----|------|---------------|
| G-01 | Accelerate new advisor product knowledge | Advisors pass product assessments within 30 days |
| G-02 | Provide realistic client interaction practice via AI roleplay | 80%+ of trainees complete at least 5 roleplay scenarios |
| G-03 | Improve CMFAS exam pass rates | First-attempt pass rate above 75% |
| G-04 | Track training progress with gamification | Weekly engagement above 70% of enrolled trainees |

## 3. User Roles

| Role | Description |
|------|------------|
| Trainee | Studies products, completes roleplay scenarios, prepares for CMFAS exams |
| Trainer/Admin | Creates modules, manages resources, tracks trainee progress |

## 4. Core Features

| Feature | Description |
|---------|------------|
| Product Education | AIA insurance and investment product catalog with detailed breakdowns |
| AI Roleplay Scenarios | Simulated client conversations for training, powered by Claude |
| CMFAS Exam Prep | Study tools and practice questions for regulatory exams |
| Progress Tracking | Gamified completion tracking with achievements |
| AI Product Guidance | Intelligent recommendations based on client scenarios |
| Accessible Chat | WCAG 2.1 AA compliant chat interface |
| Module Editor | Admin tool for creating and managing training modules with resources |

## 5. Technical Architecture

| Aspect | Detail |
|--------|--------|
| Stack | React + TypeScript + Vite + Tailwind + shadcn/ui |
| Backend | Supabase |
| Custom Hooks | 90+ React hooks |
| AI | Claude CLI integration for roleplay and guidance |
| Accessibility | WCAG 2.1 AA compliance |
| Deployment | Vercel (aia-product-compass-hub.vercel.app) |

## 6. Contributors

| Contributor | Commits | Role |
|------------|---------|------|
| `lovable-dev[bot]` | ~2,959 | Primary AI builder |
| `jiliangarette` | 49 | Developer -- feature work |
| `joshua0006` | 32 | Developer -- feature work |
| `leotansingapore` | 27 | Owner, product direction |
| `claude` | 18 | AI contributor |
| Total | 3,085 | |

## 7. Non-Goals

- Policy application or e-submission
- Financial planning or projections (handled by BeeHive Finance Hub)
- Non-AIA product coverage
- Live client-facing tools

## 8. Success Metrics

| Metric | Target |
|--------|--------|
| Product assessment pass rate | 90%+ within 30 days |
| CMFAS first-attempt pass rate | 75%+ |
| Roleplay scenario completion | 5+ per trainee |
| Weekly active engagement | 70%+ of enrolled |
| Accessibility audit score | WCAG 2.1 AA pass |

## 9. Current Status

| Feature | Status |
|---------|--------|
| Product education catalog | Production |
| AI roleplay scenarios | Production |
| CMFAS exam prep | Production |
| Progress tracking | Production |
| AI product guidance | Production |
| Accessible chat | Production |
| Module editor | Production |

## 10. Open Questions

1. How will training completion data feed into Agent Rank Dash for performance tracking?
2. Should the platform support non-AIA products for comparison education?
3. Is there a compliance review requirement for AI-generated roleplay content?
