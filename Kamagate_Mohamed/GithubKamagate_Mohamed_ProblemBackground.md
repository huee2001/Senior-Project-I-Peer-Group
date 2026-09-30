## Part 1 — Describe the Problem

## Explain:

- Who or what experiences the problem?

- What are they trying to accomplish?

- How is it currently done?

- What difficulty or limitation exists?

- Why does the problem matter?

- Under what conditions does the problem occur?

Describe the problem without assuming your eventual solution.

Training AI Models have become increasingly popular in current day society. It is nearly

common to see a website, software, or developer incorporate some type of AI into their product. The problem is datasets are becoming larger, parameters are reaching the trillions, and hardware is becoming more expensive. As data continues to grow, it introduces more and more obvious bottlenecks such as network & synchronization that helps allows GPUs communicate with each other1, and hardware capacities due to VRAM having limited storage.

## Who or what experiences the problem?

Companies, Machine learning engineers, AI researchers and general computer science developers in general experience these problems. They may run into this problem during data analysis or fine tuning an AI model.

What are they trying to accomplish?


They are trying to reduce there previously mentioned bottlenecks when working with gigantic, terabytes+ amounts of datasets across multiple servers. This would primarily look like efficient communication between the GPUs via a well established distributed system framework along with efficient monitorization of each GPU. When a GPU is working too slow or crashes while calculating a gradient for example, the fault tolerance should be managed, meaning one faulty GPU should not have a huge negative impact on all the others. This would also look like reducing the hardware burden by delegating a piece of a models weights to each of the GPU instead of having all the GPUs contain a 100% copy of a weight which can be expensive.

## How is it currently done?

One method is data parallelism which involves dividing the training dataset to multiple worker nodes

Another method, proposed in the “Scaling Distributed Machine Learning with the Parameter Server” paper in 2014, is a distributed system framework called parameter server in which each individual nodes when finished with their local gradient, uploads their value onto a global parameter server so the current GPU can update the parameters and work on the next batch. This is done until all servers are finishing computing their gradients which leads to a ALl-Reduce in which the average of the gradients are sent to all the nodes to readjust their parameters, weights and gradients.

Another method is proposed in the “ZeRO: Memory Optimizations Toward Training Trillion Parameter Models” paper in which they proposed the ZeRo method in which GPUs get a partition of a parameter to process

## What difficulty or limitations exist?

Hardware limitations are one. As data scales, VRAMs have only a limited amount of storage. It becomes more expensive as you have to purchase different VRAMs to help in the AI training process across multiple servers

The price of hardware has increased during the AI boom

Fault tolerance and durability becomes more of a problem as data scales

Efficient communication

Why does the problem matter?


The use of AI has increased over the years dramatically, being seen in almost every factor of our life. But training large AI models is extremely expensive in terms of hardware costs, electricity and time. If a node fails, it can stall a system or cause an entire dataset to be reprocessed from scratch. The need for AI will still be prevalent regardless of expense in time and costs, so it is in our best interest to reduce these bottlenecks.

Under what condition does this problem occur?

Usually during high volumes of data across multiple machines

## Part 2 — Provide Evidence

Provide evidence that the problem or limitation actually exists.

For each important claim, be clear whether it is:

Documented — supported by a credible published source.

Observed — something you directly observed or measured.

Reported — described by a user, organization, developer, or other credible party.

Hypothesized — something you believe may be true but still need to investigate.

You are allowed to have hypotheses. You simply need to identify them honestly as hypotheses rather than established fact

Provide evidence that problem exists

Documented(12): According to Sagar Joshi’s “Global AI Adoption Statistics: A Review from 2017 to 2025” article, Open AI’s ChatGPT reached over 100 million users in 2023, and in 2025 about “92% of companies plan to invest in Gen AI over the next three years.” This shows an increasing use of AI over the years.


