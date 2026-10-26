### Ibsan Hossain 

### Senior Project 

A12 — Benchmarking Heterogeneous Computing and Sensing 

## **What problem are you investigating?** 

The question being explored here is how one determines which computer in the distributed system should be used to process the sensor data if there are computers with varying levels of capabilities in the system. This would mean that there could be a small computer near the sensors and a bigger computer further away in the network. The data could be processed by the larger computer faster than by the smaller one, but first it has to be sent over the network. It therefore means that having the largest computer does not always imply getting the quickest result. 

This problem is connected to edge computing, which is a form of distributed computing where processing is done close to data sources. According to International Business Machines Corporation (IBM), "edge computing involves placing applications and processing close to the data source – IoT devices". It also notes that sending all the data from the devices to a data center or cloud creates issues with latency and bandwidth. 

<u>https://www.ibm.com/think/topics/edge-computing</u> 

A simple example illustrates the above issue. For instance, suppose there is an environmental sensor which captures some information. A small computer connected to the sensor may take ten seconds to analyze the data. A more advanced computer located away from the sensor may take three seconds to do the same. However, while transferring the information to the remote computer takes one second, the remote option will take four seconds. On the other hand, suppose that the communication channel between the computers gets worse so that the transfer of information now takes eight seconds; in such a case, the remote analysis may take eleven seconds. In that case, the slow local computer will complete the job first. 

As you see, these figures are arbitrary and not actual results I have measured. They just help to illustrate the condition under investigation. The point is that the total time spent on completing the task consists of processing and communication time in case of the remote computer usage. 

According to the reading Communication in Engineering Capstone Projects, engineers must first be aware of and prove the actual need prior to pursuing the solution. Incorrect need might lead to the wrong design which does not solve the problem itself. In this regard, I would not assume right away that local processing/edge computing must be considered a solution. First, I need to understand how processing capacity and communication delay influence the decision. 

This project will only analyze the comparison between local processing and remote processing based on changing communication delay. No new sensor, processing unit, communication protocol and cloud systems will be designed in this project. 

# **Who or what is affected by it?** 

The issue also applies to those who design and operate systems that gather data using sensors and have more than one potential site for processing this data. These systems include systems for environmental monitoring, intelligent buildings, industrial monitoring, transportation, and other applications based on the Internet of Things. 

The computers used in such a system are also affected by this decision. A local computer will not have as powerful capabilities as a remote computer but will have immediate or almost immediate access to data coming from sensors. A remote computer will be much more powerful but will only get access to data after it comes through the network. 

A similar issue is discussed in the concept of Fog Computing by the National Institute of Standards and Technology (NIST). According to NIST, cloud-based systems designed for IoT are often faced with problems related to large numbers of devices, diversity of devices, and latency. 

<u>https://www.nist.gov/publications/fog-computing-conceptual-model</u> 

The consequence of choosing a wrong processing location in my case is reduced speed. Given a fast connection, the remote computer wins the race as its increased processing power compensates for the time taken to transmit the data from the sensors. When the network connection is slower, the remote computer will spend more time on transmission than processing the data locally. 

Network usage also changes as a result of transmitting the data from the sensors to the remote computer since data transfer is involved. Latency and bandwidth are considered by IBM as key factors driving computation offloading from remote locations. 

However, this does not imply that local processing is preferable all the time. A small local computer can process data much slower than the remote computer. The question is about the conditions under which one of the two choices becomes better. 

## **What evidence do you currently have that it is a real problem?** 

The published opportunity associated with A12 is the Defense Advanced Research Projects Agency (DARPA) Multi X Office (MXO) Office-wide Innovative Solutions Opening, DARPA-PS-26-115. This opportunity provides the broader research context connected to the A12 project area. 

### <u>https://sam.gov/opp/2b5fd12340a642e4ac3d1f5c21ecaeed/view</u> 

The DARPA opportunity does not show that my specific local and remote processing problem is experienced by any organization. Neither does it show whether the local processing or remote processing is more effective. It only creates a research background, while my performance behavior will have to be tested. 

The NIST concept, on the other hand, gives technical details. The Fog Computing Conceptual Model shows how traditional cloud-based IoT solutions suffer from latency and how the migration of applications and data analytics to the devices is a solution to these challenges. 

<u>https://doi.org/10.6028/NIST.SP.500-325</u> 

IBM also explains that sending device-generated information to centralized cloud or data-center resources can create latency and bandwidth problems. 

<u>https://www.ibm.com/think/topics/edge-computing</u> 

At this phase, my evidence is divided into three types. The first evidence is the documented evidence, which I got from the sources NIST and IBM, and it documents that latency, bandwidth, and location of processing are issues in the field of distributed sensing and the Internet of Things. I do not have any observed evidence yet, since I have not constructed my simulation and taken measurements. My hypothesis at this point is that if the communication delay increases, it will eventually be faster to process locally rather than remotely for some tasks. 

Also, the assigned reading Research and Analysis of Existing Solutions indicates that engineers need to analyze the existing solutions and identify the pros and cons before starting the design process. 

## **What solutions already exist?** 

Centralized or remote processing is one of the existing approaches in which the sensor data is sent over the network to a remote computer or cloud for processing. 

The advantage of this method is that it uses more processing power. A remote server may possess more processing capability and memory than the tiny local computer. When there is fast communication between these two, the task might get done faster by using remote processing. 

