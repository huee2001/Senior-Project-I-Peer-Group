What problem are you investigating?

Describe a specific difficulty and the conditions under which it occurs. Walk through one concrete example, including the normal behavior and what goes wrong. Define the boundaries of the problem.

Problem Statement - (1) Want to keep fair in mind in which valuable data is easy to find (2) Want a sort of version control system that tracks changes to the document. (Organizations/researchers should manually upload the changes). (3) A way to alert people who downloaded

Problem Statement (attempt 2) - One way data becomes meaningless overtime with high volume of data is because its hard to find, access, or has messy formatting that makes it harder to reuse by either human or machine. Another way data can become meaningless is the changes in data without the user knowing, causing them to work with outdated, incorrect data.

Problem Statement (attempt 3) - Research can go on for long periods of time. During this time, researcher A can rely on old research from researcher B. However, researcher A may be oblivious to the changes made by researcher B, ultimately compromising the efforts of researcher A if they heavily relied on this. This is because the old research may get updated with corrected values, better formatting for understandability, or even have a bigger sample size that researcher A may not know about despite relying heavily on the data. How can a researcher keep track of these changes so as to not compromise their ongoing research? How can one scientific researcher essentially be able to always have up-to-date data for them to use?

Solution can be some type of version control system to alert users when there has been an update to their downloaded copy, and what changes we’re made. It can be solved through modern distributed means, where each person has their own replica of the data on their machine, and once they visit the website dashboard it can alert all who downloaded the replicas of the newly updated data. Documenting things such as what was the change, when was the change, and what version it is. An additional solution that also answers the problem of how to make it so scientific research has up-to-date data they need for their research, is to follow the FAIROS program “FAIR”(Findable, Accessible, Interoperable and Reusable) protocol to make sure this data isn’t hidden to people in need of certain data and has a standardized format making it easier for humans and machines to work with.

Problem Statement (attempt 4) - It is not unusual for a researcher to rely on or build on top of an existing dataset published by other organizations or independent researchers. But it’s important to note that scientific research can go on for long periods of time. And during this time frame, the dataset these researchers rely on may change without the researcher knowing. Changes like updating the old dataset


with corrected values, renaming field names, changing units and/or adding more samples to the dataset. The problem that arises is researcher may not be aware that they are using an outdated dataset, or if they do realize and download the newest version of the dataset, the meaning and formatting isn’t preserved, causing the researcher to spend time reinterpreting this new dataset instead of a seamless transition. For example, researcher A conducts a study on how to perform better in school, and relies on an old dataset from researcher B that surveys the average study time for different grade levels. Previously, the dataset from researcher B uses “FR” that stands for freshman in one of the fields, and uses student data from 2019. Researcher B updates the datasets with more up-to-date samples(i.e students from 2019 to students from 2026) changes FR to just F. Researcher A may not know about these helpful updates in values and continues to use outdated data. And if researcher A is noted about an update to the change, they may not understand the meaning behind the field names any longer. In either case, researcher A is now working with data that may compromise their ongoing research. How can we develop a system that not only notifies users of any changes to their replica of data but also preserves

the meaning of the data in the newest version to allow for seamless usage?

(changes should be seamless and cause no amount of trouble)

(possible documentation to the changes)

“Research can go for long periods of time. During this time, it is not uncommon from researchers to heavily rely on or build ontop of preexisting scientific data. But if researcher A relies on old research from researcher B, researcher A may be oblivious to the changes made by researcher B, ultimately compromising the efforts of researcher A. This is because the old data may not be updated with more corrected values, changed formatting and other important improvements compared to the old version. So how can a researcher keep track of these changes as to not compromise their ongoing research.

A solution to this frame

Who or what is affected by it?

Identify the users, organizations, or systems affected. Explain the consequences, such as missing information, repeated work, slow results, or incorrect decisions. Connect those consequences to your example.

Downstream researcher(People who rely on preexisting datasets) - There are two potential consequences of this problem. Relying on old data causes their ongoing research to be seen as unreliable and questions their integrity. Another consequence is the meanings/format not being preserved. The researcher may have to spend extra time finding where the previous dropped column names changed to,

