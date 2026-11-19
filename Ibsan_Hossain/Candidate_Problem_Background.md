# Candidate Problem Background

**Ibsan Hossain**  
**Candidate problem:** Detecting password spraying  
**September 28, 2026**

## Part 1: Describe the Problem

It is important for the security analyst to detect the process of password spraying before the attacker is able to access the account. In such an attack, the attacker uses one or several passwords on numerous accounts, and this might be performed over a period of time to prevent per-account lockout, according to the MITRE ATT&CK. The company might have authentication logs of its cloud identity provider, remote access portal, VPN, and other applications.

The particular problem to address would be that of late arrival of login logs. The timing of a particular login attempt can be one point, but its logging may be done after some minutes. Given the different delivery lags of services, a particular filtering rule may fail because it will only look for an event-time window. This problem is well detailed by Microsoft for scheduled analytics rules on how to set up a particular rule that considers the ingestion lag. In case of password spraying, the omission of some attempts will mean that the overall attempt against many accounts becomes less suspicious.

My proposed solution for Senior Project II is a delay-tolerant detector which will categorize the failed attempts according to the time when they were made, allow late arriving records, and send an update to the corresponding alarm without duplicate messages. It should be noted that this system is an indication of the direction worth researching rather than a definite design.

## Part 2: Provide Evidence

**Documented:** The MITRE ATT&CK framework explains the concept of password spraying along with detection methods that require more than one account or source of authentication. NIST explains why it is necessary to capture and analyze logs for security purposes across an organization. Microsoft's Sentinel documents one specific case where an event that occurred late is not picked up by a scheduled rule's look-back filter; a fix has also been documented.

**Hypothesized:** Unpredictable delays within each service could cause issues in detecting and deduplicating password spray events. I have never seen an organization miss a password spray attack for this reason. The sources outline a potential failure point but not its prevalence or an unaddressed problem.

## Part 3: Investigate Existing Solutions

Microsoft Sentinel can ingest logs and perform scheduled analytics rules. Their documentation talks about delay handling in terms of expanding the event-time look-back and filtration based on ingestion time to avoid duplicates. This is a solid baseline for my project. The password spray detections are published by Splunk Enterprise Security via their Authentication Data Model including a distributed-spray analytic. This proves that correlation of sign-in events and password spray detection is already possible. Microsoft Entra ID Protection offers a password-spray risk detection in their identity domain; Microsoft claims that the mentioned detection triggers after successful authentication. I would test a fixed window rule, the described by Microsoft Sentinel approach and my own adaptation under the same simulated log arrival rates. The issue here is whether a rule that supports dynamic delays performs better at finding attacks and duplicates than existing approaches while keeping low alerting latency. I am not sure whether it does yet.

## Part 4: Relate the Problem to the Senior Project

This is currently closer to Option 2: cybersecurity detection challenge related to distributed services. This may also involve adaptive design through extension of an existing detector design, along with selection design for selecting log processors. First, I will analyze the existing baselines, rather than try to present my own design for password-spray detection. The need for distributed computing arises due to the fact that independent services produce their events independently and send them via a network. They may have different clocks and delivery time, and one of them may become temporarily unavailable. The detector needs to separate the event occurrence time from its arrival time, combine relevant records and not repeat alerts if late records alter previously processed time intervals.

## Part 5: Identify What I Still Do Not Know

1. **What is the degree of variability in authentication log delays in applicable systems?** Examine the documentation and research findings, then measure the delays in a test environment where you have authorization.
2. **Is there already a delay-aware rule that works well enough?** Implement the Sentinel rule as outlined in the document as the basis for comparison against another technique using the same test data.
3. **What is the trade-off between detection and alerting delays?** Test the normal sign-ons and spray attacks with delays, recording missed attacks, duplicate attacks, false positives, and delays until the alert is raised.

## Part 6: Identify One Early Risk

A valid assessment requires representative login history data, as well as delay data. The real-world authentication data is sensitive and unobtainable for security reasons. The use of artificial data makes an experimental assessment possible but does not ensure its applicability.

## Part 7: Connect the Readings to the Candidate

Adaptive design is justified by the "Types of Engineering Design" reading since Sentinel shows there is already a solution for a similar failure mode. By "Research and Analysis of Existing Solutions," I need to test the solution and other baselines to see if my design is really better than them. "Communications in Engineering Capstone Projects" makes me label the "delayed ingestion" as "documented" and the "variable delays" as hypothesis. I will keep track of sources, assumptions tested, and design changes in my research log.

## References

- MITRE ATT&CK. "Brute Force: Password Spraying (T1110.003)." https://attack.mitre.org/techniques/T1110/003/
- K. Kent and M. Souppaya, *Guide to Computer Security Log Management*, NIST SP 800-92, 2006. https://doi.org/10.6028/NIST.SP.800-92
- MITRE ATT&CK. "Distributed Password Spraying via Authentication Failures Across Multiple Accounts (DET0487)." https://attack.mitre.org/detectionstrategies/DET0487/
- Microsoft Learn. "Handle ingestion delay in Microsoft Sentinel." https://learn.microsoft.com/en-us/azure/sentinel/ingestion-delay
- Splunk Security Content. "Detect Distributed Password Spray Attempts." https://research.splunk.com/application/b1a82fc8-8a9f-4344-9ec2-bde5c5331b57/
