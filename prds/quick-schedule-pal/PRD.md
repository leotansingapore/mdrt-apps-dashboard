# PRD: Quick Schedule Pal

Version: 1.0 | Date: 2026-04-08 | Status: Active | Owner: Leo Tan

## 1. Introduction

Quick Schedule Pal is an appointment scheduling tool designed for financial advisors. It streamlines the process of booking client meetings, managing availability, and reducing scheduling friction -- enabling advisors to spend more time in client conversations and less on logistics.

## 2. Goals

| ID | Goal | Success Metric |
|----|------|---------------|
| G-01 | Reduce scheduling back-and-forth | Average booking takes under 2 minutes |
| G-02 | Increase client meeting volume | 20% more meetings booked per advisor per month |
| G-03 | Prevent double-booking and conflicts | Zero scheduling conflicts reported |

## 3. User Roles

| Role | Description |
|------|------------|
| Advisor | Sets availability, shares booking links, manages appointments |
| Client / Prospect | Books available time slots via shared link |
| Admin | Manages team-wide scheduling rules and defaults |

## 4. User Stories

| ID | Story | Acceptance Criteria |
|----|-------|-------------------|
| US-01 | As an advisor, I want to set my available time slots so clients can self-book | Availability editor with recurring and one-off slot support |
| US-02 | As a client, I want to book an appointment from a shared link so I can schedule without calling | Booking page shows available slots; confirmation sent on booking |
| US-03 | As an advisor, I want to see my upcoming appointments in one view so I can plan my day | Calendar view with appointment details, client info, and meeting type |

## 5. Functional Requirements

| ID | Requirement |
|----|------------|
| FR-01 | Availability management with recurring schedules |
| FR-02 | Shareable booking links per advisor |
| FR-03 | Appointment calendar with day/week/month views |
| FR-04 | Booking confirmation and reminder notifications |
| FR-05 | Buffer time and meeting duration configuration |

## 6. Non-Goals

- CRM or lead management
- Video conferencing integration
- Payment collection for consultations

## 7. Technical Considerations

| Aspect | Detail |
|--------|--------|
| Stack | React + TypeScript + Vite + Tailwind + shadcn/ui |
| Backend | Supabase |
| Deployment | Vercel |

## 8. Success Metrics

| Metric | Target |
|--------|--------|
| Average booking time | Under 2 minutes |
| Scheduling conflicts | Zero |
| Advisor adoption | 80% of team |

## 9. Current Status

| Feature | Status |
|---------|--------|
| Availability management | MVP |
| Booking links | MVP |
| Appointment calendar | MVP |
| Notifications | Planned |

## 10. Open Questions

1. Should the tool integrate with Google Calendar or Outlook?
2. Is there a need for meeting type categories (e.g., initial consultation vs. review)?
3. How will client data from bookings feed into other ecosystem apps?
