"""Day 2 Assessment: Self-consistency observation."""

import os
import sys
from collections import Counter

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

DAY1_FOLDER = os.path.join(PROJECT_ROOT, "Day1")
sys.path.insert(0, DAY1_FOLDER)

from config import client, MODEL


QUESTION = (
    "A student reads three books taking 4, 6 and 5 days. "
    "If the student has 17 days available, "
    "how many days will remain after finishing all three?"
)


PROMPT = (
    "Solve the problem carefully. "
    "Give the final numerical answer clearly."
)


def ask():
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": QUESTION}
        ],
        temperature=0.8
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    print("\n=== SELF-CONSISTENCY ===")
    print("Model:", MODEL)
    print("Temperature: 0.8")
    print("\nQuestion:")
    print(QUESTION)

    answers = []

    for i in range(5):
        answer = ask()

        print(f"\n--- RUN {i + 1} ---")
        print(answer)

        answers.append(answer)

    print("\n=== OBSERVATION ===")

    # Simple normalization for the expected numerical answer
    normalized = []

    for answer in answers:
        if "2" in answer:
            normalized.append("2 days")
        else:
            normalized.append("Other")

    counts = Counter(normalized)

    print("Normalized results:")
    for answer, count in counts.items():
        print(f"{answer}: {count}/5")

    majority = counts.most_common(1)[0]

    print("\nMajority result:", majority[0])
    print("Count:", f"{majority[1]}/5")