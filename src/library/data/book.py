from pyrsistent import pmap, pvector

watchmen_book = pmap({
    "isbn": "978-1779501127",
    "title": "Watchmen",
    "publicationYear": 1987,
    "authorIds": pvector(["alan-moore", "dave-gibbons"]),
    "bookItems": pvector([
        pmap({
            "id": "book-item-1",
            "libId": "nyc-central-lib",
            "isLent": True,
        }),
        pmap({
            "id": "book-item-2",
            "libId": "nyc-central-lib",
            "isLent": False,
        }),
    ]),
})