or if there were even a replacement to them in the first place. In either case, it wastes time

Data publishers (People/organizations who post data) - When a researcher dedicates time to publish or

update their study, it may not be seen. This leads to their work potentially being lost in the vast volume


of information online due to the failure of cyberinfrastructure. **The research paper, “Shedding light on the dark data in the long tail of science”, talks about this when it coins the term dark data.

Ai engineers: People who train models on a previous dataset are affected. If a model was trained on a 2019 version with “FR” for freshman, and the data is later updated with new samples, retraining or evaluating the model with the new version without noticing the changes can cause the model to

missclassify some labels and yield worse predictions.

## What evidence do you currently have that it is a real problem?

Explain what the published opportunity and technical sources establish. Identify observations or measurements you have actually made. Clearly label assumptions and missing evidence. A request for a product or research topic does not prove that your specific failure has occurred.

Published opportunity(notes) -

Context (ignore) First and foremost, a group of stakeholders proposed the idea of using the FAIR guiding principles, with the intent of making data more reusable by other scholars. It’s an urgent call to action as data has increased in volume and complexity over time, making it harder to find and reuse for research purposes. More details on this in their published paper, “The FAIR Guiding Principles for scientific data management and stewardship”

New FAIROS is an NSF funding program that wishes to fund open science activities. The main problem it is trying to address is that research data may be harder to find and/or integrate with other ongoing research. The goal is to make research data and other related outputs become more usable by following the FAIR guiding principles (Findable, Accessible, Interpoolable, Reusable). Interoperable and reusable here could mean research A works on the same topic as researcher B, but when he/she tries to combine, there are too many mismatches in the field names,rows, or values(overall schema incompatibility). Making it harder to seamlessly integrate both their findings.

FAIROS also advocates for creating new, potentially better models that drive better scientific communication (possibly better than FAIR principles) with emphasis on increasing efficiency and accessibility. It wishes

(Final) Lowering barriers, meaning making the document and data easier to integrate, link with other data, easier to access, and available across multiple domains


## Fair principles:

- Finability: Easy for humans and computers to search and locate.

- Accessibility: Openly available without unnecessary restrictions. (meaning free, no subscription, no paywalls)

- Interoperable: Able to work seamlessly across different systems and software.

- Reusable: Well-documented so others can safely build on or verify the findings1.

Other evidence of it being a problem

80/20 rule in data science

According to a Pragmatic institute article, titled “Overcoming the 80/20 Rule in Data Science,” it states “Data practitioners spend 80% of their valuable time finding, cleaning, and organizing the data. This leaves only 20% of their time to actually perform analysis on it.” This is a huge concern considering the size of complexity of data only increasing over time. Now, if there was a pipeline setup involving the old dataset, and a researcher intends to use an updated version, they would have to spend 80% of their time, if not more, manually altering the pipeline to account for the schema changes, data samples, units etc. This is a huge concern and time waster with the growing use of AI. And in addition to this, since time spent looking for data is included in the 80%, it may become even more difficult unless there are platforms that implement something akin to the FAIR guiding principles.

https://www.pragmaticinstitute.com/resources/articles/data/overcoming-the-80-20-rule-in-data-science /

Guidance on Versioning of Digital Assets

In this paper, by Helmholtz Metadata Collaboration, it states the importance of having good version control of documents and datasets. “Using the wrong version of a (meta)data set can lead to drastically different outcomes in interpretation, and lead to substantial, propagating downstream errors.” It then goes on to say “...a digital "chain of evidence" that records who changed what and why over the life cycle of a digital asset is a key component of good data management. …Without this chain, and the transparency it brings, it is far more difficult to assess the trustworthiness of (research) data, especially as projects close and the individuals who generated the data are no longer available. “ These passages highlight the existing risks of bad version control documentation. It noted the problem in a general

1 Similar to what the “Versioning Data Is About More than Revisions: A Conceptual Framework and

Proposed Principles” paper wants to resolve


