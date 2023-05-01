from src.library.catalog import author_names, book_info, search_books_by_title
from src.library.data.book import watchmen_book
from src.library.data.catalog import catalog_data


def test_search_books_by_title_found():
    actual = search_books_by_title(catalog_data, "Watch")
    expected = [{
        "title": "Watchmen",
        "isbn": "978-1779501127",
        "authorNames": ["Alan Moore", "Dave Gibbons"],
    }]
    assert expected == actual


def test_search_books_by_title_not_found():
    actual = search_books_by_title(catalog_data, "Not Found")
    assert [] == actual


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
