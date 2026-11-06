A08: Plain-Language Search Across Disaster Data Archives
Raed Jaber
CSC 59866 – Senior Project I
Professor Kurt Brown
NSF Project 10 – Award 2609535
1. What problem are you investigating?
The problem I am investigating is how to make disaster-related research information easier to find when it is stored across different independent archives.

This project is based on NSF Project 10 from the course PDF, “Category III: AI-Driven National Synthesis Hub for Convergent Disaster Research and Intelligence.” The NSF project plans DISCAT 2.0, a next-generation disaster data infrastructure that connects existing disaster archives. The project also says that users should be able to ask questions in plain language and receive useful information from those connected sources.

https://www.nsf.gov/awardsearch/show-award?AWD_ID=2609535

The full NSF project is much larger than what I can build as one student. It includes artificial intelligence agents, knowledge graphs, security, governance, user roles, and a federated data layer.

For my individual project, I am focusing on one smaller product inside that larger idea.

My goal is to build a plain-language disaster archive search application.

A user would type a normal question into a search box, such as:
What information is available about Hurricane Sandy?

The application would search across a small number of separate disaster-data sources and return the relevant results in one place.

The main problem is that disaster information may be stored in different repositories, each with its own data and organization. A user may need to search several different systems separately to find related information.

My product would provide one search interface that sends the user’s question to the connected sources, gathers the matching information, and presents the results together.

For example, I may use three simplified disaster-data sources. One source could contain disaster-event information, another could contain research or report metadata, and another could contain response-related information.

Each result would clearly show which source it came from.

The application should also handle a source becoming unavailable. If one connected source cannot respond, the entire product should not fail. The application should still show the information it can retrieve from the other sources and clearly tell the user which source was unavailable.

This keeps the project connected to A08 because A08 focuses on discovery across independent research-data repositories. My product is a specific disaster-data version of that problem.
2. Who or what is affected by it?
The main users affected by this problem are disaster researchers, emergency managers, and other people who need to find information from disaster archives.

The NSF Project 10 abstract specifically mentions researchers, emergency managers, and policy stakeholders as users involved in the planned DISCAT 2.0 system.

https://www.nsf.gov/awardsearch/show-award?AWD_ID=2609535

A disaster researcher may need information that is stored in more than one archive. For example, one repository may contain information about a disaster event, while another may contain reports or research related to that same event.

If those repositories are separate, the user may have to visit different systems and perform several different searches.

That creates a discovery problem.

The user has to know which repositories exist, where to search, and how each repository organizes its information.

A plain-language search tool could reduce that difficulty by giving the user one place to ask a question.

Instead of manually searching several different archives, the user could type a normal question into one interface and receive combined results.

The independent repositories are also part of the problem because they may not all behave the same way.

One source may be available while another is temporarily unavailable. One source may also describe its datasets or records differently from another source.

My product would try to make the user experience more consistent by presenting the results in one format and showing the source of each result.

If one source is unavailable, the application would show that status instead of failing silently.

The main effect on the user is therefore not only search convenience. It is also clarity.

The user should be able to see:
- what information was found,
- which source provided it,
- and whether one of the connected sources could not be reached.
3. What evidence do you currently have that it is a real problem?
The strongest evidence for the broader problem comes from NSF Project 10.

The NSF abstract explains that the project will design a national artificial-intelligence-enabled hub that connects existing disaster archives and turns them into a more active resource for science and decision-making.

It also specifically says that the planned system should make it easier to ask questions in plain language and should use a federated data layer.

https://www.nsf.gov/awardsearch/show-award?AWD_ID=2609535

This supports the larger problem that disaster-related information exists across separate archives and that there is value in making that information easier to discover.

The NSF project also shows that the problem is important enough to support a larger research effort around disaster data infrastructure.

However, the NSF award does not prove that my exact small product already exists or that my exact search interface is the correct solution.

My product is a smaller implementation direction that comes from one specific part of the NSF project.

A second useful source is the World Wide Web Consortium (W3C) Data Catalog Vocabulary (DCAT) Version 3.

DCAT provides a standard vocabulary for describing datasets and data services. Its purpose is to improve interoperability and discovery across data catalogs.

https://www.w3.org/TR/vocab-dcat-3/

This is relevant to my product because information from different sources needs to be represented in a consistent way before it can be displayed together in one search interface.

For example, my application may use a common structure with fields such as:
- title,
- description,
- source,
- disaster type,
- date,
- and access link.
A third related source is the Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH).

OAI-PMH is an established protocol that allows metadata to be collected from repositories.

https://www.openarchives.org/pmh/

This shows another existing approach for working with information that is distributed across independent repositories.

These sources support the general problem of data discovery across multiple repositories.

