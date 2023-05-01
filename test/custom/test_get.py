from src.custom.get import my_get
from src.library.data.catalog import catalog_data


def test_my_get():
    assert "Watchmen" == my_get(catalog_data, ["booksByIsbn", "978-1779501127", "title"])
