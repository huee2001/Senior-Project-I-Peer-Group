Plain-Language Disaster Archive Search Design

Author: Raed Jaber
Course: CSC 59866
Selected project and option: A08 — Plain-Language Search Across Disaster Data Archives, based on NSF Project 10 (Award 2609535)
Current assignment: 2 — Requirements and possible solutions
Friday commit deadline: November 13, 2026, at 11:59 p.m. New York time
Monday presentation: November 16, 2026, at 6:30 p.m. New York time
Last updated: November 13, 2026
Document status: Revised

Progress note

For Assignment 2, I revised the project boundary and turned the search idea into observable requirements. The supported input is now limited to event-focused English questions that name a disaster event, rather than arbitrary natural-language questions. I defined four functional requirements for question processing, searching the configured sources, combining source-labeled results, and continuing when one source is unavailable. I also added a correctness rule for source attribution and a proposed response-time target that will be measured later rather than treated as a result. For possible solutions, I am comparing a simple rule-based keyword/event-name approach with a lightweight named-entity approach using spaCy. I have not selected the final approach yet. My main unresolved issue is whether the simpler baseline is sufficient for the supported question set. The next step is a small feasibility check before Assignment 3.

Contents

* 1 Problem research and scope
* 2 Requirements and system specification
* 3 Alternatives and selected solution
* 4 Architectural design
* 5 Component design and interfaces
* 6 Data structure design
* 7 Algorithm design and execution
* 8 Failures and security
* 9 Implementation and feasibility
* 10 Testing and verification
* 11 Operation maintenance and future work
* 12 Revision history and references

1 Problem research and scope

Problem and affected people

The primary user for this project is a disaster researcher who needs to find information that may be stored across separate disaster-data archives.

The larger NSF Project 10 also identifies emergency managers and policy stakeholders as intended users of DISCAT 2.0, but the first prototype focuses on the researcher’s search task.

NSF Award 2609535 describes DISCAT 2.0 as a planned system that connects existing disaster archives, makes it easier to ask questions in plain language, and includes a federated data layer.

My project takes one small capability from that larger idea: an event-focused question should return useful, source-labeled results from more than one disaster-data source.

https://www.nsf.gov/awardsearch/show-award?AWD_ID=2609535

Current workflow

Assumption to verify: A disaster researcher who needs information from several independent archives may currently have to identify relevant sources, open them separately, adapt the search to each source, inspect results in different formats, and combine the useful findings manually.

For this design, I am not claiming that every disaster researcher follows exactly this workflow.

The NSF project establishes the broader need to connect existing disaster archives and make them easier to query. The exact current workflow for my intended user still needs additional evidence.

A simplified current workflow is:

1. The researcher identifies a disaster event and information need.
2. The researcher decides which archives may contain useful material.
3. The researcher searches each archive separately.
4. The researcher reviews results from the different sources.
5. The researcher manually connects the relevant information.

The difficulty occurs mainly in steps 2–5 because the sources are separate and may organize or describe their information differently.

Concrete scenario

A disaster researcher wants to know what information is available about Hurricane Sandy.

A representative supported question is:

What information is available about Hurricane Sandy?

In the assumed current workflow, the researcher may need to search several archives separately and then compare the results.

In the proposed prototype, the researcher enters the question once. The program identifies Hurricane Sandy as the event being searched, queries two or three simplified sources, and displays matching results together.

Every result shows its source.

The first prototype does not claim to understand arbitrary natural-language questions.

Its supported input is deliberately limited to event-focused English questions that name one disaster event.

The selected adverse case is that one source is unavailable while the other sources are still available.

The proposed behavior is to return the results received from available sources and clearly identify the source that could not be searched.

Stakeholders and needs

Stakeholder	Main need in this project	Current concern or difficulty
Disaster researcher	Find related disaster information without repeating the same search across several sources	Relevant information may be separated across independent archives
Emergency manager or policy stakeholder	Understand where returned information came from	Results need clear source attribution; this is a secondary user for the first prototype
Data repository or archive owner	Keep its information identifiable as coming from that source	Combined results should not hide or change source attribution

Evidence and assumptions

Documented evidence: NSF Project 10 states that DISCAT 2.0 will connect existing disaster archives, make it easier to ask questions in plain language, and include a federated data layer.

This establishes the larger problem area and motivates the capability being narrowed for this project.

