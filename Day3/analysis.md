# Day 3 Assessment: From Prompt to Action

## Scenario: Campus Opportunity Radar

The Campus Opportunity Radar is a small AI assistant that helps students check campus opportunities such as innovation challenges and developer programs.

The project uses a private JSON dataset named `opportunities.json`. The LLM does not directly receive this dataset. Instead, it can access the information through one external tool called `get_opportunity_status`.

---

## 3.1 Explanation of Concepts

### What is a Large Language Model?

A Large Language Model (LLM) is a model trained on large amounts of text to understand questions and generate natural-language responses.

In this project, the plain LLM could answer questions when the required information was already present in the question.

For example, it could determine whether a third-year student belongs to the range of second to fourth year students. It could also compare two dates given directly in the question.

However, the LLM could not reliably know the private information stored in our `opportunities.json` file. When asked about the BIT AI Innovation Sprint, the plain LLM stated that it could not confirm its current status or deadline.

This shows that an LLM should not be expected to know private or newly created information unless that information is provided to it.

### What is an Agent?

An LLM agent is a system where a language model can interact with external tools or information sources instead of only generating text.

In this project, the plain LLM only generated an answer from the prompt.

The tool-enabled LLM could recognize when private opportunity information was required, call the `get_opportunity_status` tool, receive the result from the JSON dataset, and then generate its final answer.

The basic flow is:

```text
User Question
      ↓
LLM
      ↓
Does external information need to be checked?
      ↓
Tool call when required
      ↓
opportunity_tool.py
      ↓
opportunities.json
      ↓
Tool result
      ↓
LLM
      ↓
Final Answer
What is a Tool and a Tool Call?

A tool is an external function that an LLM can use to obtain information or perform an operation.

The single tool in this project is:

get_opportunity_status(opportunity_id)

The tool reads the private opportunities.json dataset and returns the status, deadline, and eligibility of an opportunity.

The tool schema describes:

the tool name
what the tool does
the parameter it accepts
the type of the parameter

For example, the schema tells the model that opportunity_id is required and that values such as BIT-AI-01 can be supplied.

The model needs this description so that it can understand when the tool is useful and how to call it correctly.

A tool call occurs when the model requests the external function with the required argument.

For example:

Tool: get_opportunity_status
Argument: BIT-AI-01
How One Tool Call Works

The tool call in this project follows these steps:

The user asks whether the BIT AI Innovation Sprint is open and asks for its deadline.
The LLM determines that this information is not available in the prompt.
The LLM selects the get_opportunity_status tool.
The LLM sends BIT-AI-01 as the opportunity ID.
The Python tool opens opportunities.json.
The tool finds the matching opportunity.
The tool returns the opportunity information as plain text.
The result is sent back to the LLM.
The LLM uses the result to generate the final answer.

The tool returned:

Opportunity: BIT AI Innovation Sprint
Status: OPEN
Deadline: 5 October 2026
Eligibility: 2nd to 4th year UG students
Why Should a Tool Return Plain Text?

A tool should return its result as plain text instead of stopping the entire program when something goes wrong.

For example, if an unknown opportunity ID is requested, the tool returns:

Opportunity XYZ was not found.

This allows the LLM to understand what happened and respond appropriately.

Returning a readable result also keeps the agent workflow running instead of terminating the program with an exception.

3.2 Comparison Table
Basis	Plain LLM Prompt	LLM with One Tool
Source of the answer	Model knowledge and information in the prompt	Model knowledge plus information returned by the tool
Can it fetch or compute information outside its own context?	No	Yes, through the provided tool
Reliability on factual questions	Cannot reliably know our private opportunity data	Can retrieve the stored opportunity information
Transparency	Shows the generated answer	Tool call, tool result, and final answer can be observed
Speed / cost	Faster because no tool call is required	Slightly more processing when a tool call is required
3.3 Observation

Three questions were tested using the plain LLM and the tool-enabled LLM.

Question 1 — Information Requiring the Tool

Question:

Is BIT AI Innovation Sprint currently open, and what is its deadline?

Plain LLM

The plain LLM stated that it did not have access to the required real-time or private information and could not reliably confirm the status and deadline.

This was expected because the opportunity information was stored in our private opportunities.json file and was not included in the prompt.

Tool-Enabled LLM

The tool-enabled LLM recognized that external information was required and called:

get_opportunity_status

with:

BIT-AI-01

The tool read the JSON dataset and returned:

Status: OPEN
Deadline: 5 October 2026

The LLM then used this result to provide the final answer.

This demonstrates how one external tool can provide information that is not available to the plain LLM.

Question 2 — Reasoning Without the Tool

Question:

A third-year student wants to apply to an opportunity open to 2nd to 4th year students. Is the student eligible?

The required information was already present in the question.

A third-year student falls within the second-to-fourth-year range, so the question can be answered through simple reasoning.

The external opportunity tool was not necessary.

This demonstrates that giving an LLM a tool does not mean that the tool must be used for every question.

Question 3 — Reasoning Without the Tool

Question:

A student has opportunities with deadlines of 5 October and 12 October. Which deadline comes first?

The two dates were already provided in the question.

The LLM could determine that 5 October comes before 12 October without accessing the opportunity database.

Therefore, the tool was not necessary for this question.

3.4 Suitability

A plain LLM prompt is suitable when the question can be answered using general knowledge or reasoning from information already provided in the prompt.

In this project, Questions 2 and 3 could be answered without the external tool.

An external tool becomes useful when the answer depends on information that is outside the model's available context.

In this project, Question 1 required the private campus opportunity dataset. The get_opportunity_status tool accessed opportunities.json and supplied the actual information to the LLM.

The tool should therefore be used when external, private, current, or otherwise unavailable information is required.

3.5 Conclusion

This project demonstrated the difference between a plain LLM prompt and an LLM connected to one external tool using the Campus Opportunity Radar scenario.

The plain LLM handled simple reasoning questions successfully when the required information was already included in the prompt. However, it could not reliably confirm information stored in the private opportunity dataset.

The tool-enabled LLM could recognize when external information was required, call get_opportunity_status, read the information from opportunities.json, receive the result, and use it to produce the final answer.