What they do not prove is exactly how my small application should be designed. That is what I still need to work out through the design process for the project.
4. What solutions already exist?
There are already several approaches related to this problem.

My project is not claiming that searching multiple repositories is a completely new idea. Instead, I am building a small product using ideas that already exist.
Federated Search
One approach is federated search.

In a federated search system, the data sources remain separate. The search system sends a request to several sources and combines the responses for the user.

This fits my project because I do not need to copy every disaster archive into one large database.

The user can search from one interface while the connected sources remain independent.

The strength of federated search is that it gives the user one place to search.

The limitation is that the application depends on multiple independent systems. If one source is unavailable, the application still needs to decide how to present the results from the sources that are available.
Common Metadata Structure
Another approach is to use a common structure for describing records from different sources.

DCAT is relevant because it provides a standard vocabulary for describing datasets and data services.

https://www.w3.org/TR/vocab-dcat-3/

For my project, I may not implement every part of DCAT, but I can use the same idea of creating a common structure for all search results.

For example:
Title
Description
Source
Disaster Type
Date
Link
This would make it easier to display information from different sources in one results page.
Metadata Harvesting
OAI-PMH provides another approach where one service collects metadata from repositories.

https://www.openarchives.org/pmh/

Instead of asking every repository for information at the exact moment of each search, a system can collect metadata and make it available through another service.

The advantage is that search can be faster and less dependent on every source being online at the same moment.

The limitation is that previously collected information may become outdated.
Comparison
Approach	Strength	Limitation
Federated search	Searches independent sources from one interface	Depends on the connected sources being available
Common metadata structure	Makes information from different sources easier to combine	Different repositories may use different formats
Metadata harvesting	Can make collected information easier to search	Stored information may become outdated


For my product, the main direction will be a small federated search interface with a common result format.

If one source is unavailable, the product should still display the information returned by the other connected sources.
5. What is the most important thing you still do not know?
The most important thing I still do not know is:

What is the best way to turn a plain-language disaster question into useful combined results from several independent disaster-data sources?

The NSF project says that DISCAT 2.0 should make it easier for users to ask questions in plain language.

https://www.nsf.gov/awardsearch/show-award?AWD_ID=2609535

For my smaller project, I still need to decide how much natural-language processing is necessary.

For example, if a user types:
What information is available about Hurricane Sandy?

the application needs to identify the important search terms and use them to search the connected sources.

A simple first version may identify terms such as:
- Hurricane Sandy
- hurricane
- location
- date
- disaster type
I still need to decide how simple or advanced this part of the system should be.

I also need to decide exactly which fields from different sources should be converted into my common result format.

Another design question is how the interface should display results when one source is unavailable.

The product should make it clear that some information may be missing, rather than making the user think that the returned results represent every connected source.

These design decisions will affect how useful and understandable the final product is.
6. Your Individual Scope
My individual project will be a small plain-language disaster archive search web application.

The product will be inspired by NSF Project 10 and its goal of making it easier to ask questions across existing disaster archives.

My project will not attempt to build the full DISCAT 2.0 system.

The planned product will include:
- one web-based search interface,
- plain-language user questions,
- two or three simplified disaster-data sources,
- a common format for search results,
- combined results from the connected sources,
- source labels for every result,
- and a clear status when one source is unavailable.
A user will enter a question such as:
What information is available about Hurricane Sandy?

The application will process the question, search the connected sources, and display the matching results on one page.

The product will show the source of each result so that the user knows where the information came from.

If one source cannot be reached, the application should continue displaying results from the other available sources and show that the unavailable source could not be searched.

The project will use small or simplified data sources so that it remains manageable for one student.

Possible implementation tools include:
- Python or JavaScript for the backend,
- a simple web frontend,
- JSON or API-based data sources,
- and a small common metadata structure for the search results.
I am excluding the larger parts of DISCAT 2.0, including:
- multiple AI agents,
- full knowledge graphs,
- national-scale infrastructure,
- advanced security and governance,
- large-scale disaster prediction,
- and a complete production-level federated data platform.
Those features are outside the scope of my individual project.

The final product I am trying to build is therefore:

A small web application that lets a user ask a plain-language disaster-related question and receive combined, source-labeled results from several independent disaster-data sources.

This keeps the project specific, manageable, connected to A08, and directly based on one capability described in NSF Project 10.
References
National Science Foundation.
Category III: AI-Driven National Synthesis Hub for Convergent Disaster Research and Intelligence.
NSF Award 2609535.
https://www.nsf.gov/awardsearch/show-award?AWD_ID=2609535

World Wide Web Consortium (W3C).
Data Catalog Vocabulary (DCAT) Version 3.
https://www.w3.org/TR/vocab-dcat-3/

Open Archives Initiative.
Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH).
https://www.openarchives.org/pmh/
