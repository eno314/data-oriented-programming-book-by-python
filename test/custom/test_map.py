from src.custom.get import my_get
from src.custom.map import my_map
from src.library.data.catalog import catalog_data


def test_my_map():
    actual = my_map(
        ["alan-moore", "dave-gibbons"],
        lambda author_id: my_get(catalog_data, ["authorsById", author_id, "name"])
    )
    assert ["Alan Moore", "Dave Gibbons"] == actual
