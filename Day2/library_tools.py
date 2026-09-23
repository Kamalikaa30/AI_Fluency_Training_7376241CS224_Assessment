"""Private college library data and tool."""


BOOKS = {
    "B101": {
        "title": "Python Basics",
        "available": 3
    },
    "B202": {
        "title": "Data Structures",
        "available": 0
    },
    "B303": {
        "title": "AI Fundamentals",
        "available": 2
    }
}


def get_book_availability(book_id: str) -> str:
    """Check the availability of a book."""

    book_id = book_id.strip().upper()

    book = BOOKS.get(book_id)

    if book is None:
        return f"Unknown book ID: {book_id}"

    return (
        f"{book['title']} ({book_id}): "
        f"{book['available']} copies available"
    )


if __name__ == "__main__":
    print(get_book_availability("B101"))
    print(get_book_availability("B202"))
    print(get_book_availability("B303"))