Raed Jaber 
October 8th , 2026
CSC 59866
Kurt Brown

A08: Discovery Across Independent Research Data Repositories

What problem are you investigating?

The problem I am investigating is how researchers can reliably discover datasets when the information about those datasets is stored across several independent repositories. A repository may contain research datasets from one organization or subject area, while another repository contains different datasets. A researcher who does not know which repository contains the information they need may want to search across all of them at the same time.
The information used for this search is mainly metadata, which means information that describes a dataset rather than the dataset itself. Metadata can include the dataset's title, description, publisher, keywords, modification date, version, and location. The World Wide Web Consortium (W3C) created the Data Catalog Vocabulary (DCAT) as a standard way to describe datasets and data services. DCAT is intended to improve interoperability between catalogs and allows metadata from multiple catalogs to be consumed and aggregated. It also supports the idea of federated search across catalogs located at different sites. W3C
Source: W3C Data Catalog Vocabulary (DCAT) Version 3
The difficulty appears when one of the repositories becomes unavailable or when its metadata changes. There are two basic approaches that can be used for discovery. One approach is to contact each repository whenever a search is performed. I will refer to this as direct or federated search. Another approach is to periodically copy metadata from the repositories into a central catalog and search that catalog instead. The project catalog specifically asks me to investigate these two conditions: an unavailable repository and outdated information. Project_Selections
A concrete example would involve three repositories. Repository A contains climate datasets, Repository B contains water datasets, and Repository C contains air-quality datasets. A researcher searches for "NYC air quality." Under normal conditions, all three repositories are online, and Repository C returns a description of a dataset called NYC Air Quality Measurements. Both a direct search and an up-to-date central catalog should be able to return that dataset.
The problem changes if Repository C becomes unavailable. A direct search may no longer receive Repository C's metadata, so the dataset could disappear from the researcher's results even though the dataset itself still exists. A central catalog that previously copied the metadata might still return the dataset description. However, the central approach creates another problem. Suppose Repository C updates the description from version 2 to version 3 after the catalog's last synchronization. Until another update occurs, the central catalog could return version 2 even though it is no longer current.
DCAT 3 specifically includes properties for modification dates and dataset versions. For example, it distinguishes the date when a catalog record was modified and includes properties for identifying current and previous versions. This gives catalogs a way to represent changes, but it does not automatically decide how frequently independent catalogs should synchronize with one another. W3C
Source: W3C DCAT Version 3
My project is therefore not about designing a new Internet search engine or storing large scientific datasets. The boundary of the problem is much smaller. I am investigating the tradeoff between availability and freshness of metadata when searching a small number of independent repositories.
________________________________________
Who or what is affected by it?

The main users affected are researchers who need to discover datasets without already knowing exactly where those datasets are stored. Organizations that publish and maintain research datasets are also affected because they want their data to remain discoverable by other researchers.
The National Science Foundation's Integrated Data Systems and Services (IDSS) program shows that shared data infrastructure is an important area for scientific research. The program supports national-scale data and cyberinfrastructure systems and services intended to enable data-intensive and artificial intelligence-driven research and education across scientific disciplines. NSF - U.S. National Science Foundation
Source: NSF Integrated Data Systems and Services (IDSS)
A discovery failure can have different consequences depending on the situation. If a repository is temporarily offline and the search system depends entirely on live requests, the researcher may receive incomplete results. They might believe that no relevant dataset exists even though the dataset is simply located in the unavailable repository. This could cause repeated searching, additional manual work, or the use of a less appropriate dataset.
Outdated metadata creates a different problem. A researcher may find a dataset, but the search result could contain an old description, version, access location, or modification date. The researcher may then have to check the original repository manually before deciding whether the dataset is useful.
Using the earlier example, if Repository C becomes unavailable during the "NYC air quality" search, direct search might omit the result completely. If a central catalog is used instead, the researcher could still find the dataset but might see information that was copied before the newest update. The user therefore faces a tradeoff between missing information and possibly stale information.
The systems themselves are also affected. A direct-search service depends on the availability and response of several independent repositories. A centralized catalog has less dependence on every repository being available at search time, but it now has the responsibility of keeping its copied metadata synchronized.
________________________________________
What evidence do you currently have that it is a real problem?

