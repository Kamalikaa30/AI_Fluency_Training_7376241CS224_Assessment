"""Day 3 Assessment: LLM with one external tool."""

import json
import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

DAY1_FOLDER = os.path.join(PROJECT_ROOT, "Day1")
sys.path.insert(0, DAY1_FOLDER)

from config import client, MODEL
from opportunity_tool import get_opportunity_status


TOOL_SCHEMA = {
    "type": "function",
    "function": {
        "name": "get_opportunity_status",
        "description": (
            "Look up a campus opportunity in the private "
            "opportunity database. Returns its status, deadline "
            "and eligibility."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "opportunity_id": {
                    "type": "string",
                    "description": (
                        "The opportunity ID, such as BIT-AI-01, "
                        "BIT-DEV-02, or BIT-GEN-03."
                    )
                }
            },
            "required": ["opportunity_id"]
        }
    }
}


QUESTIONS = [
    "Is BIT AI Innovation Sprint currently open, and what is its deadline?",
    (
        "A third-year student wants to apply to an opportunity "
        "open to 2nd to 4th year students. Is the student eligible?"
    ),
    (
        "A student has opportunities with deadlines of "
        "5 October and 12 October. Which deadline comes first?"
    )
]


def run_with_tool(question):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a college opportunity assistant. "
                "Use the opportunity tool only when information "
                "from the private opportunity database is required. "
                "Do not invent private opportunity information."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=[TOOL_SCHEMA],
        tool_choice="auto",
        temperature=0
    )

    message = response.choices[0].message

    if not message.tool_calls:
        return (
            "Tool not called.\n"
            "Final answer: " + message.content
        )

    messages.append(message)

    for tool_call in message.tool_calls:

        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print("\nTOOL CALL")
        print("Tool:", tool_name)
        print("Arguments:", arguments)

        result = get_opportunity_status(**arguments)

        print("\nTOOL RESULT")
        print(result)

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            }
        )

    final_response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0
    )

    return final_response.choices[0].message.content.strip()


if __name__ == "__main__":

    print("\n=== LLM WITH ONE EXTERNAL TOOL ===")
    print("Model:", MODEL)

    for number, question in enumerate(QUESTIONS, start=1):

        print("\n" + "=" * 70)
        print(f"QUESTION {number}:")
        print(question)

        print("\nRESULT:")
        print(run_with_tool(question))