sense, where downstream errors can be a variety of things such as using old values that were corrected in the newest versions, and highlights a specific problem of how not having proper documentation and preserving meanings through each version can create distrust in the credibility of the data. Both things compromise the ongoing research of a downstream researcher which is a problem mentioned in my problem statement.

[Guidance on Versioning of Digital Assets](https://elib.dlr.de/193967/1/2022-12_HMC-Paper_3_Versioning_v1-1.pdf)

(my definition of Downstream researchers are those who work on a replica on their own local machine from a given source).

Versioning Data Is About More than Revisions: A Conceptual Framework and Proposed Principles

This paper states that datasets are often updated or altered for things such as increasing sample size, correcting values, or schema changes. It claims that these changes in versions should be clearly documented to allow reproductivity, and how it's a growing concern to be able to verify. For instance, the authors state:

“As more and more datasets are becoming available online, the versioning problem is becoming acute. In some cases, datasets have become so large that downloading the data as a single file is no longer feasible. Using web services, datasets can be accessed and subsetted at a remote source when needed, but the user often has no knowledge whether, and when, the dataset they accessed online has been changed or updated. Errors in research data have the potential to cause significant damage when used to inform decision making. A high-profile case was the retraction of a multi-national study on a potential COVID-19 treatment that had to be withdrawn because it could not be reproduced (Mehra et al, 2020)”

First thing to point out, is the mentioning of datasets becoming too large and having to download a subset. This is a big problem because users now rely on dynamic data instead of having a static copy on their local machine. If users rely on dynamic data, then changes to the data become much more unnoticeable. We need more specific guidelines to see what changes were made to understand how it will affect our research. And version control was mentioned in the problem statement.


Another jarring thing to note is these datasets are being used in big decision making process. It is essential to verify the data by trying to reproduce it. If the dataset was changed, and not knowing the specific changes, the data becomes unreliable. Which delays progress such as the covid 19 treatment example mentioned in the passage. This example slightly differs from my project however, since it focuses on downloalded copies instead of dyunamically pulling data

[1246-1-9224-1-10-20210323.pdf](https://storage.googleapis.com/jnl-up-j-dsj-files/journals/1/articles/1246/submission/proof/1246-1-9224-1-10-20210323.pdf)

past versions of datasets should be preserved for reproducibility, and if not, it should properly document the changes to ensure reproducibility to verify the credibility of the dataset.

Shedding Light on the Dark Data in the Long Tail of Science

This paper starts by saying scientific research outputs data, but infrastructures that are responsible for preserving and spreading the data are doing a bad job at it. This leads to the coined term, “Dark Data.”

Dark data is essentially research data that hasn’t been sufficiently documented in ways such as indexing it (making it easily findable) and storing it. The problem here is that scientists aren’t able to make use of this valuable data since it's so hard to find.

This directly ties into the FAIR guiding principle that is trying to solve a problem like this

Observation: Sometimes using someone's dataset from kaggle, there's an update to the dataset. The one previously used obviously leads to different results when using it on an AI model. This becomes a problem especially if the changes aren't documented. And may have a harder time creating a new pipeline to clean and format the data.

Assumptions: Many platforms allow publishers to add version notes or field descriptions(i.e Kaggle) , but do not require them or enforce a consistent, machine-readable way to record schema or unit changes, so a change can go undocumented.

What solutions already exist?

Compare at least two existing approaches. Explain how they work, what they handle well, and their

limitations under your chosen conditions. Use relevant documentation to support the comparison.

OpenRefine is an open-source tool for cleaning and transforming data. Primarily useful for consistently standardized updated datasets. It records every transformation in an undo/redo history, and that history


can be extracted as JSON and reapplied to another project. The limitation is that this is more helpful for researchers rather than people who publish datasets. For example, a researcher can format an existing dataset tailored to their benefits. Some useful tools provided: Tools such as edit rows where sorting is based on value of one column; Split and join column where the user may join or separate column based on a character or string; Fingerprinting which is most helpful and considered fast, where it goes through all rows, removes punctuations, all whitespace, uppercase, and compares them all to see if they are the same. If they are, combines it to one row which acts as a “key” value.

GitHub records the full history of a dataset’s files, including who changed what and when, and let

publishers mark versions with tags and releases. Its limitations is that it doesnt, to my knowledge, notify a downstream researcher of the updated versions. Must be checked manually

## What is the most important thing you still do not know?

Identify the uncertainty that most affects your proposed work. Describe a research step or experiment

that could resolve it. State what data, scenario, or measurement you would use and how the result would influence your design.

What I still don’t know is how much documentation is needed, what’s the best way to preserve meaning for different categories (dates, units, semantics values etc.)

## Your Individual Scope

Define what you will investigate, what you will exclude, and the comparison you will make. Identify the tools, data, or simulation you expect to use. Briefly describe a possible solution direction without treating it as a proven answer. Explain why the work is manageable for one student.

I think for my scope, I will focus less on cleaning the data and following FAIR guidelines, and more on trying to find a way to better preserve meaning across different versions. If that seems a bit hard to focus on I may consider a balance between the two.

## IGNORE BELOW, PERSONAL NOTES

How others are doing it


Open Refine - (1) Software tool, desktop application. (2) manually cleans and standardizes messy datasets. (3)Tools shows as edit rows where sort based on value of one column; Split and join column where the user may join or separate column based on a character or string; Fingerprinting which is most helpful and considered fast, where it goes through all rows, removes punctuations, all whitespace, uppercase, and compares them all to see if they are the same. If they are, combines it to one row which acts as a “key” value. More documentations here2

Great expectations - Python validation framework to see if dataset conforms to certain expectations and rules.

Use at least three relevant sources. Include the published opportunity, technical documentation for an existing approach, and additional research or technical material that helps explain the problem. Place full web addresses beside the paragraphs they support. Explain acronyms before using them.

Source 13 - Shedding light on the dark data in the long tail of science

Purpose: This source tells us

- (1) Starts with saying scientific research outputs data, but infrastructure responsible for preserving and spreading the data are doing a bad job at it

- (2) Coins the term “Dark data”, where data from scientific research is outputted, but it hasn’t been sufficiently documented in ways such as indexing it (making it easily findable) and storing it. The problem here is that scientists aren’t able to make use of this valuable data since its so hard to find.

- (3) These data becomes unusable and ultimately meaningless. The effort put into the research can eventually become lost for a long time.

Source 24 - Using Old Data: When Is It Appropriate?

Source 3 - https://forrt.org/curated_resources/data-overuse-in-aging-research-emerging/ Source 4 potential - Data Cascades in Machine Learning [URL 🔗](https://forrt.org/curated_resources/data-overuse-in-aging-research-emerging/)

Source 55 (use) Versioning Data Is About More than Revisions: A Conceptual Framework and Proposed Principles


Purpose: Highlights the point that datasets are constantly updated or altered, yet there is not a good standard way to track these changes/versions. Because of this, researchers aren’t able to replicate the results/findings of the dataset if values change without clear version tracking (or without researchers realizing it) . Not being able to reproduce the results of the dataset makes it harder to confirm if the dataset is accurate and in turn makes it less likely to be used.

Purpose: Emphasizes the point that datasets are constantly being updated or altered. Researchers need to understand the differences between different versions because it can lead to different results after analysis. The author analyzed 33 different organization practices and came to the conclusion that there isnt a standardized system version tracker. This is a problem because different vers

- Why using same dataset is bad? Which leads to looking for more datasets Sources

- (1) Technical documentation for existing approach(Clean data) Solved, OpenRefine

- (1) Technical documentation for existing approach (general hub, easily accessible)

- (2) Material that helps explain the problem Solved, “Shedding light on the dark data in the long tail of science”

## Connect to distributed systems

- Different local machines are called nodes

- Nodes communicate with each other by passing each other messages

- Replicas is a copy of the data sitting in that individual machine/node.

- Replica copy of dataset or database in a machine

- Scientifici data not hosted on one large database, spread out to multiple different nodes. Distributed solution helps propagate updates, version histories and corrections. Each of these updates gets alerted and these nodes have the ability to pull the changes