https://www.nsf.gov/awardsearch/show-award?AWD_ID=2609535

Existing approach: The World Wide Web Consortium’s Data Catalog Vocabulary (DCAT) Version 3 provides a standard model for describing datasets and data services.

DCAT helps explain how information from different catalogs can use a common structure for discovery.

https://www.w3.org/TR/vocab-dcat-3/

Assumption: Event-focused English questions that name one disaster event are a useful small input set for the first prototype. I have not yet validated this exact question format with an actual disaster researcher.

Assumption: Two or three simplified sources are enough to demonstrate the main discovery path during this six-week design period. This is a scope choice, not a claim about what a national system would require.

Six-week contribution

The six-week contribution is one small end-to-end capability:

A disaster researcher enters an event-focused plain-language question that names a disaster event. The prototype identifies the event, searches two or three simplified disaster-data sources, and returns one combined list of matching results with a source label for every result.

The normal case is that all configured sources respond.

The selected adverse case is that one source is unavailable.

The proposed behavior is to return results from the available sources and show a clear unavailable-source notice.

Semester II scope

The larger Semester II goal is to turn the six-week working path into a more complete disaster-data discovery product.

Possible additions include:

* connecting to more realistic or public disaster-data sources,
* supporting a wider range of questions,
* improving result ranking and filtering,
* improving source and provenance information,
* and refining unavailable-source handling based on what is learned from the first implementation.

These are future goals and are not claims about what the current prototype already implements.

Exclusions

The current project does not attempt to build the full DISCAT 2.0 system.

The following are outside the current six-week scope:

* a national-scale disaster-data platform,
* multiple autonomous AI agents,
* a complete disaster-science knowledge graph,
* arbitrary natural-language question answering,
* personalized results for every possible user role,
* production authentication and authorization,
* sensitive or private disaster data,
* disaster prediction,
* and production-scale reliability guarantees.

Workflow / context image

Figure 1. The project focuses on one search path. A disaster researcher asks an event-focused question, the prototype searches a few independent sources, and the user receives combined results with source labels. One source may be unavailable while the others still return results.

2 Requirements and system specification

The requirements below describe the proposed behavior of the six-week prototype.

They are not implementation results yet.

Initial requirements

ID	Required behavior and conditions	Acceptance check	Design and test reference
F1	When the user enters a supported event-focused English question that names one known disaster event, the system identifies the event to search.	Enter What information is available about Hurricane Sandy? and verify that the interpreted event is Hurricane Sandy.	Design and test references will be added as the project develops
F2	After identifying the event, the system searches every configured source that is available for records matching that event.	Use controlled source data containing matching and nonmatching records and verify that each available source is queried for the identified event.	To be connected to later architecture and tests
F3	The system combines matching records into one result list and shows the originating source for every displayed result.	Search for a seeded event with matches in more than one source and verify that the combined output contains the expected records and source labels.	To be connected to later data design and tests
F4	If one configured source is unavailable, the system still returns results from the sources that responded and clearly identifies the unavailable source.	Make one controlled source unavailable and verify that available-source results are shown with an unavailable-source notice.	Selected adverse case for later design and testing
C1	A displayed result must keep the correct source attribution. The system must not label a record as coming from a source that did not provide it, and must not present an unavailable source as successfully searched.	Seed each source with uniquely identifiable records, run a search, and compare every displayed source label and source status with the controlled input.	Correctness rule; later tests will reference C1
Q1	Proposed target: On the documented local prototype setup, at least 19 of 20 supported queries should produce a final displayed result or defined no-match outcome within 2 seconds when all configured sources are available.	Run 20 supported queries under the documented local workload and measure elapsed time from submission to final displayed outcome. Count late or unanswered queries as misses.	Proposed and unmeasured; baseline measurement will be recorded later

The two-second value in Q1 is an initial target for an interactive local prototype.

It is not an observed result.

A later baseline measurement may justify revising it.

Inputs and outputs

Ordinary example

Input

What information is available about Hurricane Sandy?

Interpreted event

Hurricane Sandy

Illustrative source records

Source A -> Hurricane Sandy event summary
Source B -> Hurricane Sandy research report
Source C -> Hurricane Katrina response report

Expected output

Results for Hurricane Sandy
- Hurricane Sandy event summary
  Source: Source A
