# A08: Discovery Across Independent Research Data Repositories

**Raed Jaber**  
**CSC 59866 – Senior Project I**  
**Professor Kurt Brown**  
**October 2026**

---

## What problem are you investigating?

The problem I am investigating is what a federated disaster-data search system should do when one of the independent archives it depends on is slow or unavailable.

I narrowed this problem using National Science Foundation (NSF) Award #2609535, **“AI-Driven National Synthesis Hub for Convergent Disaster Research and Intelligence.”** The award describes planning for DISCAT 2.0, a national artificial-intelligence-enabled disaster research hub. One part of the proposed architecture is a **federated data layer** that connects existing disaster archives instead of assuming that all information is stored in one database.

https://www.nsf.gov/awardsearch/show-award?AWD_ID=2609535

For my project, the important part is the federated data layer rather than the entire artificial intelligence system. A federated system can search information from several independent sources while allowing those sources to remain separate.

For example, I can model three disaster-data archives:

- **Archive A:** engineering and infrastructure damage information
- **Archive B:** evacuation and social-science information
- **Archive C:** emergency-response information

A researcher or emergency-management user could submit a query such as:

> “What were the infrastructure and evacuation impacts of Hurricane X?”

Under normal conditions, the search system sends the request to all three archives. Each archive responds, and the system combines those results for the user.

The problem occurs when one archive does not respond normally. For example, Archive B may have a very slow response or may be completely unavailable because of a network or service failure.

At that point, the search system has to make a decision.

One option is to continue waiting for Archive B so that the final result has a better chance of containing all of the relevant information. The disadvantage is that the entire query may become slow because of one archive.

Another option is to stop waiting after a specified timeout and return the information that was successfully received from Archives A and C. This makes the response faster, but the user may receive incomplete information because the evacuation evidence stored in Archive B is missing.

A third possible approach is to use previously collected or cached information from Archive B when the live archive is unavailable. This could improve completeness, but the cached information may not be current.

The **World Wide Web Consortium (W3C) Data Catalog Vocabulary (DCAT)** is relevant because it provides a common model for describing datasets and data services across catalogs. DCAT supports both aggregation of metadata from multiple catalogs and federated search across catalogs located at different sites.

https://www.w3.org/TR/vocab-dcat-3/

My project is therefore focused on one specific condition: **one archive becoming slow or unavailable during a federated disaster-data query**. I am not investigating every possible failure in DISCAT 2.0.

The main problem is deciding how long the search should wait and whether returning partial or previously collected information provides a better result than waiting indefinitely for every archive.

---

## Who or what is affected by it?

The main users affected are disaster researchers, emergency managers, policy stakeholders, and other people who need information from multiple disaster-data sources.

The NSF DISCAT 2.0 award specifically describes a system intended to connect existing disaster archives and make their information useful for science and decision-making. The planned system is meant to support research and decisions related to disasters such as hurricanes, wildfires, floods, earthquakes, and other catastrophic events.

https://www.nsf.gov/awardsearch/show-award?AWD_ID=2609535

The organizations that maintain the individual archives are also part of the system. Because the archives remain independent, the search system cannot assume that every archive will always have the same performance or availability.

Consider the example query about the infrastructure and evacuation impacts of a hurricane.

Archive A may quickly return infrastructure-damage information. Archive C may return emergency-response records. If Archive B is slow or unavailable, however, the evacuation information may not arrive.

If the system waits for Archive B for a long time, the user may eventually receive a more complete answer, but the response may take too long.

If the system stops waiting quickly, the user receives information sooner, but important evidence may be missing.

This matters because a result can appear successful while still being incomplete. A user may see infrastructure and emergency-response information without realizing that the evacuation archive did not respond.

A cached fallback creates another concern. Previously stored Archive B information could allow the user to see evacuation-related results even during an outage, but the system needs to identify that those results did not come from the current live archive.

The consequences I am focusing on are therefore:

- increased query response time,
- missing results,
- incomplete information,
- and the possible use of older cached information.

I am not trying to determine whether these failures directly cause incorrect disaster-management decisions. That would require a much larger study involving real users and operational disaster systems. My project is limited to measuring the technical behavior of a small simulated discovery system.

