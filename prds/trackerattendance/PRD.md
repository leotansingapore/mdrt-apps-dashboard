# PRD: Tracker Attendance

Version: 1.0 | Date: 2026-04-08 | Status: Active | Owner: Leo Tan

## 1. Introduction

Tracker Attendance is a training event attendance tracking and check-in system for the advisory team. It enables organizers to create training events, generate check-in mechanisms (QR codes or links), track real-time attendance, and report on participation rates for compliance and development tracking.

## 2. Goals

| ID | Goal | Success Metric |
|----|------|---------------|
| G-01 | Replace manual attendance sheets with digital check-in | 100% of training events use digital check-in |
| G-02 | Provide real-time attendance visibility to organizers | Attendance count updates within 5 seconds of check-in |
| G-03 | Generate attendance reports for compliance | Reports exportable within 1 minute of event end |

## 3. User Roles

| Role | Description |
|------|------------|
| Attendee | Checks in to training events via QR code or link |
| Organizer | Creates events, monitors attendance, generates reports |
| Admin | Manages event categories, compliance rules, user access |

## 4. User Stories

| ID | Story | Acceptance Criteria |
|----|-------|-------------------|
| US-01 | As an organizer, I want to create a training event so attendees can check in | Event created with title, date, time, location; unique check-in link/QR generated |
| US-02 | As an attendee, I want to check in via QR code so my attendance is recorded instantly | Scan QR or tap link; confirmation shown; name appears on organizer's live list |
| US-03 | As an organizer, I want to see real-time attendance so I know who has arrived | Live attendance dashboard with count, names, and check-in timestamps |
| US-04 | As an organizer, I want to export an attendance report so I can submit it for compliance | Export to CSV/PDF with event details, attendee names, and timestamps |

## 5. Functional Requirements

| ID | Requirement |
|----|------------|
| FR-01 | Event creation with date, time, location, and description |
| FR-02 | QR code and shareable link generation per event |
| FR-03 | Digital check-in with timestamp recording |
| FR-04 | Real-time attendance dashboard for organizers |
| FR-05 | Attendance report export (CSV, PDF) |
| FR-06 | Historical attendance records per person and per event |

## 6. Non-Goals

- Training content delivery or LMS functionality
- Activity tracking or gamification (handled by Activity Tracker)
- Scheduling or calendar management (handled by Quick Schedule Pal)

## 7. Technical Considerations

| Aspect | Detail |
|--------|--------|
| Stack | React + TypeScript + Vite + Tailwind + shadcn/ui |
| Backend | Supabase |
| QR Generation | Client-side QR library |
| Deployment | Vercel |

## 8. Success Metrics

| Metric | Target |
|--------|--------|
| Digital check-in adoption | 100% of events |
| Check-in to confirmation time | Under 5 seconds |
| Report generation time | Under 1 minute |
| Attendance data accuracy | 99%+ |

## 9. Current Status

| Feature | Status |
|---------|--------|
| Event creation | MVP |
| QR code check-in | MVP |
| Live attendance dashboard | MVP |
| Report export | Planned |
| Historical records | Planned |

## 10. Open Questions

1. Should attendance data integrate with Activity Tracker for CPD (Continuing Professional Development) credits?
2. Is there a need for late check-in or absence justification workflows?
3. How will attendance data be used for compliance reporting to AIA or MAS?
