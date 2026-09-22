"""Shared configuration for the Student Placement Tracker project."""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "groq").strip().lower()

if PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "qwen/qwen3.8-27b")
else:
    raise SystemExit(
        f"Unknown PROVIDER '{PROVIDER}'. Use groq."
    )

if not API_KEY:
    raise SystemExit(
        "No API key found for PROVIDER=groq. Check your .env file."
    )

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)


# Private student placement data
STUDENTS = {
    "Anu": {
        "skill": "Java",
        "leetcode": 85,
        "aptitude": 78,
        "eligible": True
    },
    "Bala": {
        "skill": "Python",
        "leetcode": 62,
        "aptitude": 82,
        "eligible": False
    },
    "Charan": {
        "skill": "Java",
        "leetcode": 91,
        "aptitude": 88,
        "eligible": True
    },
    "Divya": {
        "skill": "React",
        "leetcode": 74,
        "aptitude": 91,
        "eligible": True
    }
}


QUESTIONS = [
    "What is Anu's LeetCode score?",
    "Is Charan eligible for placement?",
    "What is the average LeetCode score of Anu and Charan?",
    "Which students have a LeetCode score above 80?"
]


def banner(system_name):
    print(
        f"\n=== {system_name} | "
        f"provider: {PROVIDER} | "
        f"model: {MODEL} ===\n"
    )