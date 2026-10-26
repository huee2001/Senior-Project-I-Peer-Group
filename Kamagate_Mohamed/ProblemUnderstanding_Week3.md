*Reupload into group repo* 

## What problem are you investigating?

*Describe a specific difficulty and the conditions under which it occurs. Walk through one concrete example, including the normal behavior and what goes wrong. Define the boundaries of the problem.*




**improved problem statement** 
It is not unusual for a researcher to rely on  or build on top of preexisting data. But it’s important to note that scientific research can take a long time to complete. During this time, the datasets these researchers rely on may have changed(i.e more samples, corrected values etc). The problem is, oftentimes there is no community-agreed upon, practical way to document these changes as best as possible. The way to preserve the meaning often fluctuates between data providers. Not documenting these changes to the dataset can compromise the work of the researcher in different ways. 


For example, researcher A does a study on academic study habits (i.e studying time, environment, grade level etc. ) and relies on researcher’s B dataset that documented 2019 study times across different grade levels. If researcher B updates his/her dataset with things like correcting values, changing field names from FR(freshman) to just F,  and using samples from 2026 instead of 2019. Several problems can arise from this: The first problem is that researcher A may not know about the new and improved dataset. When researcher A is done with his/her study, they may be seen as unreliable for using an outdated data set. The second potential problem is that if researcher A was aware of the updated dataset, they may not know what these changes, specifically to the structure and schema, means. Since there was no mandated changelog to document what F refers to, the researcher would spend time reinterpreting the new dataset.  Both of these problems are all subsets to the main problem of not having a mandatory proper, consistent documentation method to help preserve the integrity and meaning of the dataset. 

*can skip this example if confusing*
Another example that applies to the real world was the covid scandal. Researchers (including world health organization) accepted a multi-national study  about covid treatment and how a certain drug was ineffective. This caused the testing trials on the drug to halt, however it was found out that there was no documented dataset that lead to this conclusion. The problem here is since there was not standardized system of documentation and mandation of documentation, the assumedly fake research was able to get away seeming legit. In general, not having a snapshot of how a dataset led to the researchers conclusions causes the conclusions to be illegitimate if researchers aren't able to use that dataset to come to the same conclusions (failure of reproductivity). 
To recap, the difficulty is not having a proper way to preserve meaning of changed data and downstream researchers not being alerted about the changes. The conditions to which this occurs are primarily in areas of research, open-science activities, essentially anything evolving sharing of data amongst scholars. 


The hopeful aim of this project is to develop a platform where there is a mandatory, correct way where data providers can upload data, properly document the changes to the updated data, and alert downstream researchers who downloaded a copy of that data. The changes should be human-readable, meaning semantic changes should be documented for the user (example with FR to F both standing for freshman) and machine-actionable meaning the data should be easily accessible by machines and they should be able to differentiate between the versions. 


The boundaries of this problem (which may be subject to change) may be prioritizing preserving meaning first across versions, alerting downstream researchers when a change to their replica has occurred may not be considered as much or treated as a secondary, and I believe I may try to keep the changes as minimal as possible for now (i.e added/deleted samples and schema change). 
This is a distributed related problem because downstream researchers have their own local copy on their own respective nodes. The platform should keep track of these nodes, whenever the original dataset gets updated, it should notify every node whenever it the user checks their dashboard








## Who or what is affected by it?

*Identify the users, organizations, or systems affected. Explain the consequences, such as missing information, repeated work, slow results, or incorrect decisions. Connect those consequences to your example. *

<ins>Downstream researcher(People who rely on preexisting datasets)</ins> - There are two potential consequences of this problem. Relying on old data causes their ongoing research to be seen as unreliable and questions their  academic integrity. Another consequence is the meanings/format not being preserved. For instance, the researcher may have to spend extra time finding where the previous dropped column names changed to, or if there were even a replacement to them in the first place. In either case, it wastes a considerable amount of time.

<ins>Data publishers (People/organizations who post data)</ins> - When a publisher dedicates time to publish or update their study, it may not be seen. This leads to their work potentially being lost in the vast volume of information online due to the failure of cyberinfrastructure. **The research paper, “Shedding light on the dark data in the long tail of science”, talks about this when it coins the term dark data.

