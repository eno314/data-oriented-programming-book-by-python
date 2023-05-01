from pyrsistent import pmap

from src.library.data.catalog import catalog_data

library_data = pmap({
    "catalog": catalog_data,
})
