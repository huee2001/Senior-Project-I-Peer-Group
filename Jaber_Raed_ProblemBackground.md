# Candidate Problem Background

Student: Raed Jaber  
Course: Senior Project I  
Candidate Problem: Reliability of Background Job Processing in Distributed Web Applications

## 1. Problem Description

Modern web applications often need to perform work that should not happen directly while a user is waiting for a web request to finish. Examples include sending emails, processing uploaded files, creating reports, sending notifications, processing large amounts of data, and running long-running computations. A common approach is to place this work into a queue and have separate workers process the jobs in the background.

This creates a distributed-systems problem because the application, queue, data store, and workers may be running as separate processes or even on different machines. Communication takes place over a network, and each component can fail independently.

The candidate problem I want to investigate is the reliability of background jobs when these failures occur. For example, a worker may crash while processing a job, lose its connection to the queue, or become unable to finish the job. A system then has to decide whether the job should be retried. Retrying can improve reliability, but it can also cause the same job to execute more than once.

This matters because some operations should not be repeated. Sending the same notification twice might only be annoying, but repeating a payment operation or modifying the same data multiple times could create more serious problems.

At this point, I am not assuming that I need to build a new distributed job queue. My goal is first to understand how existing systems handle worker failures, retries, duplicate processing, and recovery.

## 2. Evidence of the Problem

There is documented evidence that duplicate execution and worker failures are real concerns in existing distributed queue systems.

Amazon Simple Queue Service (SQS) uses an at-least-once delivery model for its standard queues. AWS explains that messages are stored redundantly across multiple servers. In some situations, a copy of a message may not be deleted successfully and can later be delivered again. Because of this behavior, AWS recommends designing applications to be idempotent so that processing the same message more than once does not create an incorrect result.

This is a **documented** limitation because it is described directly in Amazon's official SQS documentation.

BullMQ, a Redis-based job queue for Node.js applications, also documents situations where jobs may be processed more than once. BullMQ workers place locks on active jobs and periodically renew those locks. If a worker crashes or fails to renew the lock, the job can be considered stalled and returned to the waiting queue so that another worker can process it. This helps recover unfinished work, but it also creates the possibility that a job could be processed again.

This is also **documented** evidence from the project's official documentation.

The Celery distributed task queue describes a similar issue. Its documentation explains that messages may be redelivered to another worker when a worker fails, and it recommends that tasks be written so they can safely be executed multiple times.

These examples show that recovering jobs after failures while also preventing unwanted duplicate work is a real reliability concern in distributed job processing.

## 3. Existing Solutions

| Approach | How It Addresses the Problem | Strengths | Limitations / Questions |
|---|---|---|---|
| BullMQ with Redis | Stores jobs in Redis and uses workers, job locks, retries, and stalled-job recovery | Supports retries, concurrency, delayed jobs, worker recovery, and horizontal scaling | Requires Redis infrastructure. A stalled job may be processed again, so applications still need to consider duplicate execution |
| Amazon SQS | Provides a managed distributed message queue with message replication, visibility timeouts, and message redelivery | Managed by AWS, highly available, scalable, and does not require running the queue infrastructure directly | Standard queues use at-least-once delivery, so applications must be prepared for duplicate messages |
| Celery | Uses task queues and workers with message acknowledgements and configurable retry behavior | Mature distributed task-processing framework with support for multiple brokers and worker processes | Applications must carefully choose acknowledgement and retry behavior, and tasks may need to be idempotent |

These systems already provide many solutions to the problem. Therefore, the purpose of my project investigation is not to show that these systems are bad. Instead, I want to determine which reliability problems remain the responsibility of the application developer and whether there is a smaller area that could reasonably be improved or simplified.

## 4. Relationship to My Senior Project

### Project Option

This candidate currently appears closest to **Option 1: Build or Improve a Distributed Systems Tool**.

