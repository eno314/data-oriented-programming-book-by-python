catalog_data = {
    "booksByIsbn": {
        "978-1779501127": {
            "isbn": "978-1779501127",
            "title": "Watchmen",
            "publicationYear": 1987,
            "authors": ["alan-moore", "dave-gibbons"],
            "bookItems": [
                {
                    "id": "book-item-1",
                    "libId": "nyc-central-lib",
                    "isLent": True,
                },
                {
                    "id": "book-item-2",
                    "libId": "nyc-central-lib",
                    "isLent": False,
                },
            ]
        }
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
