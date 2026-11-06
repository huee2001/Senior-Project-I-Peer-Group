Mohamed Kamagate 

# **What problem are you investigating?** 

Describe a specific difficulty and the conditions under which it occurs. Walk through one concrete example, including the normal behavior and what goes wrong. Define the boundaries of the problem. 

Oftentimes a researcher may rely on a source that has been secretly corrected or retracted. This can lead to various problems such as lack of scientific integrity and reproductivity. Specifically, a lack of scientific integrity could suggest a researcher conducting an experiment or paper based on false information that was corrected without their knowledge. Other people could view that person's research as dishonest, intentionally misleading and generally just unreliable. In terms of problems of reproductivity, a scientist must be able to reproduce results based on a giving method and their gathered data. If the data or paper gets changed, other researchers would not be able to confirm their results and use their conclusions. A small example of this was a research paper regarding covid treatment. A research paper regarding how a certain treatment is ineffective caused people to pause trials regarding this treatment, which was even accepted by the WHO. The paper was found unable to be reproduced so the findings of the paper were then disregarded. 

One concrete example would be when researcher A finds interests in researcher B’s study. They used the findings in researcher B’s study into their own paper. Later, other people read researcher A's study and realized they read an updated paper on researcher B's paper. They found errors in A’s but too much time has passed since then and other people may have already downloaded local copies with wrong information. 



The boundaries of this project would be a focus on scientific research papers. The platform would be similar to PubPeer. I would put a focus on mandating documenting changes in a document, with a set guideline. And I will use distributed methods for a 

# **Who or what is affected by it?** 

Identify the users, organizations, or systems affected. Explain the consequences, such as missing information, repeated work, slow results, or incorrect decisions. Connect those consequences to your example. 

<u>Researchers: Downstream researchers specifically are affected by this. They download a local copy onto</u> their machines and are unaware of the stealth changes. 

<u>Data publishers:</u> If these people are more open about their corrections and mistakes, they can be seen as more reliable. Researchers can continue to rely on these knowing how transparent they are. 

Mohamed Kamagate 

# **What evidence do you currently have that it is a real problem?** 

Explain what the published opportunity and technical sources establish. Identify observations or measurements you have actually made. Clearly label assumptions and missing evidence. A request for a product or research topic does not prove that your specific failure has occurred. 

## <u>Inappropriate Citation of Retracted Articles in Anesthesiology and Intensive Care Medicine Publications</u> 

This paper conducted a research where they collected 478 retracted articles and tried finding out how many of the authors that used retracted articles knew the articles we’re retracted. The article states “We contacted 1297 corresponding authors of the papers that cited these articles, 417 (30%) of whom responded to our survey and were included in the final analysis. The median number of authors in the analyzed articles was five, and the median elapsed time from retraction to citation was 3 yr. Most of the corresponding authors (372, 89%) were unaware of the retracted status of the cited article, mainly because of inadequate notification of the retraction status in journals and/or databases and the use of stored copies.”  The platforms and authors varied meaning this problem seems to be prevalent across the scientific community. The fact that most scientists (about 89% of the sample size recorded) didn’t realize the changes also implies most people with static local copies don't often manually check if corrections were made by the time they published their paper. 

Good quote “'With transparency and proper documentation, you safeguard the process of disseminating scientific knowledge. It’s always important to know if something has changed, because second-guessing every scientific article you read will hurt science as a whole.'” 

Source: Inappropriate Citation of Retracted Articles in... : Anesthesiology 

## <u>Study shows stealth corrections in scientific articles</u> 

A more anecdotal experience with this involves one of the previous authors in which they reported an error in figures, two of them being the same. He states: 

“'Hey, these images are the same,' thought neuroscience researcher René Aquarius while conducting research for an animal experiment study on brain hemorrhages. In preparation for a new study, he delved into the literature and stumbled upon identical images that were associated with different groups. 'A mistake has been made here,' he thought. He made a report on the forum PubPeer, where scientific papers are discussed. The author of the article responded, thanked Aquarius, and said they would look into it. For a month, nothing happened, until Aquarius revisited the website of the publisher to look at the article again. To his surprise, the images had been altered, without any mention of it. On PubPeer, he found more researchers reporting changes to scientific publications that were not disclosed, known as stealth corrections. They united and spent months investigating unreported changes, by asking other ‘science detectives’ (or sleuths) and by using tools such as social media and prior PubPeer posts.” 

