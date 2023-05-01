import json

from pyrsistent import pmap

from src.library import library
from src.library.data.library import library_data
from src.library.data.user_management import user_management_data


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


def test_add_member():
    new_member = pmap({
        "email": "new@hoge.com",
        "encryptedPassword": "dGVzdAo=",
    })
    actual = library.add_member(library_data, new_member)
    expected = {
        "catalog": library_data["catalog"],
        "user_management": {
            "librariansByEmail": user_management_data["librariansByEmail"],
            "membersByEmail": {
                "samantha@hoge.com": user_management_data["membersByEmail"]["samantha@hoge.com"],
                "new@hoge.com": new_member,
            }
        }
    }
    assert expected == actual