---

## What evidence do you currently have that it is a real problem?

The strongest evidence for the broader research need comes from NSF Award #2609535.

The award describes DISCAT 2.0 as a next-generation disaster-data infrastructure with a federated data layer. It also states that the planning project will consider Application Programming Interface (API) standards, containerization, security, governance, scenario-based workflow testing, latency testing, and data audits.

https://www.nsf.gov/awardsearch/show-award?AWD_ID=2609535

The mention of a federated data layer establishes that independent disaster-data sources are part of the planned architecture. The mention of latency testing is especially relevant to my narrower project because I am interested in what happens when one source responds much more slowly than the others.

However, this award does **not** prove that my exact three-archive scenario has occurred or that a particular timeout value is currently causing a failure in DISCAT 2.0. The NSF project is itself a planning project. My example is a controlled student experiment inspired by one technical issue inside that larger project.

The NSF **Integrated Data Systems and Services (IDSS)** program also establishes a broader need for research-data infrastructure and services that can support data-intensive science.

https://www.nsf.gov/funding/opportunities/idss-integrated-data-systems-services

A second technical source is W3C's DCAT Version 3 specification. DCAT was created to improve interoperability between data catalogs. It allows datasets and data services to be described using a common vocabulary and specifically supports aggregation and federated discovery across catalogs.

https://www.w3.org/TR/vocab-dcat-3/

This establishes that searching and combining metadata from independent catalogs is an existing technical problem with a standardized approach to describing the information.

A third useful source is the **Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH)**. OAI-PMH allows one service to harvest metadata exposed by another repository. This provides an established example of collecting metadata from independent sources so that it can later be accessed through another service.

https://www.openarchives.org/pmh/

This is relevant to my cached or locally stored fallback idea because it demonstrates that metadata does not always have to be retrieved directly from its original repository at query time.

At this stage, I have **not yet performed my own experiment**.

I have not measured query times, result completeness, or the behavior of a slow archive. Those measurements still need to be produced.

My current assumptions are:

1. A single slow archive can increase the total response time if the search waits for every source.
2. A short timeout can reduce response time but may result in missing information.
3. Previously collected information could improve result completeness during an outage, but it may be older than information from a live source.

These are hypotheses that my experiment will test rather than results that I am claiming have already been proven.

---

## What solutions already exist?

Two existing architectural ideas are relevant to this problem.

### Approach 1: Live Federated Search

The first approach is to query independent archives directly.

DCAT supports a decentralized environment in which different catalogs use a common vocabulary, making federated search across multiple sites possible.

https://www.w3.org/TR/vocab-dcat-3/

In my experiment, a live federated query would send the same search request to Archives A, B, and C.

The main advantage is that successful responses come directly from the current archives. There is no separate copied catalog that must first be synchronized.

The problem is that the search now depends on the behavior of several independent systems.

If Archive A responds in 0.5 seconds, Archive C responds in 0.8 seconds, but Archive B takes five seconds, a system that waits for all three responses could make the entire user query take around five seconds even though two archives were ready much earlier.

If B does not respond at all, the system needs some rule for deciding when to stop waiting.

A timeout can solve the waiting problem, but then the system may return only A and C's results.

### Approach 2: Previously Harvested or Cached Metadata

The second approach is to maintain previously collected information from the archives.

OAI-PMH demonstrates an established architecture in which service providers harvest metadata exposed by independent repositories.

https://www.openarchives.org/pmh/

Applied to my experiment, the system could previously collect some of Archive B's metadata. If B becomes unavailable during a live query, the search could return the information from Archives A and C along with previously collected information from B.

This has an availability advantage because information from B does not completely disappear.

The limitation is freshness. The stored information may not be the latest version available from Archive B.

The system would therefore need to distinguish between live and cached results instead of presenting all results as if they came from the same source at the same time.

### Comparison of Approaches

| Approach | Main Strength | Main Limitation |
|---|---|---|
| **Wait for live federated responses** | Results come directly from currently available archives | One slow or unavailable archive can delay the query |
| **Timeout and return partial live results** | User receives available information faster | Relevant information from the slow archive can be missing |
| **Timeout with cached/harvested fallback** | Can preserve some information from an unavailable archive | Cached information may be older than the current source |

