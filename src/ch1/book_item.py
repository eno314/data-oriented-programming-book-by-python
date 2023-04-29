from src.ch1.book_lending import BookLending
from src.ch1.member import Member


class BookItem:
    id: str
    lib_id: str

    def checkout(self, member: Member) -> BookLending:
        pass
