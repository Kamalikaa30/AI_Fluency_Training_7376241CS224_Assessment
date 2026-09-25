"""Day 3 Assessment: Plain LLM without any tool."""

import os
import sys

# Use the existing Day1 configuration for the Groq client.
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

DAY1_FOLDER = os.path.join(PROJECT_ROOT, "Day1")
sys.path.insert(0, DAY1_FOLDER)

from config import client, MODEL


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


def ask_llm(question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful college opportunity assistant. "
                    "Answer the user's question directly. "
                    "You do not have access to external tools."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    print("\n=== PLAIN LLM — NO TOOL ===")
    print("Model:", MODEL)

    for number, question in enumerate(QUESTIONS, start=1):
        print("\n" + "=" * 70)
        print(f"QUESTION {number}:")
        print(question)

        print("\nANSWER:")
        print(ask_llm(question))