Documented(2): In the “Scaling Distributed Machine Learning with the Parameter Server “ peer-reviewed paper, its noted that “Realistic quantities of training data can range between 1TB and 1PB. This allows one to create powerful and complex models with 10^9 to 10^12 parameters.” This paper was done in 2014, as time continues to pass the amount of data available and used only increased in quantity

Documented(3): In the “ZeRO: Memory Optimizations Toward Training Trillion Parameter Models” peer-reviewed paper, it addresses the concern that AI models are only increasing in size: “To enable the continuation of model size growth from 10s of billions to trillions of parameters.”

All of these

Note: More direct quotes in the planning section of this document

## Part 3 — Investigate Existing Solutions

Identify and compare at least two existing approaches to the problem.

At least one should be a real existing technology, system, research approach, or commonly used method

| Approaches3 | How it addresses the | Strengths/Limitations Questions |   |
| --- | --- | --- | --- |
|   | problem |   |   |
| Parameter server | Utilizes multiple | Limitations: Since it | Would this approach |
|   | nodes to process | was 2014, models | hold in the modern |
|   | gradient. Doesn’t rely | were smaller than | day? |
|   | on a sequential sync | what it is today. |   |
|   | method. Instead once | Because of this it |   |
|   | one node is done | didnt have as much |   |
|   | calculating its | of a strain on the |   |
|   | gradient and weight | hardware and |   |
|   | during forward pass | memory. Doing this |   |
|   | 4 phase it uploads its | method in modern |   |
|   | calculated gradient to | day would be more |   |


| the parameter server | difficult with |
| --- | --- |
| and that GPU is now | increasing size of |
| free to go onto the | models |
| next batch of data to |   |
| process instead of | Strengths: It allowed |
| having to wait idly for | better communication |
| other CPUs. Great | across network. |
| use of a distributed | GPUs no longer had |
| system framework | to wait for other |
| because it can focus | GPUs. Revolutionary |
| on its task while | for its time. |
| having a space to |   |
| communicate ot other |   |
| GPUs. |   |
| ZeRo Problem was making | Limitations: Sacrifices Would this approach |
| a 100% duplicate of a | network bandwidth. be good for any size |
| model across all | Doesn’t work well for training model? |
| GPUs. Puts a strain | smaller models as |
| on the VRAM. ZeRo | well |
| addresses this issue |   |
| by having every GPU | Strengths: Good for |
| hold 1/N of the | VRAM capacity, and |
| billions to trillions of | when dealing with |
| parameters. Making | extremely large |
| space more efficient | parameters |

## Part 4 — Relate the Problem to Your Senior Project

Briefly answer the following:

Does this currently appear closer to Option 1 or Option 2? Explain why.

Does the project currently appear to involve original design, adaptive design, redesign, selection design, or some combination? Explain.

Why might distributed computing be important to this problem?

## Project option:

## Type of design:

## Distributed-systems relevance:


For example, does the problem involve:

- Multiple machines or services

- Communication over a network

- Shared or replicated data

- Concurrent activity

- Failure of individual components

- Geographic distribution

- Scalability

- Reliability

- Coordination

- Large amounts of data or computation

You do not have to demonstrate all of these. Identify only those that genuinely apply.

## Project option

My project option may be more similar to option one. I like the idea of having a centralized server for all GPUs to backward pass into. I feel as if this is a good way of utilizing communication between GPUs, reducing network bandwidth, and preventing stalls when one GPU is underperforming. I also like the idea of reducing the strain on the VRAMs since its more relevant and arguably more important in todays time. THe reason I want to go with option one is because my lateral thinking solution involves using these concepts, especially the ZeRo solution. I want to expand on the ZeRo solution in reducing waste by checking the quality of data first and foremost in hopes of further reducing the quantity of parameters, which can ultimately lead to more space on VRAM and better performance speed.

since ZeRo relies more on peer-to-peer communication, I’m not exactly sure if I can think of a away to incorporate the idea of a parameter server just yet

## Type of design

