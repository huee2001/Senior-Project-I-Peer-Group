**Author:** Ibsan Hossain 

**Course:** CSC 59866 

**Selected project and option:** B2 - Reliable Data Exchange for Integrated Justice Records; generalized as a data-migration system 

**Current assignment:** 1 

**Friday commit deadline:** November 6, 2026 **Monday presentation:** November 9, 2026 **Last updated:** November 6, 2026 

**Document status:** Proposed 

# **Progress note** 

For Assignment 1, I focused on defining the data-migration problem and setting a clear boundary for the project. I used my Problem Understanding Paper, the LA County migration opportunity, and the course handbook to explain the current migration process and the difficulties caused by different schemas, large amounts of data, and source records that may change during migration. I also added a stakeholder table and workflow image to make the problem easier to follow. Some parts of the scenario are still assumptions because I have not collected my own migration data or performance results. The main issue I still need to investigate is how migration work should be divided across multiple workers. After receiving feedback on this first draft, I will revise the scope if needed and begin the requirements work for Assignment 2. 

# **Contents** 

- <u>1 Problem research and scope</u> 

- <u>2 Requirements and system specification</u> 

- <u>3 Alternatives and selected solution</u> 

- <u>4 Architectural design</u> 

- <u>5 Component design and interfaces</u> 

- <u>6 Data structure design</u> 

- <u>7 Algorithm design and execution</u> 

- <u>8 Failures and security</u> 

- <u>9 Implementation and feasibility</u> 

- <u>10 Testing and verification</u> 

- <u>11 Operation maintenance and future work</u> 

- <u>12 Revision history and references</u> 

# **1 Problem research and scope** 

## **Problem and affected people:** 

The problem I am investigating is how to move a large amount of structured data from an older system into a replacement system quickly and correctly when the two systems may organize their data differently and the original data may continue changing during the migration. The people most directly affected are employees responsible for migration work, database administrators, developers, and data engineers. Organizations are also affected because the migrated records may support important daily operations, reporting, auditing, and other business functions. 

The Los Angeles County Sheriff’s Department Integrated Justice Information System opportunity provides a real example. The County plans to replace older jail-management systems while preserving historical and active records. Its statement of work requires data mappings, transformation logic, conversion routines, an initial full upload, incremental catch-up migrations, validation, reconciliation, and an audit trail. 

<u>Los Angeles County Sheriff’s Department — Integrated Justice Information System, Exhibit A: Statement of Work</u> 

|**Stakeholder**|**Current task**|**Main need**|
|---|---|---|
|Migration employee or operator|Move structured records from an<br>old system to a replacement<br>system|A clear and controlled migration<br>process|
|Database administrator|Check and protect destination data|<sup>Correct and complete migrated</sup><br>records|
|Developer or data engineer|Define mappings, transformations,<br>andmigration logic|A process that is understandable<br>andrepeatable|
|Organization replacing a system|Move to the new system without<br>losing important information|Accurate data and less repeated<br>migration work|



# **Current workflow:** 

A representative migration begins by exporting structured data from the old system. A migration employee or developer inspects the source fields and determines how they correspond to the fields expected by the new system. Required transformations are defined, the data is processed and loaded into the destination, and the migrated records are checked. If records are incorrect or the original data changes before the final cutover, some migration work may need to be repeated. 

The difficulty occurs when the old and new schemas do not match directly, when the amount of data is large enough that processing becomes slow, or when source records change after part of the migration has already been completed. 

# **Concrete scenario:** 

**Illustrative scenario, not an observed incident:** Suppose an organization needs to migrate five million employee records. The old file contains employee_number, full_name, and hire_date, while the new system expects employee_id, first_name, last_name, and start_date. The migration worker must decide how these fields correspond and how a combined name field should be converted into separate fields. 

Normally, the mapping is correct, the records are processed, and the destination receives the expected data. The problem appears if a field is mapped incorrectly, a very large dataset takes too long to process through one path, or source records change after they have already been migrated. The destination may then contain incorrect or outdated information, causing the technical team to repeat part of the migration. 

# **Evidence:** 

**Documented evidence:** The LA County statement of work requires an initial full data upload, multiple incremental catch-up migrations, record- and field-level validation, reconciliation evidence, mappings, transformation logic, and an audit trail. This supports the claim that real migration work involves schema differences, validation, and later updates rather than only copying data once. 

Apache Spark is an existing distributed data-processing approach that helps me understand the part of the problem involving large workloads. Its documentation describes a driver that coordinates executor processes and divides a larger job into tasks that can be processed in parallel. I am not claiming that my project will reproduce Spark. It is an existing approach that shows how large processing work can be divided among multiple workers. 

<u>Apache Spark — Cluster Mode Overview</u> 

# **Assumptions:** 