<ins> Ai engineers</ins>: People who train models on a previous dataset are affected. If a model was trained on a 2019 version with “FR” for freshman, and the data is later updated with new samples, retraining or evaluating the model with the new version without noticing the changes can cause the model to missclassify some labels and yield worse predictions.

## What evidence do you currently have that it is a real problem?

*Explain what the published opportunity and technical sources establish. Identify observations or measurements you have actually made. Clearly label assumptions and missing evidence. A request for a product or research topic does not prove that your specific failure has occurred.*

<ins>Published opportunity(notes)</ins> -

**Context (ignore)** First and foremost, a group of stakeholders proposed the idea of using the FAIR guiding principles, with the intent of making data more reusable by other scholars. It’s an urgent call to action as data has increased in volume and complexity over time, making it harder to find and reuse for research purposes. More details on this in their published paper, “The FAIR Guiding Principles for scientific data management and stewardship”
https://www.nature.com/articles/sdata201618

**New** FAIROS is an NSF funding program that wishes to fund open science activities. The main problem it is trying to address is that research data may be harder to find and/or integrate with other ongoing research. The goal is to make research data and other related outputs become more usable by following the FAIR guiding principles (Findable, Accessible, Interpoolable, Reusable). Interoperable and reusable here could mean research A works on the same topic as researcher B, but when he/she tries to combine, there are too many mismatches in the field names,rows, or values(overall schema incompatibility). Making it harder to seamlessly integrate both their findings.

https://www.nsf.gov/funding/opportunities/fairos-findable-accessible-interoperable-reusable-open-science

FAIROS also advocates for creating new, potentially better models that drive better scientific communication (possibly better than FAIR principles) with emphasis on increasing efficiency and accessibility. It wishes

(Final) Lowering barriers, meaning making the document and data easier to integrate, link with other data, easier to access, and available across multiple domains


## Fair principles:

- Finability: Easy for humans and computers to search and locate.

- Accessibility: Openly available without unnecessary restrictions. (meaning free, no subscription, no paywalls)

- Interoperable: Able to work seamlessly across different systems and software.

- Reusable: Well-documented so others can safely build on or verify the findings.
https://www.gofair.foundation/fair-principles

As to how this relates to the project, it advocates for better documentation of data. 1) Persistent and unique identifier for a dataset and its variants, findable 2)metadata should be availiable even if the data isn't, accesible 3) wwhen data is shared, it should be easy for other researchers to use especially when updates occur, interperable, 4) reusable, being coherent enough for other researchers to use.
                    **Other evidence of it being a problem**

<ins>80/20 rule in data science</ins>

According to a Pragmatic institute article, titled “Overcoming the 80/20 Rule in Data Science,” it states “Data practitioners spend 80% of their valuable time finding, cleaning, and organizing the data. This leaves only 20% of their time to actually perform analysis on it.” This is a huge concern considering the size of complexity of data only increasing over time. Now, if there was a pipeline setup involving the old dataset, and a researcher intends to use an updated version, they would have to spend 80% of their time, if not more, manually altering the pipeline to account for the schema changes, data samples, units etc. This is a huge concern and time waster with the growing use of AI. And in addition to this, since time spent looking for data is included in the 80%, it may become even more difficult unless there are platforms that implement something akin to the FAIR guiding principles. In short, since data always updates, it becomes a problem for data practitioners if the changes aren't well documented. Both for machine and humans alike 

https://www.pragmaticinstitute.com/resources/articles/data/overcoming-the-80-20-rule-in-data-science /

<ins>Guidance on Versioning of Digital Assets</ins>