There are several pieces of documented evidence supporting the broader problem, although I have not yet produced experimental evidence for my specific simulated failure.
First, the NSF IDSS program establishes that shared research-data infrastructure is an active technical and research need. NSF states that the program supports development, scaling, and operation of national data and cyberinfrastructure systems and services. It also describes systems that may interact with or make use of other existing systems and services. This supports the importance of integrating and accessing research information across infrastructure rather than assuming all research data exists in a single location. NSF - U.S. National Science Foundation
Source: NSF IDSS program
However, that NSF research call does not prove that my exact example of an unavailable repository causes a researcher to miss a particular dataset. That is an important distinction. NSF establishes the importance of shared research-data systems, while my project still needs to demonstrate the specific discovery failures I am studying.
Second, W3C's DCAT documentation establishes that metadata from independent catalogs needs to be interoperable. DCAT is explicitly designed so metadata can be aggregated from multiple catalogs and so federated search across multiple sites is possible. DCAT 3 also includes metadata for modification dates and version relationships, which shows that catalog information and datasets can change over time. W3C
Source: W3C DCAT 3 specification
A third relevant technical source is the Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH). OAI-PMH defines a mechanism in which data providers expose structured metadata and service providers request and harvest that metadata. This provides evidence that collecting metadata from independent repositories into another service is an established technical approach rather than something invented only for this project. Open Archives Initiative
Source: Open Archives Initiative Protocol for Metadata Harvesting
At this point, I have not yet measured missing or outdated results myself. That is missing experimental evidence that I still need to produce.
My current assumptions are that a live search will lose results when a repository containing a matching dataset is unavailable, and that a central catalog can return stale information when its copy has not yet been refreshed after the original repository changes. These are reasonable hypotheses based on the architectures, but they will be treated as assumptions until I reproduce them in my experiment.
________________________________________
What solutions already exist?

The first existing approach is direct or federated search. Instead of maintaining one complete central copy, the search service contacts several catalogs when a user performs a query and combines the responses. DCAT supports this type of decentralized environment by providing a common vocabulary that makes federated queries across catalogs possible. W3C
A major strength of this approach is freshness. If Repository C has just changed its metadata and is currently available, a live request can receive the new information without waiting for a central catalog to synchronize.
Its limitation is availability. If Repository C cannot be contacted when the search occurs, its datasets may not appear in the combined result. The search system is therefore affected by the current condition of each participating repository.
The second approach is an aggregated or central catalog. Metadata is copied or harvested from several repositories and stored in one searchable location. OAI-PMH is one example of an existing protocol that allows service providers to harvest structured metadata from data-provider repositories. Open Archives Initiative
A central catalog has an important availability advantage. If Repository C becomes temporarily unavailable after its metadata has already been collected, the catalog can still return the information it previously stored.
The weakness is freshness. If the original repository changes after synchronization, the central copy may remain outdated until the next refresh.

The comparison for my project can therefore be summarized as follows:

       |Approach|	                                       |Main Strength|	                                                  |Main Limitation|
| Direct/federated search	 |  | Can receive current metadata directly from available repositories	 |   | Results may be missing when a repository is unavailable |
|--------------------------|  |--------------------------------------------------------------------|   |-------------------------------------------------------- |
|Central/aggregated catalog|	|Previously harvested metadata can remain searchable during an outage|	 |Copied metadata can become stale between synchronizations|

Neither approach is automatically better. The useful solution may depend on how frequently repository metadata changes, how often repositories become unavailable, and how much staleness users can tolerate.
________________________________________
What is the most important thing you still do not know?

The most important unanswered question is:
How current does a central catalog need to be for researchers to reliably receive useful search results?
This question affects the design because refreshing constantly would reduce the amount of outdated metadata, but it would also require more frequent communication with the repositories. Refreshing less often would reduce synchronization activity but increase the period during which copied information could become stale.
I plan to investigate this with a controlled experiment using three mock repositories. I will create a known set of dataset descriptions and a query whose correct result is known in advance. First, I will run both approaches with all repositories online and current. This will provide the baseline.
I will then make the repository containing the matching dataset unavailable. I will record whether each approach still returns the expected result. After that, I will restore the repository but change the metadata while leaving the central catalog unchanged. I will then measure whether each approach returns the newest information or an older version.
The main measurements will be the number of missing results and the number of outdated results. I may also vary how long the simulated central catalog waits between updates. The experiment will therefore produce observable evidence rather than relying on an assumption that one architecture is better.
If even moderately delayed synchronization produces many incorrect results, the design would need frequent updates or live verification. If copied metadata remains useful for longer periods and handles outages better, a central catalog may offer a useful reliability advantage.
________________________________________
My Individual Scope

My project will intentionally use a small scope so that it can be completed and evaluated by one student.
I will create three mock research-data repositories containing a small number of dataset descriptions. I will use one consistent metadata format based on fields relevant to DCAT, such as dataset identifier, title, description, keywords, source, version, and modification date. I will not store or process large real scientific datasets because my problem is about dataset discovery and metadata, not scientific data analysis.
I will compare two approaches: a direct search that requests metadata from each repository and a central catalog that stores previously collected metadata. I will study two controlled failures: one repository becoming unavailable and one repository changing its metadata before the central catalog has refreshed.
I expect to implement the experiment using a small software simulation, most likely in Python, with JSON or another simple representation for the repository records. I do not plan to create a production-scale search engine, connect to hundreds of real repositories, or solve every problem involved in research-data discovery.
One possible solution direction is a central metadata catalog that records both the dataset information and the time when it was last synchronized. A later version could attempt to verify information against the original repository when that repository is available and warn users when cached information may be old. This is only a possible direction at this stage; my experiment needs to show whether it is actually useful before I treat it as a solution.
The project is manageable because the number of repositories, queries, metadata records, failures, and measurements is deliberately limited. The goal is not to prove that one architecture is universally better. The goal is to experimentally understand the tradeoff between freshness and availability in a small distributed dataset-discovery system.

