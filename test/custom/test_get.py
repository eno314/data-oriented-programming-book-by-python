from src.custom.get import get
from src.library.data.catalog import catalog_data


def test_get():
    assert "Watchmen" == get(catalog_data, ["booksByIsbn", "978-1779501127", "title"])
