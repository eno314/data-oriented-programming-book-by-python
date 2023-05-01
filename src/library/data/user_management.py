from pyrsistent import pmap, pvector

user_management_data = pmap({
    "librariansByEmail": pmap({
        "frank@hoge.com": pmap({
            "email": "frank@hoge.com",
            "encryptedPassword": "bXlwYXNzd29yZAo=",
        }),
    }),
    "membersByEmail": pmap({
        "samantha@hoge.com": pmap({
            "email": "samantha@hoge.com",
            "encryptedPassword": "c2VjcmV0Cg==",
            "isBlocked": False,
            "bookLendings": pvector(
                pmap({
                    "bookItemId": "book-item-1",
                    "bookIsbn": "978-1779501127",
                    "lendingDate": "2020-04-23",
                }),
            ),
        }),
    }),
})
