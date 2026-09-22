"""System 2: Rule-based workflow.

No LLM is used. The workflow follows predefined Python rules
and directly accesses the private student data.
"""

import re
from config import STUDENTS, QUESTIONS


def find_student(name):
    """Find a student using the private student database."""
    for student_name, data in STUDENTS.items():
        if student_name.lower() == name.lower():
            return student_name, data

    return None, None


def workflow(question):
    text = question.lower()

    # Rule 1: Find a student's LeetCode score
    if "leetcode" in text and ("score" in text or "rating" in text):
        for name in STUDENTS:
            if name.lower() in text:
                student_name, data = find_student(name)
                return f"{student_name}'s LeetCode score: {data['leetcode']}"

    # Rule 2: Check placement eligibility
    if "eligible" in text:
        for name in STUDENTS:
            if name.lower() in text:
                student_name, data = find_student(name)
                result = "Eligible" if data["eligible"] else "Not Eligible"
                return f"{student_name}: {result} for placement"

    # Rule 3: Calculate average LeetCode score
    if "average" in text and "leetcode" in text:
        found_scores = []

        for name in STUDENTS:
            if name.lower() in text:
                found_scores.append(STUDENTS[name]["leetcode"])

        if len(found_scores) >= 2:
            average = sum(found_scores) / len(found_scores)
            return f"Average LeetCode score: {average:.2f}"

    # Rule 4: Find students above a LeetCode score
    if "above" in text and "leetcode" in text:
        match = re.search(r"above\s+(\d+)", text)

        if match:
            limit = int(match.group(1))

            qualified = [
                name
                for name, data in STUDENTS.items()
                if data["leetcode"] > limit
            ]

            if qualified:
                return (
                    f"Students with LeetCode score above {limit}: "
                    + ", ".join(qualified)
                )

    return "Sorry, I do not have a rule for this type of question."


if __name__ == "__main__":
    print("\n=== SYSTEM 2: RULE-BASED WORKFLOW ===\n")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", workflow(question))
        print("-" * 70)