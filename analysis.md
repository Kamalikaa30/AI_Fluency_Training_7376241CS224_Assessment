# Agentic AI: Foundations and Open-Source Practice — Day 1

## 1. Private-Data Scenario

For this project, I selected a Student Placement Tracker as my private-data scenario.

The application contains fictional student placement information that is treated as private data.

| Student | Skill | LeetCode Score | Aptitude Score | Eligible |
|---|---|---:|---:|---|
| Anu | Java | 85 | 78 | Yes |
| Bala | Python | 62 | 82 | No |
| Charan | Java | 91 | 88 | Yes |
| Divya | React | 74 | 91 | Yes |

The same placement-related questions are handled using three approaches:

1. Plain chatbot
2. Rule-based workflow
3. Tool-using AI agent

The purpose is to compare how each approach accesses private data, handles decisions, performs multiple steps, and responds to questions.

---

## 2. Plain Chatbot

### Data Used

The plain chatbot uses the LLM and the user's question. It does not have direct access to the private student placement dictionary stored in the Python program.

Therefore, the chatbot cannot reliably retrieve the actual student information from the private dataset.

### Tools or Rules

The plain chatbot does not use any external tools or private-data lookup functions. It mainly sends the user's question to the LLM and returns the generated response.

### How It Handles a Request

The user provides a question. The question is sent to the LLM. The LLM generates a natural-language response and the response is displayed to the user.

For example, when asked about a student's LeetCode score, the chatbot has no direct connection to the student database.

### Limitation

The main limitation is that the chatbot cannot directly access the private student data. Therefore, it may provide an uncertain or incorrect answer when the requested information is not available in its context.

This shows that an LLM alone should not be treated as a reliable source for private application data.

---

## 3. Rule-Based Workflow

### Data Used

The rule-based workflow directly accesses the `STUDENTS` dictionary in `config.py`.

The dictionary contains the private placement information for Anu, Bala, Charan, and Divya.

### Tools or Rules

The workflow does not use an LLM. It uses predefined Python rules and conditions.

The rules identify student names, check requested information, retrieve the corresponding values, and perform predefined calculations or filtering.

### How It Handles a Request

The workflow receives the user's question and matches it against predefined rules.

For example, when the question asks for a student's LeetCode score, the workflow identifies the student and retrieves the score from the private dictionary.

It can also calculate the average LeetCode score of specified students and find students whose LeetCode score is above a specified value.

### Limitation

The workflow is reliable for cases covered by its predefined rules, but it is rigid.

This was demonstrated by the challenge question:

> I need students who have a LeetCode score above 80 and an aptitude score above 80. Which students qualify?

The workflow had a rule for LeetCode score above a value, but it did not have a rule combining the LeetCode condition with the aptitude condition.

As a result, it returned students based on the LeetCode condition without fully applying the second condition.

This shows that new requirements may require the developer to manually add new rules.

---

## 4. AI Agent

### Data Used

The AI agent accesses the private student data through controlled tools.

The LLM does not directly receive the complete private student database. Instead, it can request information using the `get_student_data` tool.

### Tools Used

The agent uses two tools:

1. `get_student_data` — retrieves private information about a student.
2. `calculator` — performs arithmetic calculations.

### LLM + Tools + Loop

The AI agent follows the concept:

**Agent = LLM + Tools + Loop**

The LLM receives the user's question and decides whether a tool is required.

If private student information is required, the LLM selects `get_student_data`.

The Python program executes the tool and returns the result to the LLM.

If arithmetic is required, the LLM can use the `calculator` tool.

The tool result becomes an observation that the LLM can use to decide its next action.

The process continues until the agent can provide a final answer or the maximum number of steps is reached.

### How It Handles a Request

For example, for a question about Anu's LeetCode score, the agent calls:

`get_student_data("Anu")`

The tool returns Anu's private information, including the LeetCode score.

For an average calculation involving Anu and Charan, the agent can retrieve both students' information and then use the calculator tool.

The agent therefore performs multiple tool calls when required instead of following one fixed rule for every possible question.

### Challenge Result

For the challenge:

