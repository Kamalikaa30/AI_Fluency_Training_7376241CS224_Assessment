"""System 1: Plain LLM chatbot.

The chatbot has no access to the private student placement data.
"""

from config import client, MODEL, QUESTIONS, banner


def chatbot(question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful student placement assistant. "
                    "Answer the user's questions naturally. "
                    "You do not have access to any private student database."
                ),
            },
            {
                "role": "user",
                "content": question,
            },
        ],
        temperature=0,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    banner("SYSTEM 1: PLAIN CHATBOT")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", chatbot(question))
        print("-" * 70)