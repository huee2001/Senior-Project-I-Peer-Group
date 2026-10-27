A08: Discovery Across Independent Research Data Repositories

Raed Jaber
CSC 59866 – Senior Project I
Professor Kurt Brown
October 2026

---

1. What problem are you investigating?

The problem I am investigating is how to make disaster-related research data easier to discover when the information is stored across separate and independent repositories.

I narrowed this problem using National Science Foundation (NSF) Award #2609535, “Category III: AI-Driven National Synthesis Hub for Convergent Disaster Research and Intelligence.” The award describes planning for DISCAT 2.0, a larger disaster-research system that would connect information from existing disaster archives through a federated data layer.

https://www.nsf.gov/awardsearch/show-award?AWD_ID=2609535

For my project, I am not trying to build the entire DISCAT 2.0 system. Instead, I am focusing on a smaller product that addresses one part of this problem.

My goal is to build a federated disaster-data discovery application. The application would allow a user to search multiple independent disaster-data sources from one interface instead of searching every repository separately.

For example, the product could connect three simplified data sources:

- Archive A: infrastructure and building damage information
- Archive B: evacuation and social-science information
- Archive C: emergency-response information

A user could search for something such as “Hurricane Sandy evacuation.” The application would search the connected sources and combine the matching information into one results page.

Each result would clearly identify which source it came from.

The main difficulty I want the product to handle is when one of those independent sources is unavailable or does not respond correctly.

For example, Archive A and Archive C may be working normally, while Archive B is unavailable. I do not want the entire search application to fail because one source cannot be reached.

Instead, the application should still return useful results from the available sources and clearly tell the user that Archive B is unavailable.

If previously retrieved information from Archive B is available, another possible feature is to display that cached information while clearly identifying it as previously stored information instead of a current live result.

The World Wide Web Consortium (W3C) Data Catalog Vocabulary, or DCAT, is relevant to this problem because it provides a standard way to describe datasets and data services across different catalogs.

https://www.w3.org/TR/vocab-dcat-3/

My project is therefore not about building a national disaster database or replacing existing repositories. It is about building a smaller discovery product that can work across several independent sources and continue to provide useful information when one source has a problem.

---

2. Who or what is affected by it?

The main users affected by this problem are researchers and other people who need to find disaster-related information across multiple sources.

A researcher studying a hurricane, for example, may need infrastructure damage information, evacuation information, and emergency-response information. Those types of information may not all be stored in the same repository.

If users have to search each repository separately, discovering information becomes more difficult and time-consuming.

The NSF DISCAT 2.0 project is attempting to address a much larger version of this problem by connecting existing disaster archives and making their information easier to use for research and decision-making.

https://www.nsf.gov/awardsearch/show-award?AWD_ID=2609535

The individual repositories are also affected because they remain independent systems. A discovery application cannot assume that every repository will always be available at the same time.

For example, imagine that a user searches for Hurricane Sandy.

Archive A may return infrastructure damage information.

Archive B may normally contain evacuation information.

Archive C may contain emergency-response information.

If Archive B is unavailable, the application should still continue working.

My product would continue showing the results from Archives A and C while warning the user that Archive B could not be reached.

This is important because users should know when their search results may be incomplete.

The product is therefore focused on making information from separate sources easier to discover while also keeping the search useful when one source is unavailable.

---

3. What evidence do you currently have that it is a real problem?

The main evidence for the larger problem comes from NSF Award #2609535.

The NSF project describes DISCAT 2.0 as a next-generation disaster-data infrastructure that would build on existing disaster archives. The proposed system includes a federated data layer and is designed to make disaster information easier to access and combine.

https://www.nsf.gov/awardsearch/show-award?AWD_ID=2609535

This supports the idea that disaster-related information is distributed across existing sources and that connecting those sources is an important technical problem.

However, the NSF award does not say that my exact three-source product already exists or that my exact example is a documented failure.

My three-source design is a smaller version of the larger problem so that the project is manageable for one student.

A second source is the W3C Data Catalog Vocabulary (DCAT) Version 3 specification.

DCAT was developed to improve interoperability between data catalogs. It provides a common model for describing datasets and data services and supports discovery across different catalogs.

https://www.w3.org/TR/vocab-dcat-3/

Another related approach is the Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH).

OAI-PMH allows one system to collect metadata from independent repositories.

https://www.openarchives.org/pmh/

This is relevant to the cached-information feature of my product. Information that has already been collected from a repository could potentially remain available even when the original repository cannot currently be reached.

These sources show that distributed repositories, federated discovery, and metadata sharing are real technical areas.

