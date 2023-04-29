from typing import List

from src.ch1.book_item import BookItem
from src.ch1.book_lending import BookLending
from src.ch1.member import Member


class Librarian:

    def block_member(self, member) -> bool:
        pass

    def unblock_member(self, member) -> bool:
        pass

    def add_book_item(self, book_item: BookItem) -> BookItem:
        pass

    def get_book_lendings_of_member(self, member: Member) -> List[BookLending]:
        pass
