"""Challenge: a question requiring private data and multi-step reasoning."""

from workflow import workflow
from agent import agent


QUESTION = (
    "I need students who have a LeetCode score above 80 "
    "and an aptitude score above 80. Which students qualify?"
)


print("Q:", QUESTION)

print("\nWorkflow:")
print(workflow(QUESTION))

print("\nAgent:")
print(agent(QUESTION))
