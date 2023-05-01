from pyrsistent import pmap

from src.library.data.catalog import catalog_data
from src.library.data.user_management import user_management_data

library_data = pmap({
    "catalog": catalog_data,
    "user_management": user_management_data,
})
