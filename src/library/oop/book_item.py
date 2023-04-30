from src.library.oop.book_lending import BookLending
from src.library.oop.member import Member


class BookItem:
    id: str
    lib_id: str

    def checkout(self, member: Member) -> BookLending:
        pass