Mohamed Kamagate 

Two things to note here: since the scope of this project and problem revolves around scientific research, its imperative to have accurate info. Otherwise it can be very harmful to patients. The topic in question was brain hemorrhages. 

Another thing to note is the “tools” researchers use to detect corrections is social media, and PubPeer posts made about the papers, not the authors themselves. This is obviously not reliable because some research can be niche and not as many people can view it for mistakes, and not every researcher posts on social media.  Finally the author suggests methods to improve this 

“Aquarius and his international colleagues offer three suggestions to prevent stealth corrections: 

- Develop and implement a mandatory system for publishers that publicly logs all changes that have been made to published works. 

- Create clear definitions and guidelines for all types of corrections. 

- Promote vigilance among scientists to publicly register stealth corrections. 

## “ 

This full falls in line with the FAIR guiding principles advocated by the fairos program. 

<u>Study shows stealth corrections in scientific articles - Some scientific articles are secretly changed - Radboudumc</u> 

I will also post other things I had in my past paper that I feel would be relevant here. 

## <u>Guidance on Versioning of Digital Assets</u> 

In this paper, by Helmholtz Metadata Collaboration, it states the importance of having good version control of documents and datasets. “Using the wrong version of a (meta)data set can lead to drastically different outcomes in interpretation, and lead to substantial, propagating downstream errors.” It then goes on to say “...a digital "chain of evidence" that records who changed what and why over the life cycle of a digital asset is a key component of good data management. …Without this chain, and the transparency it brings, it is far more difficult to assess the trustworthiness of (research) data, especially as projects close and the individuals who generated the data are no longer available. “ These passages 

Mohamed Kamagate 

highlight the existing risks of bad version control documentation. It noted the problem in a general(Similar to what the “Versioning Data Is About More than Revisions: A Conceptual Framework and Proposed Principles” paper wants to resolve) sense, where downstream errors can be a variety of things such as using old values that were corrected in the newest versions, and highlights a specific problem of how not having proper documentation and preserving meanings through each version can create distrust in the credibility of the data. Both things compromise the ongoing research of a downstream researcher which is a problem mentioned in my problem statement. Guidance on Versioning of Digital Assets (my definition of downstream researchers are those who work on a replica on their own local machine from a given source). 

Shedding Light on the Dark Data in the Long Tail of Science This paper starts by saying scientific research outputs data, but infrastructures that are responsible for preserving and spreading the data are doing a bad job at it. This leads to the coined term, “Dark Data.” Dark data is essentially research data that hasn’t been sufficiently documented in ways such as indexing it (making it easily findable) and storing it. The problem here is that scientists aren’t able to make use of this valuable data since it's so hard to find. This directly ties into the FAIR guiding principle that is trying to solve a problem like this Observation: Sometimes using someone's dataset from kaggle, there's an update to the dataset. The one previously used obviously leads to different results when using it on an AI model. This becomes a problem especially if the changes aren't documented. And may have a harder time creating a new pipeline to clean and format the data. Assumptions: Many platforms allow publishers to add version notes or field descriptions(i.e Kaggle) , but do not require them or enforce a consistent, machine-readable way to record schema or unit changes, so a change can go undocumented. 

# **What solutions already exist?** 

Compare at least two existing approaches. Explain how they work, what they handle well, and their limitations under your chosen conditions. Use relevant documentation to support the comparison. 

<u>PubPeer: It’s a scientific research platform that allows form discussions. Through the forum discussions,</u> users are able to identify errors and post comments about it. Furthermore, there is a “get alert for new activity” in which if you place your email, you will get notifications about other researchers comments about the problem. 

Mohamed Kamagate 



<!-- Start of picture text -->
Email<br>Please<br>input your e-mail<br><!-- End of picture text -->