The disadvantage of this method is that communication through the network adds to the overall completion time because the data needs to reach the remote computer for the task to get done. 

The second way is local or edge processing. The difference between these approaches is that in this one, some or all of the processing is done near the sensor. This decreases the reliance on communications with a remote computer and can decrease the data transmitted via the network. 

Its drawback is that local devices can have significantly less processing power. If the network 

performance is good and the computer is significantly more powerful, then local processing may be slower. 

The third way to do this is a hybrid or adaptive approach. The processing can be done both locally and remotely, while the other approach can be choosing which type of processing is more appropriate depending on the delay in communications and expected processing time. 

The adaptive approach will not be my last choice for implementation yet. First, I need to find out if there is any change of preferable location for processing of data. 

That aligns well with the types of engineering design described in the first reading assignment. This document describes adaptive design as applying an existing solution to a new application, while redesign modifies an existing solution. In that sense, my ultimate design might adopt edge and remote processing techniques rather than inventing a new type of computing. 

There is a tool I would use in future tests and modeling that is SimPy, which is a discrete event simulator for Python. SimPy provides process, events, timing, and limited shared resources. In this way, I can model a local computer, a remote computer, processing time, and network communication delay without using sensors. 

<u>https://simpy.readthedocs.io/en/stable/</u> 

## **What is the most important thing you still do not know?** 

The biggest thing that I do not understand is at which point of delay, if any, does local processing become more advantageous than remote processing on a faster computer of the same workload. 

This is crucial since the answer tells me whether a simple static process will do the job or not. In case remote processing is better in all possible situations, then there is no need for an adaptive process. However, if it depends on the delay value, an adaptive process may work. 

The next step in my research will be the development of a simulation where I have one workload for sensing and two simulated computers. One computer is low-performance, local, while the second is high-performance, remote. The same workload is being processed in both cases. 

Workload and processing abilities will be kept constant, and only the communication delay will be changed gradually. For each communication-delay setting, I would measure the total completion time and the amount of data transferred. These measurements would allow me to determine whether a crossover point exists and whether an adaptive placement approach is worth considering. 

The objective is to find out if there is a crossover point. The remote processing may be faster at low communication delay and vice versa. However, one should not assume anything before the tests. 

Such a crossover would be helpful for implementing the adaptive placement technique. In case one approach is always better, this information can also prove useful, as it may be used to confirm that there is no need in anything else. 

# **Your Individual Scope and Senior Project Relationship** 

The project will involve studying the performance of one simple sensing workload, two computing nodes, and communication delay as the varying parameter. The first node will model a relatively less powerful 

computer that is close to the sensor. The second node will be the more powerful computer located remotely and connected to the first one via a network. 

In the project, the comparison of the local and remote computation processes under various communication delays will be performed using such metrics as total completion time and data transfer volume. 

Concerning the implementation part, I plan to implement the simulation using Python and SimPy. No real sensors or cloud computing platform will be used in the experiment; no security, privacy, power consumption, competing processes, and complicated scheduling issues will be taken into account in the current project. 

A possible solution could be an adaptive placement algorithm which will take into account processing capacity as well as communication delay while deciding where to place the workload for processing. This is just a possible direction of solutions and not an existing solution yet. 

This project falls into the category of distributed computing since it is about computing using distributed resources and communication over a network where the behavior of the whole system will depend on processing capacity as well as communication among these resources. 

This project is doable by one person since it requires only one workload, two types of computers, and one changing variable. 

# **Connection to the Three Assigned Readings** 

Engineering Design Approaches would impact my perspective of the project since I do not need to consider that I must produce a completely novel design. The readings mention such types of engineering designs as adaptive design, redesign, and selection design, aside from original design. In my project, I might have to adapt or modify some existing processing-placement solution rather than come up with a new one. 

Research and Analysis of Existing Solutions states that one needs to study existing solutions before engaging in active design and that one has to study their pros, cons, and possible improvements. In the case of A12, this means that I have to compare local processing and remote processing before I can conclude that adaptation is required. 

Communication in Engineering Capstone Projects says that one needs to comprehend and prove the necessity of the issue and only then provide the solution. In this case, this would mean that I have to understand what is already stated in the technical sources about local processing and how my hypothesis compares with them. 

# **References** 

[1] Defense Advanced Research Projects Agency (DARPA). _MXO Office-wide Innovative Solutions Opening, DARPA-PS-26-115._ 

<u>https://sam.gov/opp/2b5fd12340a642e4ac3d1f5c21ecaeed/view</u> 

[2] National Institute of Standards and Technology (NIST). _Fog Computing Conceptual Model, NIST Special Publication 500-325._ 

<u>https://doi.org/10.6028/NIST.SP.500-325</u> 

[3] IBM. _What Is Edge Computing?_ 

<u>https://www.ibm.com/think/topics/edge-computing</u> 

[4] SimPy. _SimPy Documentation._ 

<u>https://simpy.readthedocs.io/en/stable/</u> 

[5] _Engineering Capstone Design: Project Planning, Organizing, and Executing._ “Types of Engineering Design.” Assigned course reading. 

[6] _Engineering Capstone Design: Project Planning, Organizing, and Executing._ “Research and Analysis of Existing Solutions.” Assigned course reading. 

[7] _Engineering Capstone Design: Project Planning, Organizing, and Executing._ 

- “Communications in Engineering Capstone Projects.” Assigned course reading. 