Distributed job queues are a common component of distributed software systems. The course specifically allows projects involving distributed job queues, communication between services, reliability, fault tolerance, failure recovery, and similar areas.

I am not yet proposing to replace BullMQ, SQS, Celery, or another existing system. The first step is to study their approaches and identify a specific limitation that could become a realistic Senior Project.

### Type of Design

The project currently appears most likely to involve **adaptive design or redesign**.

The first assigned reading describes adaptive design as taking an existing engineering solution and applying or modifying it for another need. Redesign focuses on improving an existing design while keeping its general purpose.

Since distributed job queues already exist, it would probably not be reasonable for me to assume that I need a completely original queue system. My project may eventually involve improving or adapting one particular part of an existing approach.

### Distributed-Systems Relevance

Distributed computing is important to this problem because job processing can involve multiple independent services and workers communicating through a network.

Relevant distributed-systems concerns include:

- Multiple services or machines
- Network communication
- Concurrent workers
- Coordination
- Component failure
- Failure recovery
- Reliability
- Shared job state
- Scalability
- Duplicate processing

## 5. Important Unanswered Questions

| Question | How I Might Investigate It |
|---|---|
| Under exactly what conditions can a job be executed more than once? | Compare the official documentation of BullMQ, SQS, and Celery and later create controlled worker-failure experiments |
| What responsibilities are left to application developers even when using an existing queue? | Review official documentation, examples, issue discussions, and research on idempotent distributed tasks |
| Is there a smaller reliability problem that could realistically be improved in a two-semester individual project? | Compare existing systems and identify one narrow limitation involving retries, failure recovery, duplicate detection, or observability |

## 6. Early Project Risk

One major early risk is **project scope**.

A complete distributed job-processing system can involve networking, durable storage, worker coordination, concurrency, retries, failure detection, scheduling, monitoring, and scalability. Attempting to build a complete replacement for systems such as BullMQ, Celery, or SQS would probably be too large for one student to design and implement within two semesters.

Because of this, the project will likely need to focus on one clearly defined reliability issue rather than attempting to solve every problem related to distributed job processing.

## 7. Connection to the Assigned Readings

### Reading 1 — Types of Engineering Design

One useful idea from this reading was the difference between original design, adaptive design, redesign, and selection design. This changed how I think about the project because I do not need to invent a completely new distributed queue for the project to be meaningful. An improvement or adaptation of an existing approach could still represent a valid engineering project.

### Reading 2 — Research and Analysis of Existing Solutions

The main idea I took from this reading is that existing solutions should be researched before beginning the actual design. The reading explains that designers should study current solutions, their advantages, disadvantages, and possible improvements before deciding whether something must be designed from scratch.

For my candidate problem, this means I need to understand existing systems such as BullMQ, Amazon SQS, and Celery before claiming that a new solution is necessary.

### Reading 3 — Communications in Engineering Capstone Projects

One important idea from this reading is that an engineer should verify the real need before developing a solution. A misunderstood problem can result in creating a system that does not actually solve the user's need.

For my project, I should not simply assume that existing distributed queues are unreliable or difficult to use. I need to identify specific documented limitations and determine whether those limitations are important enough to justify a project.

## References

Amazon Web Services. (n.d.). *Amazon SQS at-least-once delivery*. Amazon Simple Queue Service Developer Guide.

Amazon Web Services. (n.d.). *Amazon SQS visibility timeout*. Amazon Simple Queue Service Developer Guide.

BullMQ. (n.d.). *What is BullMQ*. BullMQ Documentation.

BullMQ. (n.d.). *Stalled jobs*. BullMQ Documentation.

Celery Project. (n.d.). *Tasks*. Celery Documentation.

Morozov, A., et al. *Engineering Capstone Design: Project Planning, Organizing, and Executing*. Assigned course readings: Types of Engineering Design; Research and Analysis of Existing Solutions; Communications in Engineering Capstone Projects.