I believe this approach, trying to reduce the quantity of data by removing the bad quality data, may be a form of redesign. Redesign is an engineering design that targets the improvement of an existing design to expand products capabilities and functionality or reduce manufacturing cost. The existing design in question would be the ZeRo distributed system design method.


## Distributed systems relevance

This problem is fundamentally relevant to distributed systems because its working with multiple machines. Training a model with an immense amount of parameters must require multiple machines, and to ensure the process is efficient and productive, communication between these machines is key.

If a GPU is slowing or crashing, its imperative to pick up the task and delegate it to a new Machine. A well established distributed system framework allows this efficient communication. Updating parameters, weights and gradients and sharing this info to other machines is also allowed to happen with A distributed system framework.

## Part 5 — Identify What You Still Do Not Know

## List two or three important unanswered questions.

For each question, briefly explain how you might obtain evidence.

For each question, briefly explain how you might obtain evidence.

Question(1) - How would I be able to vet whether the training data is useful or not?

How I would investigate(1) - Data science papers talk about the ETL pipeline in detail. What ill be interested in is how they would clean data, but for a larger scale

Question(2) - Does filtering out low quality data during early training stages negatively impact the gradients? Meaning if we don't have these low quality data will it cause the model to ignore certain features leading to many of the gradients being 0?

How I would investigate(2) - Train a small model, one that includes low quality data, and another that doesn't. See the impact on the gradients

## Part 6 — Identify One Early Risk


Identify at least one factor that could make the project difficult to complete.

## Risks

One alarming factor that can make this project difficult is training AI models with a weak GPU

Second alarming factor that can make this project difficult is not having access to multiple machines(Can experiment with pytorch to see how far it takes me)

The third alarming factor that can make this project difficult is timing.

Fourth alarming factor is not having enough storage to handle a large dataset with large parameters for the model

## Part 7 — Connect the Readings to Your Candidate

Choose one useful idea from each of the three assigned readings and explain briefly how it affects your investigation

One useful thing about this reading is giving multiple frameworks on how to view the project. For instance, it gave a list of different types of designs. I was able to differentiate the path I plan to go with the path that wouldn’t apply to my project. I don’t plan to create something new which eliminated the concept of original design. I was conflicted whether or not adaptive design would apply since there are existing solutions, but I don’t exactly plan to use these solutions for an uncommon need. And I think a redesign is the perfect match for what I plan to do since I will attempt to make an improvement on an existing solution. This improvement indirectly reduces cost as well. The software design section and the modular design were also helpful because it provided a good mindset on how to go about the project

I probably found this reading the most helpful. It gave me useful principles that can help reduce being overwhelmed by the work load and process. The reading introduced me to Occam’s Razor/Ockham’s razor which prioritizes simplicity especially for large scale projects. I learned about best practices when designing a product which included investing into the project as early as possible before the launch. Although this can be difficult for project involving a small amount of people on a tight budget. The reading also introduced the idea of keeping components mostly

## Types of Engineering Design - Engineering Capstone Design, Project Planning, Organizing, and Executing

## Research and Analysis of Existing Solutions - Engineering Capstone Design, Project Planning, Organizing, and Executing


independent of each other to help simplify complex designs. Lastly they advocated for methods of thinking such as vertical thinking, lateral thinking and brainstorming. This is especially useful since many AI researchers are thinking of countless way to create a solution to the problem in question. Trying to think of a solution from an “off-angle” helps with a more unique solution to the problem.

Communications - Engineering Capstone Design, Project Planning, Organizing, and Executing This reading helped me the least unfortunately, although I believe I’ll come back to it one day. It mentioned communication is key which I initially thought wasn’t too help as this project was noted to be solo, but I’ll consider reaching out more during peer reviews and professor as needed. Other than that, it provided organization and typical expectations of capstones I can expect.

## Research Requirements

Use at least three substantive sources, including at least two primary or authoritative sources where possible.

## Sources