- Hurricane Sandy research report
  Source: Source B

The Hurricane Katrina record should not appear because it does not match the requested event.

Unsuccessful input example

Input

What information is available?

The input does not name a disaster event.

The proposed result is a clear unsupported-input message such as:

Please name a disaster event to search.

The system should not invent an event or fabricate search results.

Unavailable-source example

For a supported question, if Source B cannot be reached, the proposed result is:

Results from Source A
Results from Source C
Source B: unavailable

The system should not claim that Source B was searched successfully.

Assumptions

Assumption	Why it is needed now	Planned check
Supported questions are in English and name one disaster event	Keeps the question-processing problem bounded	Define a small supported query set and check how each approach interprets it
The prototype uses two or three sources with structured metadata	Keeps the search path manageable for one student	Create or obtain small source fixtures before implementation depends on them
Each returned record can retain a source identifier	Needed for correctness rule C1	Seed unique source IDs and verify them in combined output
Public or synthetic data is sufficient for the prototype	Avoids private or sensitive disaster information	Record the exact data used before Assignment 5

Constraints

* The six-week prototype must be small enough to design and implement on the available development computer.
* The first version supports only a limited event-focused question set, not arbitrary question answering.
* The initial data sources may be simplified local data or small public sources rather than production disaster archives.
* The project will not require private or sensitive disaster data.
* The project must keep source attribution visible when results from multiple sources are combined.
* Numerical quality targets remain proposed until actual measurements are recorded.

3 Alternatives and selected solution

Assignment 2 compares two approaches for the question-processing part of the same search path.

No final choice is made yet.

The selected approach will be justified in Assignment 3 after a small feasibility check.

Approach A — Simple rule-based event-name / keyword extraction

This is the simple baseline.

The baseline uses a small supported event list plus simple text normalization or matching rules.

For example:

Input:
"What information is available about Hurricane Sandy?"
Known event:
"Hurricane Sandy"
Extracted search event:
"Hurricane Sandy"

The search layer would then use the extracted event name against the configured source metadata.

Strengths

* simple to understand and implement,
* easy to inspect when a query fails,
* little processing overhead,
* fits the deliberately small six-week question set.

Limitations

* depends heavily on supported event names and wording rules,
* may fail on abbreviations, spelling variations, or more flexible questions,
* does not provide broader language understanding.

Approach B — Lightweight named-entity extraction with spaCy

The second approach uses an existing natural-language-processing library such as spaCy to examine the question and identify named entities that may help determine the disaster event.

spaCy provides trained language-processing components that can identify information in text.

https://spacy.io/usage/linguistic-features

The extracted event information would still be sent to the same source-search and result-combination path.

Strengths

* can support more flexible wording than a fixed template,
* reuses an existing language-processing library,
* may support later expansion to locations, dates, and other question details.

Limitations

* adds a model and dependency to the prototype,
* predictions may be incorrect,
* disaster event names may still require extra matching rules,
* may add more complexity than the narrow six-week input set needs.

Comparison against the same requirements

Requirement or constraint	Approach A: rule-based baseline	Approach B: spaCy entity extraction
F1 — identify the event in a supported question	Direct candidate for known event names and bounded wording; easy to verify	Candidate for more varied wording, but extraction is model-dependent
F2 — search configured sources	Uses the same source-search path after event extraction	Uses the same source-search path after event extraction
F3 — combine and label results	Uses the same common result format	Uses the same common result format
F4 — continue when one source is unavailable	Can use the same unavailable-source handling	Can use the same unavailable-source handling
C1 — preserve correct source attribution	Independent of parsing method; source IDs must be preserved	Independent of parsing method; source IDs must be preserved
Q1 — proposed local response-time target	Expected to have low processing overhead; not yet measured	Adds model loading and processing overhead; not yet measured
Six-week implementation constraint	Lower complexity	Higher complexity and an additional dependency
Future question flexibility	Limited	Potentially better, but needs evidence from the supported query set

Current status

No approach is selected yet.

The Assignment 3 decision will use the requirements above and a small feasibility check.

The main question is whether the rule-based baseline already handles the bounded event-focused questions well enough, or whether the NLP approach provides a useful improvement without unnecessary complexity.

4 Architectural design

Work to come in Assignment 3.

This section will show the system boundary, main running parts, communication, dependencies, and what is built, reused, or simulated.

