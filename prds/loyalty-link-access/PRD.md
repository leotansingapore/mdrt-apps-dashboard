# PRD: Loyalty Link Access

Version: 1.0 | Date: 2026-04-08 | Status: Active | Owner: Leo Tan

## 1. Introduction

Loyalty Link Access is a personality assessment platform with over 754 commits. It delivers DISC behavioral assessments and Enneagram personality typing with compatibility analysis, PDF report generation, leadership profiling, and team building tools. Built entirely by Lovable Bot.

## 2. Goals

| ID | Goal | Success Metric |
|----|------|---------------|
| G-01 | Provide accurate DISC and Enneagram assessments | Assessment results consistent on retest within 2 weeks |
| G-02 | Generate professional PDF reports for clients and team members | PDF reports generated in under 10 seconds |
| G-03 | Enable team compatibility analysis | Leaders use compatibility insights in team formation decisions |
| G-04 | Support leadership development with personality-based profiling | 80% of leaders complete their profile |

## 3. User Roles

| Role | Description |
|------|------------|
| Assessment Taker | Completes DISC and/or Enneagram assessments |
| Coach / Leader | Views team results, compatibility matrices, leadership profiles |
| Admin | Manages assessment configurations and report templates |

## 4. User Stories

| ID | Story | Acceptance Criteria |
|----|-------|-------------------|
| US-01 | As an assessment taker, I want to complete a DISC assessment so I understand my behavioral style | Questionnaire completes in under 10 minutes; results shown immediately |
| US-02 | As an assessment taker, I want to complete an Enneagram assessment so I understand my personality type | Type and wing identified with description; results stored for later access |
| US-03 | As a coach, I want to view compatibility between two team members so I can pair them effectively | Compatibility matrix shows strengths, friction points, and communication tips |
| US-04 | As a leader, I want to download a PDF report of my assessment results so I can share them | PDF includes profile summary, strengths, growth areas, and team tips |
| US-05 | As a leader, I want to see my leadership profile based on DISC and Enneagram so I can develop my style | Leadership profile maps personality traits to leadership competencies |

## 5. Functional Requirements

| ID | Requirement |
|----|------------|
| FR-01 | DISC behavioral assessment with validated questionnaire |
| FR-02 | Enneagram personality typing with wing identification |
| FR-03 | Compatibility analysis between any two profiles |
| FR-04 | PDF report generation via jsPDF/html2pdf |
| FR-05 | Leadership profiling based on assessment results |
| FR-06 | Team building tools: group compatibility view, suggested pairings |
| FR-07 | Result storage and historical comparison |

## 6. Non-Goals

- Activity tracking or gamification (handled by Activity Tracker)
- Performance metrics or EPS (handled by Agent Rank Dash)
- Financial planning (handled by BeeHive Finance Hub)

## 7. Technical Considerations

| Aspect | Detail |
|--------|--------|
| Stack | React + TypeScript + Vite + Tailwind + shadcn/ui |
| PDF Generation | jsPDF, html2pdf |
| Backend | Supabase |
| Builder | 100% Lovable Bot |
| Deployment | Vercel |

## 8. Success Metrics

| Metric | Target |
|--------|--------|
| Assessment completion rate | 90% of team members |
| PDF report generation time | Under 10 seconds |
| Retest consistency | 85%+ same primary type within 2 weeks |
| Compatibility tool usage by leaders | Monthly |

## 9. Current Status

| Feature | Status |
|---------|--------|
| DISC assessment | Shipped |
| Enneagram assessment | Shipped |
| Compatibility analysis | Shipped |
| PDF report generation | Shipped |
| Leadership profiling | Shipped |
| Team building tools | Shipped |

## 10. Open Questions

1. Should DISC results feed into the Activity Tracker's coaching module automatically?
2. How will assessment validity be maintained as the questionnaire evolves?
3. Is there demand for additional assessment types (e.g., StrengthsFinder, MBTI)?
4. What is the privacy policy for storing personality data?
5. Should reports be white-labeled for client-facing use?