“Scaling Distributed Machine Learning with the Parameter Server” Mu Li, David G. Andersen, Jun Woo Park, Alexander J. Smola, Amr Ahmed, Vanja Josifovski, James Long, Eugene J. Shekita, and Bor-Yiing Su. 2014. Scaling distributed machine learning with the parameter server. In Proceedings of the 11th USENIX conference on Operating Systems Design and Implementation (OSDI'14). USENIX Association, USA, 583–598. Osdi14-paper-li_mu.pdf [URL 🔗](https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-li_mu.pdf)

“ZeRO: Memory Optimizations Toward Training Trillion Parameter Models” Rajbhandari, S., Rasley, J., Ruwase, O., & He, Y. (2020). ZeRO: Memory optimizations toward training trillion parameter models. In SC20: International Conference for High Performance Computing, Networking, Storage and Analysis (pp. 1–14). IEEE. https://ar5iv.labs.arxiv.org/html/1910.02054 [URL 🔗](https://ar5iv.labs.arxiv.org/html/1910.02054)

https://docs.pytorch.org/tutorials/beginner/dist_overview.html https://developer.nvidia.com/nccl [URL 🔗](https://docs.pytorch.org/tutorials/beginner/dist_overview.html)


Joshi, S. (2025, May 28). Global AI adoption statistics: A review from 2017 to 2025. G2 Learn Hub. https://learn.g2.com/ai-adoption-statistics [URL 🔗](https://learn.g2.com/ai-adoption-statistics?utm_source=gemini)

======BRAIN STORMING BELOW ===

Also potential audience is people who work in companies like tesla, where information is Background knowledge:

Using large dataset as training data for Ai training model requires lots of nodes(computers) and their GPUs. Training data works better on GPU than CPU

If we offload data into AI model, different nodes get different training data.(Nodes can also be

substituted with replicas in this case, which is basically individual models running on different GPUs) This concept of each GPU getting own training data to work with is known as data parallelism Each gpu arrive/calculate a different set of updates known as gradients. Gradients are the calculated direction and size to help reduce error during the training process based on a given batch size . The problem is if each gpu doesnt understand what each of their other correspondents learned, the Ai models would end off being weaker. They can either learn separately which would drive back progress or they can learn in tandem which means what one gpu learns can help improve the learning rate of another. So the solution to this is synching updates/gradients which can be seen as alerting other GPUS what they had learned

Another term is All-Reduce: An optimized communication algorithm used by distributed frameworks (like PyTorch or TensorFlow) where all GPUs send their local gradients to each other, average them out, and send the unified average back to every GPU.

## Process

- 1. Every gpu gets same parameters

- 2. Every gpu gets own batch size of training data

- 3. Every gpu process its own local gradients based on their independent dataset

- 4. Sync step involves every gpu running all reduce to calculate average gradient, and sends it back to each and every gpu

- 5. Every gpu updates parameters based on gradient

- 6. All gpus remain synbchronize for next batch

Network communications

RDMA, that allows independent computers or gpus exchange information/digital data with each other. Acts as physical path that allows gpus to communicate their gradients to keep models in synch.

\- hardware cables and software protocols like TCP/IP, InfiniBand, or


Latency - The amount of time it takes for a single message/packet to travel from point A to point B across a network. In AI context it tis time that takes for gpu 1 to send computed gradient to

gpu 2

Bottleneck - slowest part of system that limits overall speed capacity and performance of overall system. I.e if gpu computes gradient in 2 seconds, but network causes latency of 10 seconds, then network is bottleneck. Gpu sits completely idle in this time

Overhead - unnecessary time you have to go through in order to get to actual tasks

Pytorch relevancy

- Pytorch is a distributed system frame work

Sources

[https://docs.pytorch.org/tutorials/beginner/dist_overview.html](https://docs.pytorch.org/tutorials/beginner/dist_overview.html)

osdi14-paper-li_mu.pdf “Scaling Distributed Machine Learning with the Parameter Server “ Talks about network bandwidth in big data centers being 10x to 100x slower compared to local [URL 🔗](https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-li_mu.pdf)

bandwidth a student has at home.

[1910.02054] ZeRO: Memory Optimizations Toward Training Trillion Parameter Models Rajbhandari, S., Rasley, J., Ruwase, O., & He, Y. (2020). ZeRO: Memory Optimizations Toward Training Trillion Parameter Models. IEEE/ACM International Conference for High Performance [URL 🔗](https://ar5iv.labs.arxiv.org/html/1910.02054)

Computing, Networking, Storage and Analysis (SC '20). / Microsoft Deep

[[1910.02054] ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://ar5iv.labs.arxiv.org/html/1910.02054)

[Global AI Adoption Statistics: A Review from 2017 to 2025](https://learn.g2.com/ai-adoption-statistics)

[NVIDIA Collective Communications Library (NCCL) | NVIDIA Developer](https://developer.nvidia.com/nccl)

Quotes

For “scaling Distributed Machine Learning with the parameter server”

- (1) We propose a parameter server framework for distributed machine learning problems. Both data and workloads are distributed over worker nodes, while the server nodes maintain globally shared parameters, represented as dense or sparse vectors and matrices. The framework manages asynchronous data communication between nodes, and supports flexible consistency models, elastic scalability, and continuous fault tolerance. To demonstrate the scalability of the proposed frame work, we show experimental results on petabytes of real data with billions of examples and parameters on prob lems ranging from Sparse Logistic Regression to Latent Dirichlet Allocation and Distributed Sketching. In short, proposed the idea that its better to create a parameter server framework for distribuyted machine learning problems. The process


- involves creating multiple nodes that share global parameters, and use the frame work to communicate with each node to calculate gradients. Their proof of this working was them experimenting with petabytes of real data. This distributes system helps prevent slowing down or crashing. Connection: This can be seen as the original, industry standard solution. Can follow vertical thinking if II further explore this

- (2) Distributed optimization and inference is becoming a pre requisite for solving large scale machine learning prob lems. At scale, no single machine can solve these prob lems sufficiently rapidly, due to the growth of data and the resulting model complexity, often manifesting itself in an increased number of parameters. In short, author(s) mentions how machine learning problems will only increase due to the growing scale of data. This is even more prevalent today with the wide use of AI by even non-computer scientist, its application amongs a vast number of companies and their reliance on AI training on their customers, investments into information gathering companies such as Telsa, where learning as fast as possible contributes to the safety of the people. Connection: This can be seen as evidence to the problem

- (3) Realistic quantities of training data can range between 1TB and 1PB. In short, shows the scale of the problem. This was in 2014. It only increased since then.

- (4) Sharing imposes three challenges: • Accessing the parameters requires an enormous amount of network bandwidth. • Many machine learning algorithms are sequential. The resulting barriers hurt performance when the cost of synchronization and machine latency is high. • At scale, fault tolerance is critical. Learning tasks are often performed in a cloud environment where ma chines can be unreliable and jobs can be preempted. In short, the author highlights the problem with sharing gradients across GPUs. One being accessing high dimensional parameters and gradients requires a lot of network bandwidth, increasing latency. Which is the bottle neck since gpu can process data and must wait. Another problem being the current state of machine learning algorithms at that time were sequential synchronization, meaning one gpu that finish computing its gradient must wait for the other gpu to finish processing before moving onto next step. (Solution to this would be asynch, where if one gpu finishes processing, it uploads gradient to parameter server , then that gpu gets updated parameters and can start the next batch. As opposed to waiting for all reduce.) . Increasing latency since different gpus will finish at different times. And lastly fault tolerance, which are essential when a gpu crashes or slolws down alot becomes even bigger problem as you scale up the data.

- (5) Paper is advocating parameter server frame work which is a distributed async technique

- (6) Since its introduction, the parameter server frame work [43] has proliferated in academia and industry. This paper describes a third generation open source implemen tation of a parameter server that focuses on the systems aspects of distributed inference. It confers two advan tages to developers: First, by factoring out commonly required components of machine learning systems, it en ables application-specific code to remain concise. At the same time, as a shared platform to target for systems level optimizations, it provides a robust, versatile, and high-performance implementation capable of handling a diverse array of algorithms from sparse logistic regression to topic models and distributed sketching. Our design decisionswereguidedbytheworkloadsfoundinrealsys tems. In short, offers two advantages after building upon previous solutions(this is third gen) One advantage is handles all the dirty work like task scheduling, communication,m under the hood via the distributed system technique, to make it easier for developers. THe second advantage also makes it easier for developers by allowing addition to the algorithm not having to require its own distributed tool system and can just rely on the server. Connection: this shows how this innovative solution made it easier for companies and developers which are the primarily target audience.

- (7) Proposed solutions advantages “Our parameter server provides five key features:

- Efficient Communication: The asynchronous communication model does not block computation (unless requested). It is optimized for machine learning tasks to reduce network traffic and overhead.

- Flexible Consistency Models: Relaxed consistency further hides synchronization cost and latency. We allow the algorithm designer to balance algorithmic convergence rate and system efficiency. The best trade-off depends on data, algorithm, and hardware.

- Elastic Scalability: New nodes can be added without restarting the running framework.

- Fault Tolerance and Durability: Recovery from and repair of non-catastrophic machine failures within 1s, without interrupting computation. Vector clocks ensure well-defined behavior after network partition and failure.


- Ease of Use: The globally shared parameters are represented as (potentially sparse) vectors and matrices to facilitate development of machine learning applications. The linear algebra data types come with high-performance multi-threaded libraries.

(8)

“

- (9) First problem stated - Two key challenges arise in constructing a high performance parameter server system: Communication. While the parameters could be updated as key-value pairs in a conventional data store, using this abstraction naively is inefficient: values are typically small (floats or integers), and the overhead of sending each update as a key-value operation is high. Our insight to improve this situation comes from the observation that many learning algorithms represent parameters as structured mathematical objects, such as vectors, matrices, or tensors. At each logical time (or an iteration), typically a part of the object is updated. That is, workers usually send a segment of a vector, or an entire row of the matrix. This provides an opportunity to automatically batch both the communication of updates and their processing on the parameter server, and allows the consistency tracking to be implemented efficiently. In short, saying that shouldnt treat updating parameters and gradients as typical database with key-value info. Problem is values are typically small, wasted space. Solution to this is more linear algebra approach. Data is related, send data as an array/matrix instead of bit by bit. Can process vector in bulk

- (10) Another problem stated - “Fault tolerance, as noted earlier, is critical at scale, and for efficient operation, it must not require a full restart of a long-running computation. Live replication of parameters between servers supports hot failover. Failover and self repair in turn support dynamic scaling by treating machine removal or addition as failure or repair respectively.”

- (11) States previous solutions, previous gen on 1.3. Criticized Graphlab even though it supported asynch because of poor elasticity, couldnt easily replace machine. And it couldnt save states as efficiently, often being huge and slow snapshots

Bottleneck - gpu is fast but network is slow, causing idling

For “ZeRO: Memory Optimizations Toward Training Trillion Parameter Models”

First the problem addressed here. Ai model training is dealing with gigantic datasets,

parameters, gradients etc. It’s becoming extremely expensive on the hardware, specifically VRAM to have an exact duplicate of each of model with the parameters and their respective gradients. This becomes increasingly a problem as hardware becomes more expensive. Data parallelism and model parallelism no longer enough.

Traditional parallelism -(1) buy several gpus like 10 (2) every gpu must store 100% of parameters, gradients etc. (3) 9 out of the 10 gpus holde redundant info.

## The bottle neck here is VRAM capacity and memory, instead of network latency like in first paper

- (1) Large deep learning models offer significant accuracy gains, but training billions to trillions of parameters is challenging. Existing solutions such as data and model parallelisms exhibit fundamental limitations to fit these models into limited device memory, while obtaining computation, communication and development efficiency. We develop a novel solution, Zero Redundancy Optimizer (ZeRO), to optimize memory, vastly improving training speed while increasing the model size that can be efficiently trained. ZeRO eliminates memory redundancies in data- and model-parallel training while retaining low communication volume and high computational granularity, allowing us to


Prof. Brown 9/26/26

scale the model size proportional to the number of devices with sustained high efficiency. Our analysis on memory requirements and communication volume demonstrates: ZeRO has the potential to scale beyond 1 Trillion parameters using today’s hardware.

- (2) We implement and evaluate ZeRO: it trains large models of over 100B parameter with super-linear speedup on 400 GPUs, achieving throughput of 15 Petaflops. This represents an 8x increase in model size and 10x increase in achievable performance over state-of-the-art. In terms of usability, ZeRO can train large models of up to 13B parameters (e.g., larger than Megatron GPT 8.3B and T5 11B) without requiring model parallelism which is harder for scientists to apply. Last but not the least, researchers have used the system breakthroughs of ZeRO to create the world’s largest language model (17B parameters) with record breaking accuracy.

- (3) Above is saying ZeRo goal to eliminate waste/hardware bottleneck is to introduce a distributed system network in which it grants each gpu a piece of the total parameter and gradient. The distributed system in questions allows for each gpu to communicate with each other to fill in missing blanks that may be needed. That process is called All gather. All gather specifically allows forr one layer that gpu 1 holds to communicate to the other layers the math required to compute layer 1. Then all the other layers delete the layer they used to help compute for gpu 1. Layer 1 holds a layer of the weights and is given to gpu 1. Gpu 1 is essentially the owner of the layer and will always keep this layer.

## Potential Idea(s)

Problem: Training AI models and using task scheduler as a distributed design tool Context: AI models are being used more recently. A ussr can unload large training data/dataset that can be expensive to process. One computer/server can not handle this tasks alone. Impossible for single computer or single gpu to handle. If server 1 is processing 90% of the task

with a batch size of about 1,000, it can over heat and crash.

Solution: Distributed task scheduler. If distributed system detects server 1 stops working or becomes idle, it offloads the work to another server. This required monitoring.

## Basics

- Software designed to coordinate, manage, monitor communication between multiple computers(nodes) over a network

- Instead of single computer running application, modern software runs across hundreds or thousands of servers.

## What is a distributed tool?

## What computer in question?


## What is distributed tool purpose?

- Handles heavy lifting for communication.

- Makes sure these different computers/serverrs can talk to each other, share data, track whose active and how to recover if one is down

- 1. Coordinate on key facts across all computers. Like “who is the leader?”

- 2. Help independent services find each other network dynamically

- 3. Moving data reliably between servers

## Responsibilities of distributed tools:

## Example for understanding

5 people work on a document. 1 person deletes a paragraph that person B was editing and adding on too. Person B doesn't see this until 5 seconds later. There can be many conflicts like this that will occur. The solution is google synching engine tool.

## Google doc

## Chapter 2

Advocates learning as many existing solutions as possible. Learn their advantages and disadvantages and make list of potential improvements

Interactions between humans and other system elements

Study of optimizing human comfort and safety and productivity

Considers all of human physical capabilities and limitations and implements in product to make it easy for them to use

Need info about human characteristics of user

Entities are not to be multiplied beyond necessity Prioritizes simplicity Simpler explanation should be preferred from two hypothesis

## Research

## Ergonomics

## Occam’s Razor/Ockham’s razor


In engineering, using Occam’s razor means doing something (design, test, analyze, model, etc.) in the simplest manner possible, and usually, the simpler the better.

For example, in the first stage of conceptual design, the initial calculation should be made by pencil on a single sheet of paper, without any complicated modeling and/or simulation.

NOT ALWWAYS A GOOD PRINCIPLE. As part count increases, reliability generally decreases.

## “Best Practices” of Product Development:

Goal is to make as many changes to product in early sta ges of development. Otherwise changes post market product becomes very expensive. Of course this decision is timely

Should find balance between Occam’s razor(solving problems only when time comes) and best practice principle(invest in product as much as you can in early stages

Graph shows line with first desires progress being heavy on early investments, and investments sloww down during mass production stage. Second line shows more realistic scenario in which company gradual invests over time, with its peak nearing the mass production stage

Independent Functions: Keep the Functions of a Design Independent from One Another

Mechanical engineering - Product described by its function. This drives the functions objective when designing the product.

In general complex systems should be broken down to small manageablel parts. Such as Primary function which is what the product needs to accomplish not just aesthetics. Its broken up into function-based (what the product should do) sub descriptions(which is overall saying what each component that contri butes to the overall function of the product should accomplish). Leads to hierarchy of functions designer can use to develop final product

Into project should be split into mayn sub functions

Independent functionality leads to decomposition. which: “The goal of decomposition is to simplify the complex design problem to facilitate the decision-making process, to increase system reliability and, potentially, to save different types of resources.”

Computer science - uses the principle of “seperation of concerns” or SOC. A design principle where separates a program into sections where each section addresses a separate concern. Think of modularity. Concern is defined as “information that affects the program code” meaning code driven around solving a certain problem or tasks.


In design process face, most important thing is idea generation. Its a very demanding task with a goal of making better, more novel solutions

Requires:

- Broad outlook

- Open minded approach

For best research, designer should not shy away from most original solution, nonstandard solutions(brute force?) but its constraint should be a realistic, based in nature solution.

Brain storming is effective for mental blocks. Goal is to generate high volume of ideas, unusual, out of the box. You dont keep most of the ideas. Section doesnt further elaborate on this

## Lateral thinking**** helpful

One process of generating ideas is to think of solutions not directly. Evaluate situation from nonstandard direction. Often engineers avoid traditional methods to achieve this, ignoring biased judgements and opinions

Edward De Bono in his boo de bono(1967) states that point of lateral thinking is many problems require different perspectives to be solved successfully.

“Lateral thinking stems from a combination of two standard modes of thinking and problem-solving, namely, vertical thinking that is a classical step-by-step method of problem-solving from the given data, and brainstorming where many ideas are generated without the goal of mandatory implementation of all of them.”

To rephrase above, lateral thinking stems from two modes of thinking. Vertical thinking which is step by step, almost iterative problem. Where you start off with a given data, pre existing truth, problem statement, then follow a direct path based on this to explore a solution, justfying if its correct each time you go down the path to aim for a definitive solution, and brainstorming which is generating multiple ideas without worrying about testing them out/exploring deeper to see if it’ll work. Trying not to think or challenge the idea thoroughly. Lateral thinking in general involves changing your starting approach which can look like a new possible problem, or look at new data that can help with solution. It’s more of an application of mindset. How lateral thinking connects with brainstorming and vertical thinking is similar to brainstorming, it involves not committing to a single pathway of an idea, step out of your comfort zone to create volume of ideas. And most importantly, It does not take the traditional approach to the solution. Whereas similar to vertical thinking it relies on realistic logical principals. Using ideas that only seem realistic to real world or rather software world. But unlike vertical thinking, it doesnt commit to an idea and follow an established track, allowing you to start off from different starting points so you wont think your first/previous starting points are the best approach to the problem,

becoming bias.

De bono describes the difference between vertical and lateral thinking as (a) vertical thinking involves implementation and using existing ideas (b) lateral thinking is concerned with thinking


of new ideas outside the box. “Digging a whole somewhere else” instead of digging a whole deeper

De bono uses 4 principles of lateral ideas:

- Recognize the dominant ideas that polarize the perception of a problem

- Search for different ways of looking at things.

- Relax the rigid control applied to vertical thinking

- Use chance to encourage other ideas. This last factor in lateral thinking involves low-probability ideas that are unlikely to occur in the normal course of events.
