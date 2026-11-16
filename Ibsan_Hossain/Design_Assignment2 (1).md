**Author:** Ibsan Hossain 

**Course:** CSC 59866 

**Selected project and option:** B2 - Reliable Data Exchange for Integrated Justice Records; generalized as a data-migration system 

**Current assignment:** 2 

**Friday commit deadline:** November 13, 2026 **Monday presentation:** November 16, 2026 **Last updated:** November 13, 2026 

**Document status:** Revised 

# **Progress note** 

For Assignment 2, I turned the problem from Assignment 1 into a set of specific requirements for the proposed data-migration system. I defined the main functions the system should provide, two correctness rules, and a proposed performance target that can be tested later. I also added an ordinary input/output example, an unsuccessful case, assumptions, and constraints. In Section 3, I compared a simple single-worker approach, a custom multi-worker approach, and Apache Spark as a distributed-processing alternative. I have not selected the final design yet because that decision belongs in Assignment 3. The main issue I still need to investigate is how migration work should be divided among workers without adding too much overhead or affecting correctness. My next step is to use the architecture and feasibility work in Assignment 3 to make that choice.
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

Based on the Assignment 2 requirements, the initial design will also assume that each source record has a usable key so that changed records can be identified across file versions.

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



# **2 Requirements and system specification**

The requirements below describe what the completed system should be able to do without deciding exactly how the system will be implemented. **F** means functional requirement, **C** means correctness requirement, and **Q** means quality requirement. The acceptance checks below are planned checks, not completed test results.

|**ID**|**Required behavior and conditions**|**Acceptance check**|**Design and test reference**|
|---|---|---|---|
|F1|The system must accept a valid CSV file with a header row and identify the source fields so they can be mapped. If the file cannot be read as the supported format, the migration should not begin.|Upload a valid CSV file and confirm that its field names are identified. Then provide an invalid file and confirm that it is rejected before the migration starts.|To be added in later assignments.|
|F2|Before a migration begins, the user must be able to map the required source fields to the fields expected by the destination system.|Using the employee example, map `employee_number` to `employee_id`, the name information to the required destination name fields, and `hire_date` to `start_date`. Confirm that the selected mapping is saved correctly.|To be added in later assignments.|
|F3|After the mapping is confirmed, the system must process the source records and produce records that follow the destination schema. It must also identify records that fail during processing.|Use a small synthetic dataset with known expected results and compare the processed destination records and failure count with the expected results.|To be added in later assignments.|
|F4|The user must be able to view the status of the migration and a final summary showing the number of total, completed, and failed records.|Run a controlled migration and confirm that the progress information changes while records are processed and that the final totals match the actual results.|To be added in later assignments.|
|F5|When a newer version of previously migrated source data is provided, the completed system should be able to identify new or changed records so unchanged records do not need to be processed again.|Use an original file and a second version containing an unchanged record, a changed record, and a new record. Confirm that only the changed and new records are selected for processing again.|To be added in later assignments.|
|C1|Every record reported as successfully migrated must match the approved field mapping and transformation rules.|Use a small dataset where the expected destination records are known and compare every successful result with the expected values.|To be added in later assignments.|
|C2|If a unit of migration work fails, it must not be reported as successfully completed or leave only part of that work recorded as successful.|Introduce a controlled failure during part of a migration and inspect both the migration status and the destination records.|To be added in later assignments.|
|Q1|**Proposed target:** When using the same 100,000-record test file and transformations on the same computer, the multi-worker version should process at least 25% more records per second than the single-worker version while still satisfying C1 and C2. The 25% value is an initial proposed target and may be revised after the single-worker baseline is measured.|Run the same migration with one worker and with multiple workers. Measure records processed per second and compare the results while also checking correctness. This target has not been measured yet.|Proposed target; measurement details will be added later.|

## **Inputs and outputs**

An ordinary input would be a CSV file such as:

```text
employee_number,full_name,hire_date
E101,Ava Chen,2021-05-10
E102,Marcus Lee,2020-09-01
```

For the example mapping, the expected destination data would look like:

```text
employee_id,first_name,last_name,start_date
E101,Ava,Chen,2021-05-10
E102,Marcus,Lee,2020-09-01
```

An unsuccessful case would happen if the destination requires an `employee_id`, but the user does not map any source field to that required field. In that situation, the system should identify that the required mapping is missing and prevent the migration from starting instead of creating incomplete destination records.

## **Assumptions**

- The initial input files will be CSV files containing a header row.
- Each record will have a field that can be used as a unique record key.
- The destination schema and its required fields will be known before the mapping begins.
- The first version will support a limited set of transformations, such as renaming fields, splitting a value, and formatting dates.
- Synthetic data can be used to test normal cases, errors, and changed records without using private real-world data.
- The proposed performance target may change after actual measurements are collected later.

## **Constraints**

- The project is being completed by one student, so the system must remain small enough to design, build, and test within the course.
- CSV will be the first supported input format.
- PostgreSQL is the planned destination database.
- The project must be able to run and be tested on the available computer.
- Multiple worker processes may run on one computer during development, but this will not be described as equivalent to a production multi-machine distributed system.
- Only public documentation and synthetic data will be used.
- Production cloud deployment, enterprise authentication, and a complete Change Data Capture system are outside the project scope.


# **3 Alternatives and selected solution**