The concrete five-million-record employee example is an illustrative scenario rather than a measured case from LA County. I am assuming that the first planned version of the project can focus on structured file input, beginning with CSV, and a known destination schema. I am also assuming that synthetic data will be sufficient for design and later testing, so no real LA County records are required. Another assumption is that the project can be designed around multiple workers even if development and later testing use processes or services on one physical computer. These assumptions will be refined as the later design assignments define requirements, architecture, and evaluation. 

# **Six-week contribution:** 

During this six-week design period, I will investigate and define the bounded core migration capability that the Semester II system will later implement. The focus is the path from a structured source file to a mapped destination schema, followed by dividing a large migration into smaller units of work that can be assigned to multiple workers and eventually loaded into a destination database. This semester's contribution is to make that capability precise enough to guide implementation by documenting the problem, requirements, possible approaches, architecture, data and algorithm behavior, failure conditions, and the planned way to judge correctness and performance. 

The bounded question is not whether I can recreate every feature of an enterprise migration platform. It is how a general-purpose migration tool should combine schema mapping with distributed work division while keeping the destination data correct. 

# **Semester II scope:** 

The larger Semester II goal is to implement the working web-based data-migration product described in the Problem Understanding Paper. A user will be able to provide structured source data, map source fields to a destination schema, start the migration, and have the workload divided among multiple workers before the transformed records are loaded into PostgreSQL. The completed project is also intended to include migration monitoring and file-based change detection so that later source versions can identify new or changed records without repeating all unchanged work. 

CSV will be the initial structured input format. The design should keep input parsing separate enough that another structured format, such as JSON, can be added later without redesigning the entire migration process. 

# **Exclusions:** 

- Real LA County records and development of the complete LA County justice system. 

- Support for every possible database, file type, or transformation language. 

- Enterprise authentication and production cloud deployment. 

- Multi-datacenter operation or claims that a classroom design represents production-scale fault tolerance. 

- A full transaction-log Change Data Capture platform such as Debezium. 

- Completing the full Semester II implementation as part of Assignment 1. 



<!-- Start of picture text -->
Current Data-Migration° .  Workflow<br>Old System |-»| Migration Worker |p| Processing Step |-»| NewDatabase |-»| Validation<br>Structured records Inspects fields and Transforms and Receives the Checks migrated<br>are exported defines mappings processes records transformed records records and handles<br>(e.g., CSV). (source > target). (e.g., split, rename, (e.g., PostgreSQL). updates (e.g.,<br>format). incremental).<br><!-- End of picture text -->

**2 Requirements and system specification Work to come  - Assignment 2.** 

**3 Alternatives and selected solution** 

**Work to come  - Assignments 2 and 3.** 

**4 Architectural design Work to come - Assignment 3.** 

**5 Component design and interfaces Work to come - Assignment 3.** 

**6 Data structure design** 

**Work to come - Assignment 4.** 

**7 Algorithm design and execution** 

**Work to come - Assignment 4.** 

**8 Failures and security** 

**Work to come - Assignment 4.** 

**9 Implementation and feasibility** 

**Work to come - later assignments.** 

**10 Testing and verification** 

**Work to come - later assignments.** 

**11 Operation maintenance and future work** 

**Work to come - later assignments.** 

**12 Revision history and references** 

|**Revision date**|**Change to my design**|**Reason and evidence**|
|---|---|---|
|November 6, 2026|Created the initial Assignment 1<br>design document for B2 with the<br>affected people, current workflow,<br>concrete scenario, evidence,<br>assumptions, bounded<br>contribution, Semester II goal,<br>exclusions, table, image, and<br>sources.|Assignment 1 requires the<br>problem and project boundary to<br>be understandable before later<br>requirements and design work<br>begins.|
|**Open question**|**Why it matters**|**Next action**|
|How should a large migration be<br>divided among multiple workers<br>without adding too much<br>coordination overhead or<br>producing incorrect destination<br>data?|Work division is central to the<br>distributed part of B2 and will<br>affect both performance and<br>correctness in the completed<br>project.|Research and compare possible<br>work-division approaches during<br>the later requirements and<br>alternatives assignments before<br>selecting a design.|



## **Assistance and reuse:** 

This document is based on my B2 Problem Understanding Paper, the course provided design template, and the Software Project Design Handbook. No implementation results or performance measurements are claimed in this Assignment 1 draft. 

## **References** 

1. Los Angeles County Sheriff’s Department. Integrated Justice Information System - Exhibit A: Statement of Work, RFP 712-SH. Supports the problem evidence concerning mappings, transformation, full and incremental migration, validation, reconciliation, and auditing. 

<u>https://lasd.org/wp-content/uploads/2026/10/Solicitations_RFP712-SH_4_ExhA_100126.pdf</u> 

2. Apache Spark. Cluster Mode Overview. Provides an existing distributed-processing approach for understanding how larger jobs can be divided into tasks and coordinated across executor processes. 

<u>https://spark.apache.org/docs/latest/cluster-overview.html</u> 

3. CSC 59866 course materials. Software Project Design Handbook and Design Document Template, Fall 2026. Used for the Assignment 1 structure, scope, Markdown requirements, and weekly design process. 

