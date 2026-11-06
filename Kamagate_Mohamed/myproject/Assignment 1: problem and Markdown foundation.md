**1. Apply it to your project.** *Identify one caller, one program that responds, one piece of saved information, and one situation in which a response might not arrive. If your project is a simulator, identify the simulated participants and the messages the simulation represents. You are ready to continue when you can explain these four things without relying on product names.*  

Caller: A NYC first respondent or  a general user who both wants  to  send plain language query to the adaptive knowledge broker

One program that responds: The adaptive knowledge broker that breaks down the given query(requests) into semantics 

One situation in which a response does not arrive: when the broker attempts to deliver the final synthesized report back to a responder whose cellular connection has dropped (i.e during live hurricane event or flooding may disrupt connection).

One piece of saved information: Reasoning domain agents query their specialized tailored sources and write down their findings to be saved. 


**2. Apply it to your project.** *Write one sentence for each of the four design steps. Use the form “At this step, I need to explain…” A useful architectural sentence names responsibilities; a useful algorithm sentence names a decision or sequence. Avoid writing the same list of technologies four times*

Architectural design : At this step, I need to explain how the four-tier system distributes responsibilities among the Adaptive Knowledge Broker, reasoning Domain Agents, Functional Agents, and the federated data layer.

Component design: At this step, I need to explain how each AI agent is responsible for different things such as the Broke being responsible for breaking down semantic intent, domain agents being chosen and querying their tailored repositories, and broke stitching the results back together. 

Data structure design: At this step, I need to explain all the information each part uses such as Broker using query, domains using their repositories. 

Algorithm design: At this step, I need to explain the process of coordinating agentic delegation of tasks and agentic retrieval.

