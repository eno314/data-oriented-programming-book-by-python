from src.library.data.book import watchmen_book

catalog_data = {
    "booksByIsbn": {
        "978-1779501127": watchmen_book,
    },
    "authorsById": {
        "alan-moore": {
            "name": "Alan Moore",
            "books": ["978-1779501127"]
        },
        "dave-gibbons": {
            "name": "Dave Gibbons",
            "books": ["978-1779501127"]
        },
    },
}