The limitation is it does not follow a strict guideline to document changes, allowing for “Stealth corrections” and/or retractions to occur. Also the author can choose not to post comments about it 

<u>Github: Is a great example that allows for good version tracking.   One limitation is since the project is</u> specific to scientific research paper, github covers a more broad category. (Will also paste my past comments on this) 

Strengths are, records full history of changes to the data, including who changes what and when. Commit message is also attached to each change for semantic versioning. Can see a “snapshot” of each version. Very machine-actionable Limitations are, doesn’t notify downstream researchers of updated versions, must be manually checked. Another limitation is line by line comparison of changes in diff file , and commit messages can be wishy washy in quality (i intend to solve by making it community based. Can like or dislike based on how good documentation is. ) 

# **What is the most important thing you still do not know?** 

Identify the uncertainty that most affects your proposed work. Describe a research step or experiment that could resolve it. State what data, scenario, or measurement you would use and how the result would influence your design. 

1. I’m still unsure of the final guideline procedures I should mandate for authors. I fear that putting too much work would discourage people from going to the platform, and how too little will still 

Mohamed Kamagate 

lead to bad understanding of the changes. A research step I will do is learn more about FAIR practices and what other researchers did to implement documentation. 

2. Another thing I’m unsure of is what specific tools I should use to implement this project to track changes, especially if it’s similar to PubPeer. 

------
# AI-Driven National Synthesis Hub for Convergent Disaster Research and Intelligence

<!-- Copy this file into your project directory as DESIGN.md. Replace prompts
with your own explanations as sections become due. Create assets and evidence
directories for files you include. Remove instructional comments at final submission. -->
## Problem and scope
Disasters can take place any time. It's important to be prepared for, properly respond to, and recover from said disasters. The problem is disaster information is spread across many repositories , fragmented known as silos. These data silos often compliment each other or further elaborate on each other but alone they aren't as useful. The emergency responders, disaster scientist, and the general public affected by these disasters may not have the time to consolidate all these fragmented information and the general public may not have the means to these resources locked behind well funded agencies, large cities,  elite research universities or understand the jargon. The aim of this project is to democratize technology by providing a plain language query interface with real-time accurate information


For this project, my scope will be narrowed to disasters that primarily affect New York (i.e Floods, hurricane, heat waves).


### What this version leaves out

- Limited to disasters that primarily affect New York and related archives (floods)

**Author:** Mohamed Kamagate  
**Course:** CSC 59866  
**Selected project and option:** 10  Category III: AI-Driven National Synthesis Hub for Convergent Disaster Research and Intelligence   
**Current assignment:** 1
**Friday commit deadline:**  November 6 2026, at 11:59 p.m. New York time  
**Monday presentation:**  November 9 2026, at 6:30 p.m. New York time  
**Last updated:** 11/4  
**Document status:** Proposed, revised, or ready for review

<!-- Commit and push by Friday. Supply the exact commit identifier through the
course submission channel. Every Monday, present your own work and orally review
the same selected group mate for the remainder of the semester. No written
peer-review report, review link, or review transcript is required. -->

## Progress note

<!-- Write 100â€“150 words: changes, learning, main open issue, feedback addressed,
and next step. Link evidence when available. Update at each Friday deliverable. -->

## Contents

