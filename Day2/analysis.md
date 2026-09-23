# Day 2 Assessment: Reasoning and Acting

## 3.1 Direct Prompting, Chain-of-Thought, and ReAct

This assessment compares three approaches using a College Library Assistant scenario.

### Direct Prompting

Direct prompting sends the question directly to the language model and asks for an answer without using external tools.

In this project, direct prompting was tested on three reasoning questions:

1. A student reads books taking 4, 6 and 5 days and has 17 days available.
2. Anu finished before Bala, and Bala finished before Charan.
3. A student has 2 extra days and the three books take 4, 6 and 5 days.

The model answered these questions directly without using the library tool.

### Chain-of-Thought

Chain-of-Thought prompting asks the model to solve the problem step by step.

In this project, the same three reasoning questions were given to the model with instructions to show the calculation or reasoning clearly.

For example:

4 + 6 + 5 = 15 days

17 - 15 = 2 days

Therefore, 2 days remain.

This approach makes the reasoning process easier to follow for calculation and ordering problems.

### ReAct

ReAct combines reasoning with tool usage.

In this project, the ReAct agent was given the question:

> Is book B202 available in the college library?

The agent selected the `get_book_availability` tool and passed `B202` as the book ID.

The tool returned:

> Data Structures (B202): 0 copies available

The agent then used this observation to give the final answer that B202 is not available.

---

## 3.2 Comparison of the Three Approaches

| Feature | Direct Prompting | Chain-of-Thought | ReAct |
|---|---|---|---|
| Reasoning | Direct answer | Step-by-step reasoning | Reasoning + action |
| Tool usage | No | No | Yes |
| External information | No | No | Yes |
| Transparency | Lower | Higher | High |
| Speed | Fast | Slower than direct prompting | Slower because of tool call |
| Best suited for | Simple questions | Multi-step reasoning | Questions requiring external data |
| Example in this project | Book-reading calculation | Book-reading calculation with steps | Checking B202 availability |

Direct prompting was useful for getting quick answers to the reasoning questions.

Chain-of-Thought was useful for understanding the calculations and logical steps.

ReAct was useful for the library availability question because the answer depended on the library data stored in the tool.

---

## 3.3 Self-Consistency Observation

Self-consistency was tested using the same reasoning question multiple times.

The question used was:

> A student reads three books taking 4, 6 and 5 days. If the student has 17 days available, how many days will remain after finishing all three?

The script generated five responses using a non-zero temperature of 0.8.

The expected calculation is:

4 + 6 + 5 = 15 days

17 - 15 = 2 days

The five generated responses were compared to observe whether the model consistently produced the same answer.

The majority result was used to observe the consistency of the model responses.

---

## 3.4 Suitability

### Direct Prompting

Direct prompting is suitable for simple reasoning questions where all required information is already provided in the question.

In this project, it was suitable for questions involving book-reading time and ordering students.

### Chain-of-Thought

Chain-of-Thought is suitable when the question requires multiple calculations or logical steps.

In this project, it was useful for calculating the total reading time and remaining days.

### ReAct

ReAct is suitable when the answer requires information from an external tool.

In this project, ReAct was used to check whether book B202 was available in the library.

The tool returned 0 available copies, allowing the agent to provide the correct library availability answer.

---

## 3.5 Conclusion

This project compared Direct Prompting, Chain-of-Thought, and ReAct using a College Library Assistant scenario.

Direct Prompting provided direct answers to reasoning questions.

Chain-of-Thought provided step-by-step reasoning for the same type of questions.

ReAct used the `get_book_availability` tool to obtain external library information and then generated the final answer.

The self-consistency experiment used five runs of the same reasoning question to observe whether the model produced consistent answers.

The experiment shows that different approaches are useful for different types of tasks. Direct Prompting is suitable for straightforward questions, Chain-of-Thought is useful for multi-step reasoning, and ReAct is useful when external information or tools are required.