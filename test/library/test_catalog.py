from src.library.catalog import author_names, book_info
from src.library.data.book import watchmen_book
from src.library.data.catalog import catalog_data


def test_book_info():
    actual = book_info(catalog_data, watchmen_book)

    expected = {
        "title": "Watchmen",
        "isbn": "978-1779501127",
        "authorNames": ["Alan Moore", "Dave Gibbons"],
    }
    assert expected == actual


def test_author_names():
    actual = author_names(catalog_data, watchmen_book)
    assert ["Alan Moore", "Dave Gibbons"] == actual
