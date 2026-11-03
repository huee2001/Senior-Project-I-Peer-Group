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

