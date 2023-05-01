import pytest

from src.library.data.book import books


def test_shared():
    next_books = books.transform(["978-1779501127", "publicationYear"], 1986)
    assert next_books["978-1779501127"]["authorIds"][1] == "dave-gibbons"
    with pytest.raises(TypeError):
        next_books["978-1779501127"]["authorIds"][1] = "dave-chester-gibbons"
