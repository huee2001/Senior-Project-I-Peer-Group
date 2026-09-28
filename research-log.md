# Senior Project Research and Design Log

Raed Jaber

## Week 1

### Candidate Problem

Reliable processing of background jobs in distributed web applications.

### Initial Idea

Modern web applications often perform work outside the main web request,
such as sending notifications, processing files, calling AI services,
or running scheduled tasks.

When these tasks are performed by separate workers or services,
failures may cause jobs to be lost, duplicated, delayed, or retried
incorrectly.

I want to investigate how existing distributed job queue systems handle
these problems and whether there is an area that could be simplified or
improved.

### Questions

- How do existing job queue systems prevent lost jobs?
- How are failed jobs retried?
- How do systems prevent a job from running twice?
- What happens if a worker crashes while processing a job?
- How much infrastructure is required to operate existing systems?

### Existing Solutions to Research

- BullMQ / Redis
- Amazon SQS
- Possibly Celery

### Current Assumptions

- Background job reliability is important for web applications.
- Existing distributed queue systems already solve many parts of this problem.
- There may still be opportunities involving ease of use, failure recovery,
  observability, or deployment complexity.

These are currently assumptions and must be verified with sources.

### Early Risks

The problem may already be well solved by existing systems.

Another risk is making the project too large for one student.

### Current Decision

Continue investigating the problem before deciding on a final system
or technology.
