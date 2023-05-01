import pytest

from src.library import catalog
from src.library.data.catalog import catalog_data


class TestSearchBooksByTitle:

    def test_found(self):
        actual = catalog.search_books_by_title(catalog_data, "Watch")
        expected = [{
            "title": "Watchmen",
            "isbn": "978-1779501127",
            "authorNames": ["Alan Moore", "Dave Gibbons"],
        }]
        assert expected == actual

    def test_lower_case_match(self):
        actual = catalog.search_books_by_title(catalog_data, "watch")
        expected = [{
            "title": "Watchmen",
            "isbn": "978-1779501127",
            "authorNames": ["Alan Moore", "Dave Gibbons"],
        }]
        assert expected == actual

    def test_not_found(self):
        actual = catalog.search_books_by_title(catalog_data, "NotFound")
        assert [] == actual


class TestBookInfo:
    @pytest.fixture
    def test_catalog_data(self):
        return {
            "authorsById": {
                "alan-moore": {
                    "name": "Alan Moore",
                },
                "dave-gibbons": {
                    "name": "Dave Gibbons",
                },
            },
        }

    @pytest.fixture
    def test_book_data(self):
        return {
            "isbn": "978-1779501127",
            "title": "Watchmen",
            "authorIds": ["alan-moore", "dave-gibbons"],
        }

    def test(self, test_catalog_data, test_book_data):
        actual = catalog.book_info(test_catalog_data, test_book_data)
        expected = {
            "title": "Watchmen",
            "isbn": "978-1779501127",
            "authorNames": ["Alan Moore", "Dave Gibbons"],
        }
        assert expected == actual


class TestAuthorNames:
    @pytest.fixture
    def test_catalog_data(self):
        return {
            "authorsById": {
                "alan-moore": {
                    "name": "Alan Moore",
                },
                "dave-gibbons": {
                    "name": "Dave Gibbons",
                },
            },
        }

    def test_with_no_author_ids(self, test_catalog_data):
        actual = catalog.author_names(test_catalog_data, [])
        assert [] == actual

    def test_with_one_author_id(self, test_catalog_data):
        actual = catalog.author_names(test_catalog_data, ["alan-moore"])
        assert ["Alan Moore"] == actual

    def test_with_two_author_ids(self, test_catalog_data):
        actual = catalog.author_names(test_catalog_data, ["alan-moore", "dave-gibbons"])
        assert ["Alan Moore", "Dave Gibbons"] == actual

    def test_with_unknown_author_id(self, test_catalog_data):
        actual = catalog.author_names(test_catalog_data, ["unknown"])
        assert [None] == actual

    def test_with_empty_catalog_data_and_author_ids(self):
        actual = catalog.author_names({}, [])
        assert [] == actual

    def test_with_empty_catalog_data_and_one_author_id(self):
        actual = catalog.author_names({}, ["alan-moore"])
        assert [None] == actual
