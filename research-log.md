# Senior Project Research and Design Log

Raed Jaber  
Senior Project I

---

## Week 1

### Candidate Problem

Reliability of background job processing in distributed web applications.

### Initial Problem

Web applications commonly use background workers for work that should not
happen during the user's main request.

When jobs are distributed between different workers or services, failures can
create problems involving retries, duplicate processing, unfinished jobs, and
recovery.

I want to investigate how existing distributed job-processing systems handle
these situations.

### Why I Am Considering This Problem

The problem fits the distributed-systems focus of the course because it
involves:

- multiple workers or services
- communication over a network
- concurrent processing
- failure recovery
- shared job state
- reliability
- coordination
- scalability

### Existing Systems Identified

#### BullMQ

BullMQ is a Redis-based job queue for Node.js applications.

Important areas to investigate:

- retries
- worker crashes
- stalled jobs
- locks
- duplicate processing
- Redis dependency

#### Amazon SQS

Amazon SQS is a managed message-queue service.

Important areas to investigate:

- at-least-once delivery
- visibility timeout
- message redelivery
- duplicate processing
- idempotency

#### Celery

Celery is a distributed task queue commonly used with Python.

Important areas to investigate:

- acknowledgements
- worker failure
- message redelivery
- retries
- idempotent tasks

### Evidence Found

**Documented:** Amazon SQS Standard queues use at-least-once delivery, meaning
a message can sometimes be delivered more than once.

**Documented:** BullMQ detects jobs that stop renewing their worker locks as
stalled. These jobs can be returned to the waiting queue and processed again.

**Documented:** Celery can redeliver tasks after certain worker failures and
recommends designing tasks so repeated execution does not cause unwanted
effects.

### Current Hypotheses

The following are hypotheses and have not yet been proven:

1. Developers of smaller applications may find reliable distributed job
   processing unnecessarily complicated.

2. Detecting or preventing unwanted duplicate job execution may be an area
   worth investigating.

3. Existing queue systems may provide reliable message delivery while leaving
   important reliability responsibilities to the application developer.

These need further research before they can become project claims.

### Current Project Classification

**Course option:** Option 1 — Distributed Systems Tool

**Possible design type:** Adaptive design and/or redesign

I currently do not believe that creating an entirely new queue system would
be the best direction. Existing systems already solve much of the problem.

### Questions for Further Research

1. What exactly happens when a worker crashes halfway through a job?
2. When can the same job execute twice?
3. How do applications safely handle duplicate execution?
4. What guarantees do existing queues actually provide?
5. What reliability responsibilities remain with the application developer?
6. Is there one narrow part of this problem that could reasonably become my
   Senior Project?

### Early Risk

The largest current risk is scope.

A distributed queue can involve many separate problems, including storage,
networking, worker coordination, concurrency, retries, failure detection,
monitoring, and scalability.

The project will probably need to focus on one narrow reliability problem
instead of attempting to build a complete distributed queue.

### Week 1 Decision

Continue researching distributed background-job reliability before committing
to a final project design.

The next step is to compare existing queue systems and identify one specific
limitation that is realistic enough to investigate and eventually implement
during Senior Project II.

### Sources Investigated

- Amazon SQS official documentation
- BullMQ official documentation
- Celery official documentation
- Engineering Capstone Design course readings
