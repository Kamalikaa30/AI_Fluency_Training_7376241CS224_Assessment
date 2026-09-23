"""Tool definitions for the ReAct library agent."""

from library_tools import get_book_availability


TOOL_FUNCTIONS = {
    "get_book_availability": get_book_availability
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_book_availability",
            "description": (
                "Check how many copies of a book are currently "
                "available in the college library."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "book_id": {
                        "type": "string",
                        "description": (
                            "The book ID, such as B101, B202, or B303."
                        )
                    }
                },
                "required": ["book_id"]
            }
        }
    }
]