5 Component design and interfaces

Work to come in Assignment 3.

This section will define component responsibilities and the interface contract for the critical search operation.

6 Data structure design

Work to come in Assignment 4.

This section will define the records, fields, relationships, ownership, persistence, and data rules.

7 Algorithm design and execution

Work to come in Assignment 4.

This section will provide pseudocode and normal, interrupted, and overlapping execution behavior for the critical operation.

8 Failures and security

Work to come in Assignment 4.

This section will describe relevant adverse scenarios, misuse cases, expected behavior, and planned checks.

9 Implementation and feasibility

Work to come beginning in Assignment 3.

The first feasibility check will compare the two question-processing approaches on the same small supported query set before the final design choice.

10 Testing and verification

Work to come beginning in Assignment 4.

This section will connect test IDs to requirements and later distinguish expected results from actual observations.

11 Operation maintenance and future work

Work to come beginning in Assignment 4.

This section will cover startup, diagnosis, recovery, risks, maintenance, and the Semester II continuation plan.

12 Revision history and references

Revision history

Revision date	Change to my design	Reason and evidence
November 5, 2026	Created the Assignment 1 design foundation and narrowed the project to one event-focused plain-language search path	The course handbook requires one bounded six-week contribution rather than reproducing the full funded project
November 5, 2026	Kept unavailable-source behavior as the selected adverse case instead of making it the entire project	The product goal is disaster-data discovery; unavailable-source handling is one important condition within that product
November 13, 2026	Limited supported input more explicitly to English event-focused questions that name one disaster event	Makes the system boundary and F1 acceptance check concrete
November 13, 2026	Added F1–F4, C1, proposed Q1, examples, assumptions, and constraints	Assignment 2 requires observable behavior and concrete acceptance checks
November 13, 2026	Added a comparison between a rule-based baseline and spaCy-based entity extraction	Assignment 2 requires at least two approaches compared against the same needs; final selection is deferred to Assignment 3

Open question

Open question	Why it matters	Next action
Does the rule-based baseline interpret the supported event-focused question set reliably enough, or does spaCy provide a useful improvement?	The answer affects complexity, dependencies, and the design selected for the critical search path	Use the same small query set for a feasibility check before making the Assignment 3 decision

Assistance and reuse

The design is based on the course design template and handbook, NSF Project 10, the W3C DCAT specification, and spaCy documentation.

AI assistance was used to help organize and draft revisions to this Markdown document.

The author is responsible for reviewing, revising, understanding, and presenting all submitted content according to course policy.

References

1. National Science Foundation.
    Category III: AI-Driven National Synthesis Hub for Convergent Disaster Research and Intelligence.
    NSF Award 2609535.
    https://www.nsf.gov/awardsearch/show-award?AWD_ID=2609535
    Supports: the larger disaster-archive problem, plain-language questioning, and federated data layer that motivate this project.
2. World Wide Web Consortium (W3C).
    Data Catalog Vocabulary (DCAT) Version 3.
    https://www.w3.org/TR/vocab-dcat-3/
    Supports: the use of common metadata to improve interoperability and discovery across catalogs.
3. spaCy.
    Linguistic Features.
    https://spacy.io/usage/linguistic-features
    Supports: the candidate use of language-processing components for interpreting more flexible question wording.
4. CSC 59866 course materials.
    Software Project Design Handbook, Design Checkpoints, and Design Document Template, Fall 2026.
    Supports: the weekly design process, requirement structure, acceptance checks, comparison method, and distinction between proposed targets and measured results.

Supporting media and evidence

* Workflow/context image — Figure 1 from Assignment 1.
* No measured performance result is claimed yet.
* Q1 is a proposed quality target and will remain labeled that way until it is measured.
* The approach comparison is a design comparison, not a completed feasibility result.

Current document check

* [x]	Section 1 is revised and remains consistent with the bounded project.
* [x]	Four functional requirements have stable IDs and acceptance checks.
* [x]	At least one correctness rule is included.
* [x]	One measurable quality target is included and labeled proposed.
* [x]	Ordinary, unsuccessful, and unavailable-source examples are included.
* [x]	Assumptions and constraints are stated.
* [x]	Two approaches are compared against the same requirements.
* [x]	The final approach is not selected early.
* [x]	At least two relevant project sources are explained.
* [x]	The progress note and references are updated.