What I still need to determine is how I should combine these ideas into a small and usable product.

---

4. What solutions already exist?

There are already several approaches related to this problem. My goal is not to claim that I invented federated search, caching, or failure handling.

Federated Search

One approach is federated search.

In a federated search system, the sources remain independent instead of being combined into one large database. A search system sends requests to multiple sources and then combines their responses.

This fits my product because my three disaster-data sources can remain separate while the user interacts with only one search interface.

The advantage is that the user does not need to manually search every repository.

The limitation is that the application depends on several independent sources. If one source is unavailable, the application needs to decide how to present the results that are still available.

Common Dataset Descriptions

Another existing approach is DCAT.

DCAT provides a standard vocabulary for describing datasets and data services.

https://www.w3.org/TR/vocab-dcat-3/

For my product, a simplified common metadata structure could include fields such as:

- dataset title
- description
- source
- category
- disaster name
- date
- last updated time

Using a consistent structure would make it easier for the application to display results from different sources together.

Cached or Previously Collected Information

Another approach is storing previously retrieved information.

OAI-PMH is an example of an established method for harvesting metadata from repositories.

https://www.openarchives.org/pmh/

A similar idea could be useful in my application.

If Archive B was available earlier and the application stored some of its dataset information, the application could still display that information when B becomes unavailable.

The disadvantage is that previously stored information may not be current.

Because of this, cached results should be clearly labeled so that the user knows they are not live results.

Comparison

Approach| Strength| Limitation
Federated search| Searches several independent sources from one place| One source may become unavailable
Common metadata structure| Makes results from different sources easier to combine| Sources may describe information differently
Partial results| Application can still work when one source fails| User may receive incomplete information
Cached information| Can preserve information from an unavailable source| Information may be outdated

These approaches give me possible components for the product, but I still need to decide how they should work together in a simple interface.

---

5. What is the most important thing you still do not know?

The main thing I still need to determine is:

What is the best way for my product to continue giving useful and understandable search results when one connected disaster-data source is unavailable?

I already know that techniques such as federated search, partial results, and caching exist.

The unknown for my project is how I should combine those ideas into a product that makes the status of the information clear to the user.

For example, if Archive B cannot be reached, the application could still display results from Archives A and C.

The interface could show:

- Archive A – Available
- Archive B – Currently unavailable
- Archive C – Available

The results would also show their original source.

If cached Archive B information exists, the product could display it separately with a label such as:

Cached result – last retrieved October 20

This is important because I do not want users to confuse older cached information with current live information.

The goal is for the application to continue functioning when one source has a problem while also being clear about what information may be missing or outdated.

---

6. My Individual Scope

My individual project will be a small federated disaster-data discovery web application.

The application will have one main search interface.

For the initial version, I plan to work with three simplified disaster-data sources:

1. infrastructure and damage data
2. evacuation or social-science data
3. emergency-response data

The sources may use small sample datasets or simplified repository services so that the project remains manageable for one student.

A user will enter a search term, such as a hurricane name or disaster topic.

The application will search across the connected sources and display the matching information together on one results page.

Each result will show which repository it came from.

The product will also include source-status information.

If one source cannot be reached, the entire application should not stop working. The application should continue displaying information from the available sources while clearly showing which source is unavailable.

If the project remains manageable, I would also like to include a cached-information feature.

Previously retrieved information from an unavailable source could still appear, but it would be clearly labeled as cached and include information about when it was last retrieved.

The main product features would be:

- one search interface
- three independent disaster-data sources
- combined search results
- source labels
- repository availability/status information
- partial results when one source is unavailable
- possibly clearly labeled cached results

I am not building the complete DISCAT 2.0 system.

I am also not building artificial intelligence agents, a national disaster database, a knowledge graph, disaster prediction software, or a complete production-scale distributed architecture.

Those features are outside the scope of one student project.

The purpose of my project is to build a smaller working product that demonstrates how disaster-related information from independent repositories can be discovered through one interface while still providing useful and transparent results when one source is unavailable.

This keeps the project connected to A08 while giving me a clear product that I can continue designing during Senior Project I and implement as a working system.

---

References

National Science Foundation.
Award Abstract #2609535: Category III: AI-Driven National Synthesis Hub for Convergent Disaster Research and Intelligence.
https://www.nsf.gov/awardsearch/show-award?AWD_ID=2609535

World Wide Web Consortium (W3C).
Data Catalog Vocabulary (DCAT) Version 3.
https://www.w3.org/TR/vocab-dcat-3/

Open Archives Initiative.
Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH).
https://www.openarchives.org/pmh/