- [1 Problem research and scope](#1-problem-research-and-scope)
- [2 Requirements and system specification](#2-requirements-and-system-specification)
- [3 Alternatives and selected solution](#3-alternatives-and-selected-solution)
- [4 Architectural design](#4-architectural-design)
- [5 Component design and interfaces](#5-component-design-and-interfaces)
- [6 Data structure design](#6-data-structure-design)
- [7 Algorithm design and execution](#7-algorithm-design-and-execution)
- [8 Failures and security](#8-failures-and-security)
- [9 Implementation and feasibility](#9-implementation-and-feasibility)
- [10 Testing and verification](#10-testing-and-verification)
- [11 Operation maintenance and future work](#11-operation-maintenance-and-future-work)
- [12 Revision history and references](#12-revision-history-and-references)

## 1 Problem research and scope

<!-- Assignment 1. Describe a person, task, difficulty, and consequence using
a concrete scenario. Label assumptions. Distinguish a larger research project's
aims from your own contribution where relevant. -->

**Problem and affected people:** Disaster related info is scattered across many archives, which makes it harder to have complete understanding of the topic because some works complement each other or further elaborates on it, and many people affected may not have the time to consolidate it all.
These archives are needed for decision making, long term or quick, by common people affected by these disasters, disaster science researchers who study these events and write ontologies about them, and first responders or emergency managers who act based on this info
This information might also be hard to interpret due to the jargon, technical or software skills needed to extract the info, or lack of general access to these things.

*Potential Stakeholders*
* Under-resourced communities
* Disaster science researchers
* Emergency Managers/First responders

(1)*General Public/Victims to disasters* “broaden access for under-resourced communities,” 
* Communities who are under-resourced include people in rural areas where much analysis arent done in there region, making GIS maps useless for them and not much documentation they can go off on. They can query the AI agents, asking for things like "What federal grants are available for repairing our specific type of bridge damage, and what documents do we need?" where the AI agent can fetch fema documents and make it easier to understand and interpret by the user.

* Low-income communities in general are most affected by these disasters[^1].. They’re located in flood prone zones, bad urban infrastructure, and are often left out of academic loop when new works are published. Since traditional disaster data is hidden behind paywalls or especially  locked behind complex academic jargon, a plain language query ai engineering hub such as this project provides accurate, and clear guidance on what to do and what to expect. LLMs can be used, but they fall victim to halluncinations and unreliable sources. This project utilizes a federate data layer that enables source independence, allowing responses to be tracked to their original source proving to be accurate. 
[^1]:  An example of this https://nysclimateimpacts.org/explore-the-assessment/case-studies/hurricane-ida-vulnerabilities-in-new-york-city/#:~:text=Left%2C%20the%20basement%20living%20space%20in%20Brooklyn%2C,federal%20assistance%20because%20of%20their%20immigration%20status

(2) *Disaster science researchers*  “support training of the next generation of disaster researchers and practitioners”
* Natural disasters/catastrophes are inherently complex. They require a blend of research to make full understanding of it. There is also a knowledge gap, social scientist must blend together hard technical data (like hydrological sensor readings) with social science. This project helps by bridging engineering findings with social science data
* Disaster catastrophes are inherently complex. To fully extract real info and/or raw data, it requires a mix of domains between engineering and social science and physical science. Instead of learning these domains, a specialist can prioritize their respected field, and allow this platform to bridge the knowledge gap. 
* Disaster science researchers must also be able to cite deep historical literature that is accurate. A simple LLM can cause halluncinations and are difficult to cite properly. Search engines are helpful, but may take up too much of the researchers time. This platform provides accurate information that can be cited due to the federate data layer component. 

(3) Emergency Managers/First responders
* Must be able to make quick, accurate descions. Instead of scavenging multiple sources too get the best, accurate, real time information, this platform helps them save time and potentially lives. In addition, sources these stakeholders look at (such as  NYC open data, FEMA, etc.) would be included in the federate data layer. 

**Current workflow:** A user queries a adadptive knowledge broker. The knowledge broker breaks down the query into its semantic value tokens then delegates the tasks to a specialized domain agent. The domain agent then refers to its personalized repositories (or really api's) to formulate a response. The broke then stitches back the response and cleans it up(solving conflicts between 2 domain agents for example) before responding back to the user  
![Visual.](assets/FourTierAgentic.png)
**Evidence:**   

University of delaware DRC hosts oldest archive of ontologist related works. The information may complex and less suited for non-researchers who are looking for accurate and clear guidance.

https://udspace.udel.edu/communities/bdc76090-7084-449f-a272-f6c7bdff1a5f/search




**Six-week contribution:** *State the small capability you will demonstrate.*
Implement a RAG system. It'll be more static, the ai agent would query a vector database regarding flooding information in new york instead 

**Semester II scope:** *Explain what the completed project will add.*
Design it to be more scalable to accept a variety of disaster archives. Implement the four tier agentic architecture.
**Exclusions:** May keep the domain narrow to disasters that affect New Yorkers primarily, the best example being floods. May refer to several api's and repositories instead of the vast amount availiable 

<!-- Add an actual image using a relative path, for example:
![Description of the workflow](assets/workflow.png)

Figure 1. Explain what the workflow shows and why it matters.
Do not leave references to nonexistent images. -->

## 2 Requirements and system specification

<!-- Assignment 2. Explain required behavior before implementation methods.
Start with 3â€“5 functions, a correctness rule, and a quality target.
Complete design and test references during Assignments 2 and 3. -->

| ID | Required behavior and conditions | Acceptance check | Design and test reference |
|---|---|---|---|
| F1 | User-visible capability | Concrete check | Add as design develops |
| C1 | Rule that must remain true | A case that could violate it | Add as design develops |
| Q1 | Measure, unit, target, workload | Measurement procedure | Mark as target until measured |

**Inputs and outputs:** Give an ordinary example and an unsuccessful example.

**Assumptions:** Conditions you rely on and how to check them.

**Constraints:** Limits on time, tools, data, and resources.

## 3 Alternatives and selected solution

<!-- Draft in Assignment 2; complete in Assignment 3. Compare at least two
approaches under the same requirements, including a simple baseline. -->

| Approach and source | Useful behavior | Limitation | Evidence or assumption |
|---|---|---|---|
| Simple baseline | Replace | Replace | Replace |
| Candidate alternative | Replace | Replace | Replace |

**Choice and reason:** Connect your choice to requirements and constraints.

### Decision 1

**Context and requirement:** Why is a choice needed?  
**Options:** Plausible alternatives.  
**Decision and reason:** What you selected and why.  
**Consequences:** Benefits, costs, and limitations.  
**Status and revisit condition:** Proposed or accepted; what might change it?

### Decision 2

**Context and requirement:** Replace.  
**Options:** Replace.  
**Decision and reason:** Replace.  
**Consequences:** Replace.  
**Status and revisit condition:** Replace.

## 4 Architectural design

<!-- Assignment 3. Show context and the main running programs and stores.
Embed a diagram from assets and retain editable source. Mermaid is optional. -->

**Boundary and outside participants:** Replace.

**Main parts and messages:** Explain responsibilities and labeled arrows.

**Where parts run:** Identify shared machines and dependencies.

**What I build reuse or simulate:** Replace.

## 5 Component design and interfaces

<!-- Assignment 3. A component can be a function or module in one program. -->

| Component | Responsibility | Input | Output or state change |
|---|---|---|---|
| Replace | Replace | Replace | Replace |

**Critical operation:** Name and purpose.

**Input:** Fields, types, allowed values, caller identity, and example.

**Output:** Fields, meanings, and example.

**Errors:** Conditions and appropriate caller actions.

**Repeated or overlapping calls:** Define the behavior.

## 6 Data structure design

<!-- Assignment 4. Explain information and meaning, not only storage syntax. -->

| Record or structure | Fields and example values | Relationships and rules | Persistence |
|---|---|---|---|
| Replace | Replace | Replace | What survives restart? |

**Ownership:** Identify the authoritative place for important facts.

**Invalid combinations:** Explain how they are prevented or detected.

**Retention and deletion:** Explain how long data is needed and what deletion changes.

## 7 Algorithm design and execution

<!-- Assignment 4. Replace this block with your pseudocode. Explain any step
that hides a guarantee, such as a protected write. -->

```text
ALGORITHM NAME(inputs)
    replace with input checks
    replace with decisions and state changes
    replace with output and error behavior
```

**Normal sequence:** Numbered steps or an explained sequence diagram.

**Interrupted sequence:** Failure point, surviving state, and recovery.

**Overlapping activity:** A conflicting execution and the mechanism that handles it.

**Resource estimate:** A small justified estimate if it affects the choice.

## 8 Failures and security

<!-- Assignment 4. Include three adverse scenarios and two misuse cases. -->

| Scenario | State that may survive | Expected behavior | Planned check |
|---|---|---|---|
| Replace | Replace | Replace | Replace |

**Selected adverse case for the prototype:** Name the case and why it matters.

**Excluded conditions and consequences:** Replace.

| Possible misuse and affected asset | Response | Remaining limitation and check |
|---|---|---|
| Replace | Replace | Replace |

## 9 Implementation and feasibility

<!-- Begin the feasibility experiment and path in Assignment 3; refine in Assignment 4;
report implementation status in Assignments 5â€“6. -->

**Minimal path:** The smallest useful end-to-end operation.

**Feasibility experiment:** Question, procedure, evidence, finding, design consequence.

**Current implementation:** Distinguish implemented, reused, simulated, blocked, and deferred.

**Run instructions and CI:** Link README.md and the recorded check.

## 10 Testing and verification

<!-- Plan in Assignment 4; add observations in Assignments 5â€“6. Expected outcomes
are not results. Link raw evidence. -->

| Test and requirement | Setup and procedure | Expected result | Status and evidence |
|---|---|---|---|
| T1 normal operation | Replace | Replace | Planned until run |
| T2 correctness rule | Replace | Replace | Planned until run |
| T3 adverse scenario | Replace | Replace | Planned until run |

**Baseline and comparison question:** Replace.

**Workload and environment:** Inputs, counts, timing, overlap, versions, machine, and reset.

**Measurements:** Units and populations, including unsuccessful operations.

**Actual results:** Explain what happened and what the evidence supports.

**Limits and next test:** State remaining uncertainty.

## 11 Operation maintenance and future work

<!-- Draft in Assignment 4; add operating instructions in Assignment 5;
complete in Assignment 6. -->

**Startup and diagnosis:** How to run the system and recognize a problem.

**Recovery:** Action, preserved state, and verification of recovery.

**One future change:** Effects on components, interfaces, data, and tests.

**Update and rollback:** How to change versions and recover a working configuration.

**Responsible design:** Connect people, data, access, reuse, and resource use to choices.

| Risk | Early sign | Response or fallback |
|---|---|---|
| Replace | Replace | Replace |

| Semester II milestone | Dependency | Completion evidence | Essential or optional |
|---|---|---|---|
| Replace | Replace | Replace | Replace |

## 12 Revision history and references

| Revision date | Change to my design | Reason and evidence |
|---|---|---|
| 11/4 | Initial plan | Just started |

| Open question | Why it matters | Next action |
|---|---|---|
| What is the best AI framework to handle the four tier architecture presented  | An AI framework provides standard patterns for agent communication, allowing one agent's structured JSON output to automatically trigger the next agent's input without custom glue code. | Start iteratively first before introducing the AI framework. Design a RAG system before making it more dynamic |

**Assistance and reuse:** Attribute sources, code, data, diagrams, and assistance under course policy.

### References
https://www.floodnet.nyc/flood-event-summaries
https://seagrant.sunysb.edu/floodinfonyc/#/local-reports

https://udspace.udel.edu/communities/bdc76090-7084-449f-a272-f6c7bdff1a5f/search

https://www.fema.gov/about/openfema/data-sets

https://data.cityofnewyork.us/Environment/FloodNet-Street-Flooding-Events-Measured-by-FloodN/aq7i-eu5q/about_data

<!-- Use descriptive links with author/organization, title, date/version, and
the claim supported. Also cite sources near relevant explanations. -->

### Supporting media and evidence

<!-- Link actual images, editable diagram files, logs, data, and optional video.
Explain each item's purpose. Avoid missing files and private-only paths. -->

### Final document check

- [ ] Terms and examples make the project understandable to a beginner.
- [ ] All twelve sections contain project-specific content.
- [ ] Requirements connect to design and tests.
- [ ] Architecture, components, data, and algorithms agree.
- [ ] Targets and plans are separate from observations.
- [ ] Tables, images, pseudocode, references, and evidence links render correctly.
- [ ] Images have alternative text, captions, and readable labels.
- [ ] Run instructions and evidence support reproduction.
- [ ] I am prepared to present my work and orally review the same selected group mate.
- [ ] Remaining work and maintenance needs are explicit.
- [ ] Instructional placeholders are removed from the final submission.