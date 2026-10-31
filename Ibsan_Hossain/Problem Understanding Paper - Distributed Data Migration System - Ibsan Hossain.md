# **Problem Understanding Paper \- Distributed Data Migration System**

## **What problem are you investigating?**

The problem I am investigating is how to move a large amount of structured data from an older system into a new system quickly and correctly when the two systems may organize their data differently and the original data may continue changing while the migration is taking place.

The Los Angeles County Sheriff’s Department Integrated Justice Information System opportunity provides a real example of this problem. The County wants to replace several older jail-management systems with a modern cloud-based system. Its existing systems contain large amounts of historical and active records that must remain available and accurate during the transition. The County also states that the contractor is responsible for the data-migration approach, mappings between the old and new data, transformation logic, conversion routines, and reconciliation evidence.

Full web address: [https\://lasd.org/wp-content/uploads/2026/10/Solicitations\_RFP712-SH\_4\_ExhA\_100126.pdf](https://lasd.org/wp-content/uploads/2026/10/Solicitations_RFP712-SH_4_ExhA_100126.pdf)

The data-conversion aspect of the opportunity stands out as particularly significant since it involves the initial full upload as well as several subsequent catch-up migrations for the new system. It also involves record-level and field-level validation and audit trail for the migration process. This reveals that the actual process of migration is much more complex than just copy-pasting the same file. Data needs to be mapped, converted appropriately, processed, verified, and updated later on after changes to the source data.

In my project, I would take this challenge even further as it applies not just to justice records but also to other kinds of organizations. The resulting product will allow an employee of a particular organization to perform migration of a large file with some specific structure, such as a Comma-Separated Values (CSV) file, into a new database. As an example, an old file can have fields like employee\_number, full\_name, and hire\_date while the new database will have fields like employee\_id, first\_name, last\_name, and start\_date.

Typically, the data from the source will be mapped, processed, and successfully loaded into the destination database. This situation becomes more complicated if the dataset is really large or if there are any changes in the source data during the process of migration. Running the whole dataset on one single worker can take a lot of time. In case the source data gets changed while it is being processed, the destination will have outdated data.

This project aims to build an operational web-based data-migration system which provides the opportunity for the user to map the source data to a new schema, split the large migration task into smaller tasks, process these tasks by several workers at once, load the result into PostgreSQL, and detect the subsequent changes in order to process the modified records only.

## **Who or what is affected by it?**

The people most directly affected are employees, database administrators, developers, and data engineers responsible for moving information from an old system to a new one. In the absence of the migration tool, the users need to develop the mapping and transformation scripts, process loading, error handling, and updates. The users might have to monitor the jobs running for a long time and figure out why certain records fail.

Organizations are also affected because the migrated data may support important daily operations. For example, in the case of LA County, the old systems have booking, custody, legal, financial, and operations records. As per the County, these records are important for daily business activity, compliance, audit, reporting, and record retention. In addition, the County claims that the migration and system cutover maintain data integrity as well as support the connection between justice and health partners.

Full web address: [https\://lasd.org/wp-content/uploads/2026/10/Solicitations\_RFP712-SH\_4\_ExhA\_100126.pdf](https://lasd.org/wp-content/uploads/2026/10/Solicitations_RFP712-SH_4_ExhA_100126.pdf)

For instance, assume that the organization requires migrating five million records. In case the migration process takes time, it may not be possible to switch over to the new system soon enough. In case a field gets mapped wrongly, the destination will end up having wrong information. If some source records change during the migration process, the destination may contain outdated information. Such issues might make it necessary for work to be done again.

## **What evidence do you currently have that it is a real problem?**

The most compelling evidence that can be found is the LA County published opportunity. This organization defines its replacement of the legacy systems as a technically and operationally complicated task due to the age of these systems, quality of historical data, and integrations with other systems. The County also explicitly mentions data mappings, transformation rules, conversion logic, initial full load, incremental loads, validation, reconciliation proofs, and audit trail among the requirements for this task. Accurate initial and ongoing synchronization between existing database and new database is included in the list of success criteria for this project.

Full web address: [https\://lasd.org/wp-content/uploads/2026/10/Solicitations\_RFP712-SH\_4\_ExhA\_100126.pdf](https://lasd.org/wp-content/uploads/2026/10/Solicitations_RFP712-SH_4_ExhA_100126.pdf)

Current technological systems can also offer proof that the distribution of large data sets between several worker nodes has its value. Apache Spark is an example of a distributed computing platform used for processing large amounts of data. According to its official documentation, a Spark application includes a driver program that coordinates executor processes. A job is divided into smaller tasks, and those tasks are sent to executors for processing. In addition, Spark is capable of processing structured information contained in files and external databases.

Full web address: [https\://spark.apache.org/docs/latest/cluster-overview.html](https://spark.apache.org/docs/latest/cluster-overview.html)

Debezium offers an example for the problem where data becomes altered once it is copied initially. The approach used by Debezium is called Change Data Capture (CDC), meaning the identification of changes in source data. Its PostgreSQL connector allows creating a consistent snapshot at first and then capturing insertions, updates, and deletions from that point on. This shows that tracking changes after an initial migration is an established technical problem.

Full web address: [https\://debezium.io/documentation/reference/stable/connectors/postgresql.html](https://debezium.io/documentation/reference/stable/connectors/postgresql.html)

So far, I have not collected any performance measures for my own developed system because the product is not yet available. Thus, I cannot state that my system achieves a certain level of performance. It is true that the sources provided above prove that migration, transformation, distributed processing, and change tracking are technical issues. Once the product becomes available, my measurements will be used to prove that the developed product functions properly. Also, my measurements will help to find the optimal configuration of distributed processing.

## **What solutions already exist?**

One existing approach is the use of the classic ETL (Extract, Transform, Load) program involving just one worker. A program may read some records from the file, perform transformation and insert records into the PostgreSQL database. The usage of transactions of PostgreSQL will be helpful to make the process more reliable. According to PostgreSQL, a transaction is a number of operations that are executed as a single one. In case the transaction execution fails for some reason, incomplete data does not need to be saved in the database.

Full web address: [https\://www\.postgresql.org/docs/current/tutorial-transactions.html](https://www.postgresql.org/docs/current/tutorial-transactions.html)

This approach is simpler to build and manage, and it may work well for smaller datasets. However, one worker must perform all of the extraction, transformation, and loading work. As the amount of data and transformation work increases, that worker can become a bottleneck. A normal single-worker ETL program also needs additional logic if it must detect which records changed after the original migration.

A second approach is distributed processing with Apache Spark. Spark divides parallel computations into tasks and sends those tasks to executor processes. Its DataFrame system is designed for structured data and can read information from files and external databases. This makes Spark useful when a large workload can be divided into independent parts and processed in parallel.

Full web address: [https\://spark.apache.org/docs/latest/sql-programming-guide.html](https://spark.apache.org/docs/latest/sql-programming-guide.html)

The Spark technology handles the distributed processing aspect effectively, but it is a generic framework, not a full migration program that I want to create. There is still a need for defining field mapping, transformations to be done, handling of failed records, updating of the destination, and user interface.

The third technique that already exists is called Change Data Capture using Debezium. The Debezium toolset can take an initial snapshot of the supported database and then capture further insertions, deletions, and updates based on PostgreSQL transaction logs.

Full web address: [https\://debezium.io/documentation/reference/stable/connectors/postgresql.html](https://debezium.io/documentation/reference/stable/connectors/postgresql.html)

Debezium performs very well in handling database changes. However, it does not solve all of my problems. It is dependent upon the capabilities offered by databases it supports. A CSV file uploaded by an employee does not have any database transaction log for Debezium to track. Moreover, it does not offer the complete workflow from the process of uploading the legacy file, mapping of fields to the new layout, distribution of the transformation tasks, loading to the new database, and tracking the migration process in one interface.

I am not making the claim that ETL processes, distributed computing, transaction support, and CDC are non-existent before this point. Rather, what I will do is build my own migration product that combines everything required for this specific case into one system. The product will incorporate the web interface for mapping the schema, distributed job execution, loading to PostgreSQL, migration tracking, and change detection based on files.

## **What is the most important thing you still do not know?**

The thing I do not know and which is most important for me is how to distribute migration jobs between the workers properly. It is clear that the final product will consist of several workers but the size of jobs and the amount of workers could influence the performance. In case the jobs are too big, one worker will still work while others will be done already. In case the jobs are too small, the system could waste time on jobs creation, workers coordination and writing of small amounts of data into the database.

It is a design problem which should be solved inside the system but not outside it. I am going to solve it once the migration pipeline works by comparing different combinations of workers and jobs chunks sizes. I can compare systems with one, two, four workers and even more. I can also compare fixed large chunks of data with dynamic small chunks which are created when there is available worker.

The measurements will include total migration time, records processed per second, failed records, and destination-data correctness. Correctness should be maintained in all cases. Transformed destination data should be correct and source changes should be detected and processed correctly.

## **Your Individual Scope**

For my personal project, I will develop a tool to migrate the data from large structured datasets to a PostgreSQL database in the form of a web application. The user uploads a CSV file, maps the columns of the file, and initiates the process. My solution will distribute the data over multiple workers to process data in parallel and load it into the database.

Moreover, my tool will control the migration process and monitor further changes in the source data. Thus, it will be able to process newly added or changed rows without repeating the whole migration procedure. After completion, the software will be tested to ensure correct transformation and loading of the data and better performance by the use of multiple workers.

The programming language to be used will be Python; the database will be PostgreSQL. The web interface will be either Streamlit or FastAPI. During development, workers can be executed in different processes on the same machine in accordance with the distributed architecture.

Real LA County records, creation of an entire jail management system, all kinds of databases and file types, enterprise authentication, deployment of the solution to the production environment in the cloud, as well as implementation of the Change Data Capture platform like Debezium are outside the scope of the project.

## **Sources**

Los Angeles County Sheriff’s Department. *Integrated Justice Information System — Exhibit A: Statement of Work, RFP 712-SH.*  
[https\://lasd.org/wp-content/uploads/2026/10/Solicitations\_RFP712-SH\_4\_ExhA\_100126.pdf](https://lasd.org/wp-content/uploads/2026/10/Solicitations_RFP712-SH_4_ExhA_100126.pdf)

Apache Spark. *Cluster Mode Overview.* Apache Spark Documentation.  
[https\://spark.apache.org/docs/latest/cluster-overview.html](https://spark.apache.org/docs/latest/cluster-overview.html)

Apache Spark. *Spark SQL, DataFrames and Datasets Guide.* Apache Spark Documentation.  
[https\://spark.apache.org/docs/latest/sql-programming-guide.html](https://spark.apache.org/docs/latest/sql-programming-guide.html)

Debezium. *Debezium Connector for PostgreSQL.* Debezium Documentation.  
[https\://debezium.io/documentation/reference/stable/connectors/postgresql.html](https://debezium.io/documentation/reference/stable/connectors/postgresql.html)

PostgreSQL Global Development Group. *Transactions.* PostgreSQL Documentation.  
[https\://www\.postgresql.org/docs/current/tutorial-transactions.html](https://www.postgresql.org/docs/current/tutorial-transactions.html)