For Assignment 2, I am comparing possible ways the migration system could process its data. I am not making the final design choice yet because the final choice will be made during Assignment 3.

|**Approach and source**|**Useful behavior**|**Limitation**|**Evidence or assumption**|
|---|---|---|---|
|**Single-worker ETL baseline**|One worker reads, transforms, and loads the records in order. This is simpler to understand and provides a useful baseline for comparing performance. PostgreSQL transactions could also help prevent incomplete database updates.|One worker handles all of the processing, which may become slow for large datasets. Additional logic would still be needed for change detection.|PostgreSQL transactions provide an existing approach for grouping database operations so incomplete operations can be rolled back. The performance limitation will need to be measured later.|
|**Custom multi-worker migration system**|The migration can be divided into smaller jobs and processed by several workers at the same time. The project can also keep field mapping, progress monitoring, and file-based change detection inside one focused system.|Multiple workers make the system more complicated because the design must handle job distribution, failures, duplicate work, worker coordination, and job size.|Distributed systems such as Apache Spark show that dividing large processing jobs into smaller tasks is an established approach. The performance benefit of my system has not been measured yet.|
|**Apache Spark**|Spark already supports parallel processing and structured data. It could handle the part of the project involving large amounts of data and multiple workers.|Spark is a general-purpose processing framework and does not provide the complete migration workflow I want to build. I would still need to create the field-mapping interface, progress monitoring, change tracking, and other migration-specific features. It may also add more complexity than this individual project needs.|Apache Spark documentation describes using executors and tasks to process distributed workloads.|

## **Comparison against the same requirements**

|**Requirement area**|**Single-worker baseline**|**Custom multi-worker system**|**Apache Spark**|
|---|---|---|---|
|F1-F2: input and mapping|Can support.|Can support.|Needs separate application logic.|
|F3: processing|Can support, but processing is sequential.|Can support while dividing work across multiple workers.|Strong support for parallel processing.|
|F4: progress|Must be added.|Can be built into the migration system.|User-facing migration progress still needs separate application logic.|
|F5: change detection|Must be added separately.|Can be included in the migration system.|Must be added separately for uploaded CSV files.|
|C1-C2: correctness|Simpler to coordinate; database transactions can help.|Requires careful worker coordination.|Destination correctness rules still need separate design.|
|Q1: performance|Provides the baseline.|Intended to improve throughput; this must be measured.|Designed for parallel processing but may add more complexity than needed.|

## **Current direction**

I am not making the final choice in Assignment 2. The **custom multi-worker approach** is currently the main direction because it matches the original project goal of building my own web-based migration tool while still allowing me to investigate distributed processing.

The **single-worker approach** will remain useful as a simple baseline that the multi-worker version can later be compared against.

**Apache Spark** is an existing distributed alternative that shows how large workloads can be divided among multiple workers, but using Spark for the entire project could hide some of the worker-coordination problem that I want to design and understand myself.

The final approach will be selected in Assignment 3 after I examine the architecture and feasibility in more detail.

## **Decision 1**

**Work to come - Assignment 3.**

## **Decision 2**

**Work to come - Assignment 3.**


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
|November 13, 2026|Added the initial requirements and system specification in Section 2 and drafted the alternatives comparison in Section 3.|Assignment 2 requires observable requirements and a comparison of possible approaches before the final design choice in Assignment 3.|
|**Open question**|**Why it matters**|**Next action**|
|How should a large migration be<br>divided among multiple workers<br>without adding too much<br>coordination overhead or<br>producing incorrect destination<br>data?|Work division is central to the<br>distributed part of B2 and will<br>affect both performance and<br>correctness in the completed<br>project.|Research and compare possible<br>work-division approaches during<br>the later requirements and<br>alternatives assignments before<br>selecting a design.|



## **Assistance and reuse:** 

This document is based on my B2 Problem Understanding Paper, the course provided design template, and the Software Project Design Handbook. No implementation results or performance measurements are claimed in this Assignment 2 draft. 

## **References** 

1. Los Angeles County Sheriff’s Department. Integrated Justice Information System - Exhibit A: Statement of Work, RFP 712-SH. Supports the problem evidence concerning mappings, transformation, full and incremental migration, validation, reconciliation, and auditing. 

<u>https://lasd.org/wp-content/uploads/2026/10/Solicitations_RFP712-SH_4_ExhA_100126.pdf</u> 

2. Apache Spark. Cluster Mode Overview. Provides an existing distributed-processing approach for understanding how larger jobs can be divided into tasks and coordinated across executor processes. 

<u>https://spark.apache.org/docs/latest/cluster-overview.html</u> 

3. CSC 59866 course materials. Software Project Design Handbook and Design Document Template, Fall 2026. Used for the Assignment 1 structure, scope, Markdown requirements, and weekly design process.

4. PostgreSQL Global Development Group. Transactions. Supports the use of transactions when reasoning about reliable destination updates.

<u>https://www.postgresql.org/docs/current/tutorial-transactions.html</u>

5. Apache Spark. Spark SQL, DataFrames and Datasets Guide. Supports structured-data processing using Spark.

<u>https://spark.apache.org/docs/latest/sql-programming-guide.html</u>

6. Debezium. Debezium Connector for PostgreSQL. Supports the idea of detecting later changes after an initial snapshot and helps distinguish database change capture from the simpler file-based change tracking planned for this project.

<u>https://debezium.io/documentation/reference/stable/connectors/postgresql.html</u>

