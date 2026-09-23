"""Day 2 Assessment: Direct Prompting vs Chain-of-Thought."""

import os
import sys

# Find the project root
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

# Allow Day2 to use the existing Day1 config
DAY1_FOLDER = os.path.join(PROJECT_ROOT, "Day1")
sys.path.insert(0, DAY1_FOLDER)

from config import client, MODEL


QUESTIONS = [
    (
        "A student reads three books taking 4, 6 and 5 days. "
        "If the student has 17 days available, can they finish all three books?"
    ),
    (
        "Anu finished before Bala. Bala finished before Charan. "
        "Who finished first and who finished last?"
    ),
    (
        "If a student has 2 extra days and the three books take "
        "4, 6 and 5 days, how many days will remain after finishing all three?"
    ),
]


DIRECT_PROMPT = (
    "You are a helpful college library assistant. "
    "Give only the final answer. Do not explain."
)


COT_PROMPT = (
    "You are a helpful college library assistant. "
    "Solve the problem step by step. "
    "Show the calculation or reasoning clearly. "
    "At the end, write exactly: Final Answer: <answer>"
)


def ask(system_prompt, question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    print("\n=== DIRECT PROMPTING VS CHAIN-OF-THOUGHT ===")
    print("Provider: Groq")
    print("Model:", MODEL)

    for number, question in enumerate(QUESTIONS, start=1):

        print("\n" + "=" * 70)
        print(f"QUESTION {number}:")
        print(question)

        print("\n--- DIRECT PROMPTING ---")
        print(ask(DIRECT_PROMPT, question))

        print("\n--- CHAIN-OF-THOUGHT ---")
        print(ask(COT_PROMPT, question))