"""Campus Opportunity Radar - single external tool."""

import json
import os


DATA_FILE = os.path.join(
    os.path.dirname(__file__),
    "opportunities.json"
)


def get_opportunity_status(opportunity_id):
    """Look up an opportunity from the external JSON dataset."""

    opportunity_id = opportunity_id.strip().upper()

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            opportunities = json.load(file)

        opportunity = opportunities.get(opportunity_id)

        if opportunity is None:
            return f"Opportunity {opportunity_id} was not found."

        return (
            f"Opportunity: {opportunity['name']}\n"
            f"Status: {opportunity['status']}\n"
            f"Deadline: {opportunity['deadline']}\n"
            f"Eligibility: {opportunity['eligibility']}"
        )

    except Exception as error:
        return f"Tool error: {error}"


if __name__ == "__main__":
    print(get_opportunity_status("BIT-AI-01"))