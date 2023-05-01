from pyrsistent import pmap, pvector

from src.library.data.book import books

catalog_data = pmap({
    "booksByIsbn": books,
    "authorsById": pmap({
        "alan-moore": pmap({
            "name": "Alan Moore",
            "books": pvector(["978-1779501127"])
        }),
        "dave-gibbons": pmap({
            "name": "Dave Gibbons",
            "books": pvector(["978-1779501127"])
        }),
    }),
})