In this paper, by Helmholtz Metadata Collaboration, it states the importance of having good version control of documents and datasets. “Using the wrong version of a (meta)data set can lead to drastically different outcomes in interpretation, and lead to substantial, propagating downstream errors.” It then goes on to say “...a digital "chain of evidence" that records who changed what and why over the life cycle of a digital asset is a key component of good data management. …Without this chain, and the transparency it brings, it is far more difficult to assess the trustworthiness of (research) data, especially as projects close and the individuals who generated the data are no longer available. “ These passages highlight the existing risks of bad version control documentation. It noted the problem in a general(Similar to what the “Versioning Data Is About More than Revisions: A Conceptual Framework and Proposed Principles” paper wants to resolve) sense, where downstream errors can be a variety of things such as using old values that were corrected in the newest versions, and highlights a specific problem of how not having proper documentation and preserving meanings through each version can create distrust in the credibility of the data. Both things compromise the ongoing research of a downstream researcher which is a problem mentioned in my problem statement.

[Guidance on Versioning of Digital Assets](https://elib.dlr.de/193967/1/2022-12_HMC-Paper_3_Versioning_v1-1.pdf)

(my definition of downstream researchers are those who work on a replica on their own local machine from a given source).

<ins>Versioning Data Is About More than Revisions: A Conceptual Framework and Proposed Principles</ins>

This paper states that datasets are often updated or altered for things such as increasing sample size, correcting values, or schema changes. It claims that these changes in versions should be clearly documented to allow reproductivity, and how it's a growing concern to be able to verify. For instance, the authors state:

>“As more and more datasets are becoming available online, the versioning problem is becoming >acute. In some cases, datasets have become so large that downloading the data as a single file >is no longer feasible. Using web services, datasets can be accessed and subsetted at a remote >source when needed, but the user often has no knowledge whether, and when, the dataset they >accessed online has been changed or updated. Errors in research data have the potential to >cause significant damage when used to inform decision making. A high-profile case was the ??>retraction of a multi-national study on a potential COVID-19 treatment that had to be withdrawn >because it could not be reproduced (Mehra et al, 2020)”

First thing to point out, is the mentioning of datasets becoming too large and having to download a subset. This is a big problem because users now rely on dynamic data instead of having a static copy on their local machine. If users rely on dynamic data, then changes to the data become much more unnoticeable. We need more specific guidelines to see what changes were made to understand how it will affect our research. And version control was mentioned in the problem statement.


Another jarring thing to note is these datasets are being used in big decision making process. It is essential to verify the data by trying to reproduce it. If the dataset was changed, and not knowing the specific changes, the data becomes unreliable. Which delays progress such as the covid 19 treatment example mentioned in the passage. This example slightly differs from my project however, since it focuses on downloaded copies instead of dynamically pulling data. past versions of datasets should be preserved for reproducibility, and if not, it should properly document the changes to ensure reproducibility to verify the credibility of the dataset.

Overall, mandating a structured data documentation leads to more reliability and usage of the data itself.


[1246-1-9224-1-10-20210323.pdf](https://storage.googleapis.com/jnl-up-j-dsj-files/journals/1/articles/1246/submission/proof/1246-1-9224-1-10-20210323.pdf)



<ins>Shedding Light on the Dark Data in the Long Tail of Science</ins>

This paper starts by saying scientific research outputs data, but infrastructures that are responsible for preserving and spreading the data are doing a bad job at it. This leads to the coined term, “Dark Data.”

Dark data is essentially research data that hasn’t been sufficiently documented in ways such as indexing it (making it easily findable) and storing it. The problem here is that scientists aren’t able to make use of this valuable data since it's so hard to find.

This directly ties into the FAIR guiding principle that is trying to solve a problem like this

Observation: Sometimes using someone's dataset from kaggle, there's an update to the dataset. The one previously used obviously leads to different results when using it on an AI model. This becomes a problem especially if the changes aren't documented. And may have a harder time creating a new pipeline to clean and format the data.

Assumptions: Many platforms allow publishers to add version notes or field descriptions(i.e Kaggle) , but do not require them or enforce a consistent, machine-readable way to record schema or unit changes, so a change can go undocumented.

## What solutions already exist?

*Compare at least two existing approaches. Explain how they work, what they handle well, and their limitations under your chosen conditions. Use relevant documentation to support the comparison.*

<ins>Zenodo:</ins> Strengths is, zenodo provides DOI for all published uploads. Uses DOI versioning which allows: “edit/update the record’s files after they have been published. cite a specific version of a record. cite all of versions of a record.” According to their help versioning page. It also provides tow DOI, one representing all versions of the data, and another referring to a specific version of the data


The limitations are, it doesn’t alert people of the version changes/updates. Users will have to manually check to see if there’s been updated data. Another weakness is the idea of “semantic versioning.” It’s entirely up to the data provider whether or not they want to include human readable notes that document what the changes are and why the changes are made. 


<ins>Github(2):</ins> Strengths are, records full history of changes to the data, including who change what and when. Commit message is also attached to each change for semantic versioning. Can see a “snapshot” of each version. Very machine-actionable
Limitations are, doesn’t notify downstream researchers of updated versions, must be manually checked. Another limitation is line by line comparison of changes in diff file , and commit messages can be wishy washy in quality (i intend to solve by making it community based. Can like or dislike based on how good documentation is. )


<ins> OpenRefine </ins> is an open-source tool for cleaning and transforming data. Primarily useful for consistently standardized updated datasets.  It records every transformation in an undo/redo history, and that history can be extracted as JSON and reapplied to another project. The limitation is that this is more helpful for researchers rather than people who publish datasets. For example, a researcher can format an existing dataset tailored to their benefits. Some useful tools provided: Tools such as edit rows where sorting is based on value of one column; Split and join column where the user may join or separate column based on a character or string; Fingerprinting which is most helpful and considered fast, where it goes through all rows, removes punctuations, all whitespace, uppercase, and compares them all to see if they are the same. If they are, combines it to one row which acts as a “key” value.

## What is the most important thing you still do not know?

*Identify the uncertainty that most affects your proposed work. Describe a research step or experiment*

that could resolve it. State what data, scenario, or measurement you would use and how the result would influence your design.

Some other things I still don’t know: 

what’s the best way to preserve meaning for different categories like dates, units, semantics values  and so on. Should dates all follow a YYYY-MM-DD format for example

What constitutes as enough to be considered a new version? For example, if you change the metadata should it be considered a new version?

What needs to be included in versioning history? 

How should a version be named or numbered? 
What versioning information should be included in data citation?
How much change is enough for it to be considered a new release instead of a revised dataset?

A research step I can do to go about this is when protyping, I can include two very small data sets, each with atleast 2 versions to them. I will have people test them to see which documentation format is more preferable. 

I am also curious about how much FAIR guiding principles I should incoprporate, but not sure if that is beyond the s cope of my project. 
## Your Individual Scope

*Define what you will investigate, what you will exclude, and the comparison you will make. Identify the tools, data, or simulation you expect to use. Briefly describe a possible solution direction without treating it as a proven answer. Explain why the work is manageable for one student.*

I will investigate which version and description rules let a researcher correctly interpret both the old and new versions of a dataset after its publisher changes it.I will also check whether a researcher holding a downloaded copy can tell that their copy is out of date by comparing version tags.

I will exclude being able to remotely pull data dynamically, and only include downloaded replicas. 

Possible solution is requiring a structured documentation of changes between versions. A diff file would only help for machine-actionable goals, but also mandating semantic versioning may hopefully lead to better understanding of the changes by the reader. A diff file, semantic versioning notes along with way to tell how significant the changes are(possibily major.minor.patch.syntax format) between each versions will hopefully lead to better downstream research. 

I will also try to incorporate FAIR methods in the process. 

## IGNORE BELOW, PERSONAL NOTES

How others are doing it


Open Refine - (1) Software tool, desktop application. (2) manually cleans and standardizes messy datasets. (3)Tools shows as edit rows where sort based on value of one column; Split and join column where the user may join or separate column based on a character or string; Fingerprinting which is most helpful and considered fast, where it goes through all rows, removes punctuations, all whitespace, uppercase, and compares them all to see if they are the same. If they are, combines it to one row which acts as a “key” value. (More documentations here Great expectations - Python validation framework to see if dataset conforms to certain expectations and rules.)

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
