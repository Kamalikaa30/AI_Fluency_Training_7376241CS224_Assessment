"""Day 2 Assessment: ReAct library agent."""

import json
import os
import sys

# Project root
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

# Use Day1 config
DAY1_FOLDER = os.path.join(PROJECT_ROOT, "Day1")
sys.path.insert(0, DAY1_FOLDER)

from config import client, MODEL
from agent_tools import TOOLS, TOOL_FUNCTIONS


QUESTION = "Is book B202 available in the college library?"


def run_agent(question):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a college library assistant. "
                "Use the available tool when you need library information. "
                "After getting the tool result, give a clear final answer."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]

    print("\n=== ReAct AGENT ===")
    print("Question:", question)

    while True:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0
        )

        message = response.choices[0].message

        # Final answer
        if not message.tool_calls:
            print("\nFinal Answer:")
            print(message.content)
            break

        # Tool call
        messages.append(message)

        for tool_call in message.tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            print("\nAction:", tool_name)
            print("Arguments:", arguments)

            tool_function = TOOL_FUNCTIONS[tool_name]
            result = tool_function(**arguments)

            print("Observation:", result)

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                }
            )


if __name__ == "__main__":
    run_agent(QUESTION)