I do not currently know which policy provides the best balance.

For example, waiting five seconds might produce complete information but unacceptable latency. Waiting one second could provide a much faster result but remove too much information. A cached fallback may improve completeness, but the age of the cached information must also be considered.

Determining that tradeoff is the purpose of the experiment.

---

## What is the most important thing you still do not know?

The most important question I still need to answer is:

> **How long should a federated disaster-data search wait for a slow archive before returning partial results or using cached information?**

This question directly affects both response time and result completeness.

To investigate it, I will create three mock disaster-data archives containing a small, known collection of records.

I will create one search query for which I already know the expected results.

First, I will run a normal baseline experiment where all three archives respond quickly.

For example:

- Archive A responds normally.
- Archive B responds normally.
- Archive C responds normally.

I will record the total query time and confirm that all expected results were returned.

Next, I will artificially delay Archive B.

I can test delays such as:

- 0.5 seconds
- 1 second
- 2 seconds
- 5 seconds

I will then compare different timeout policies.

For example, the search could stop waiting after one second, two seconds, or five seconds.

For each test, I will record:

1. **Query latency** – how long the search took.
2. **Result completeness** – how many expected records were returned.
3. **Missing results** – how many expected results were unavailable because Archive B did not respond before the timeout.

I may also test a cached fallback. In that case, I will record how many results came from live archives and how many came from previously stored Archive B information.

The important point is that I will not choose a timeout because it simply seems reasonable. I want the experiment to show the tradeoff.

For example, a very short timeout may reduce response time significantly but remove too many results. A longer timeout may improve completeness without adding enough delay to matter. The measurements will help determine which direction is worth using in the later design document.

---

## My Individual Scope

My project will focus on one small part of the larger DISCAT 2.0 idea.

I will model **three mock disaster-data archives**:

- one containing infrastructure-related information,
- one containing evacuation or social-science information,
- and one containing emergency-response information.

I will use a small amount of synthetic or invented test data so that I know exactly which records should appear for the selected query.

I will use **one main disaster-related search query** and one controlled failure condition: Archive B becoming slow or unavailable.

I expect to implement the experiment using **Python**. The mock archive records may be represented using **JavaScript Object Notation (JSON)** files or another simple structured format.

The main comparison will be between:

1. waiting for live archive responses,
2. returning partial results after a timeout,
3. and, if manageable, returning cached information after the timeout.

The main measurements will be:

- total query latency,
- number or percentage of expected results returned,
- missing results,
- and, for the cached approach, the number of results that came from previously stored information.

I will not implement DISCAT 2.0's artificial intelligence agents, knowledge graphs, complete national federated data layer, security system, governance model, or user-personalization system.

Those are parts of the larger NSF-funded project but are outside my individual scope.

My possible solution direction is a federated search policy that uses a limited timeout for each archive. If an archive does not respond before the timeout, the system could return the available live results and clearly indicate which archive failed. If previously collected information is available, the system could optionally include that information while labeling it as cached.

This is only a possible design direction. I will not treat it as the correct solution until the experiment provides evidence about latency and result completeness.

The scope is manageable for one student because I am limiting the project to three mock archives, one query, one controlled failure, a few timeout values, and a small number of measurable outcomes.

The goal is to answer one narrow question inside A08: **how a federated disaster-data search should respond when one independent archive does not answer on time.**

---

## References

**National Science Foundation.** *Award Abstract #2609535: Category III: AI-Driven National Synthesis Hub for Convergent Disaster Research and Intelligence.*  
https://www.nsf.gov/awardsearch/show-award?AWD_ID=2609535

**National Science Foundation.** *Integrated Data Systems and Services (IDSS).*  
https://www.nsf.gov/funding/opportunities/idss-integrated-data-systems-services

**World Wide Web Consortium (W3C).** *Data Catalog Vocabulary (DCAT) Version 3.*  
https://www.w3.org/TR/vocab-dcat-3/

**Open Archives Initiative.** *Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH).*  
https://www.openarchives.org/pmh/