> I need students who have a LeetCode score above 80 and an aptitude score above 80. Which students qualify?

The agent retrieved the student information and evaluated both conditions.

The results were:

| Student | LeetCode | Aptitude | Result |
|---|---:|---:|---|
| Anu | 85 | 78 | Does not qualify |
| Bala | 62 | 82 | Does not qualify |
| Charan | 91 | 88 | Qualifies |
| Divya | 74 | 91 | Does not qualify |

Therefore, Charan qualifies because both conditions are satisfied.

This demonstrates the agent's ability to handle a multi-condition task using private data and tool calls.

### Limitation

The agent is more flexible than the fixed workflow, but it depends on the LLM making appropriate tool selections and following the system instructions.

Therefore, an agent can be less predictable than a completely fixed workflow.

---

## 5. Comparison Table

| Basis for comparison | Plain chatbot | Rule-based workflow | AI agent |
|---|---|---|---|
| Flexibility | Flexible for natural-language responses but lacks private-data access | Limited to predefined rules | Flexible and can select tools based on the task |
| Decision-making | LLM generates the response | Developer-defined conditions determine the result | LLM decides which tool or action is required |
| Tool usage | No tools | No LLM tool-calling mechanism | Uses `get_student_data` and `calculator` |
| Private-data access | No direct access | Direct access to the private Python dictionary | Accesses private data through controlled tools |
| Multi-step task handling | Limited when information is missing | Only possible when explicitly programmed | Can perform multiple tool calls through a loop |
| Automation | Basic response generation | Effective for known and repeated processes | Can automate flexible multi-step tasks |
| Reliability | May produce unsupported or incorrect private-data answers | Predictable for cases covered by rules | Tool-based answers can be grounded in private data, but LLM decisions introduce variability |

---

## 6. Observations

The experiment demonstrates clear differences between the three approaches.

The plain chatbot mainly provides an LLM-generated response. It does not have access to the private student placement database, so it cannot reliably answer questions that depend on that data.

The rule-based workflow directly accesses the private data and gives predictable results for the rules that were implemented. However, its behavior is limited by those predefined rules.

The AI agent combines an LLM with tools and a loop. It can retrieve private student information through `get_student_data`, perform calculations using `calculator`, observe the returned results, and continue with another action when necessary.

The challenge particularly demonstrates the difference between the workflow and the agent. The workflow did not fully apply the two conditions because that combination was not explicitly programmed as a rule. The agent was able to retrieve the relevant data and evaluate both conditions, identifying Charan as the qualifying student.

---

## 7. Suitability Analysis

For this Student Placement Tracker scenario, an AI agent is suitable when users may ask different types of questions involving private data, filtering, calculations, and multiple conditions.

A plain chatbot is suitable for general conversation, explanations, and natural-language generation when private application data is not required.

A rule-based workflow is suitable when the questions and operations are known in advance and predictable behavior is important. It is simple and deterministic for the cases covered by its rules, but new requirements require additional programming.

An AI agent is suitable when the task requires natural-language understanding, controlled access to private data, tool usage, and multiple steps. It can adapt its tool usage based on the question instead of requiring one separate rule for every possible question.

However, the agent still requires appropriate system instructions, tool definitions, and safeguards because the LLM is involved in deciding which actions to take.

---

## 8. Conclusion

A plain chatbot is appropriate when the main requirement is conversation, explanation, or content generation and no private-data lookup or external action is required.

A rule-based workflow is appropriate when a process is fixed, predictable, and can be represented using predefined conditions and actions. It is useful when deterministic behavior is important.

An AI agent is appropriate when a problem requires natural-language understanding, access to private data through tools, multiple steps, and the ability to decide which action should be taken next.

The main distinction can be summarized as:

**Chatbot:** LLM → Response

**Workflow:** Predefined Rules → Data/Actions → Result

**AI Agent:** LLM → Tool → Observation → Next Action → Final Response

The Student Placement Tracker demonstrates the Unit 1 concept that an AI agent combines an LLM, tools, and a loop to solve flexible multi-step tasks while accessing private data through controlled tools.