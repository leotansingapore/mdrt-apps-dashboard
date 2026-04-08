# PRD: Quick Schedule Pal

Version: 1.1 | Date: 2026-04-08 | Status: Active | Owner: Leo Tan

## 1. Introduction

Quick Schedule Pal is a coaching session booking tool with Google Calendar integration for financial advisors. It uses Lovable Cloud OAuth authentication and includes a self-improving AI system (swarm pipeline with 15-minute improvement cycles) to optimize scheduling. The app tracks client availability and streamlines the booking process.

## 2. Goals

| ID | Goal | Success Metric |
|----|------|---------------|
| G-01 | Reduce scheduling back-and-forth via Google Calendar sync | Average booking takes under 2 minutes |
| G-02 | Increase coaching session volume | 20% more sessions booked per advisor per month |
| G-03 | Prevent double-booking through calendar integration | Zero scheduling conflicts reported |
| G-04 | Continuously improve scheduling UX via AI swarm pipeline | Measurable UX improvement every 15-minute cycle |

## 3. User Roles

| Role | Description |
|------|------------|
| Coach/Advisor | Sets availability, shares booking links, manages coaching sessions |
| Client/Coachee | Books available coaching time slots via shared link |

## 4. Core Features

| Feature | Description |
|---------|------------|
| Google Calendar Integration | Two-way sync for availability and bookings |
| Lovable Cloud OAuth | Authentication via Lovable Cloud |
| Self-Improving AI System | Swarm pipeline on 15-minute cycles that optimizes scheduling logic |
| Client Availability Tracking | Track when clients are available for coaching sessions |
| Booking Links | Shareable links for self-service session booking |
| Session Management | Calendar views with appointment details and client info |

## 5. Technical Architecture

| Aspect | Detail |
|--------|--------|
| Stack | React + TypeScript + Vite + Tailwind + shadcn/ui |
| Backend | Supabase |
| Calendar | Google Calendar API integration |
| Auth | Lovable Cloud OAuth |
| AI | Self-improving swarm pipeline (15-min cycle) |
| Deployment | Vercel |

## 6. Contributors

| Contributor | Commits | Role |
|------------|---------|------|
| `lovable-dev[bot]` | ~89 | Primary AI builder |
| `leotansingapore` | 7 | Owner, product direction |
| `claude` | 7 | AI contributor |
| `jiliangarette` | 6 | Developer |
| Total | 109 | |

## 7. Non-Goals

- CRM or lead management
- Video conferencing integration
- Payment collection for consultations
- Full team-wide scheduling (this is for 1:1 coaching sessions)

## 8. Success Metrics

| Metric | Target |
|--------|--------|
| Average booking time | Under 2 minutes |
| Scheduling conflicts | Zero |
| Coach adoption | 80% of team |
| AI improvement cycle uptime | 95%+ |

## 9. Current Status

| Feature | Status |
|---------|--------|
| Google Calendar integration | Production |
| Lovable Cloud OAuth | Production |
| Booking links | Production |
| Client availability tracking | Production |
| Self-improving AI system | MVP |
| Session management | Production |

## 10. Open Questions

1. Should the self-improving AI system be expanded to other ecosystem apps?
2. How will coaching session data feed into Activity Tracker for advisor development tracking?
3. Is there a need for group session booking in addition to 1:1?
