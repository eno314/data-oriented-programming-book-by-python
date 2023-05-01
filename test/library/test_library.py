import json

from src.library import library
from src.library.data.library import library_data


def test_search_book():
    actual = library.search_books_by_title_json(library_data, "Watch")
    expected = """
[
  {
    "authorNames": ["Alan Moore", "Dave Gibbons"],
    "isbn": "978-1779501127",
    "title": "Watchmen"
  }
]"""
    assert json.loads(expected) == json.loads(actual)
