from src.ch1.book_item import BookItem
from src.ch1.book_lending import BookLending
from src.ch1.user import User


class Member(User):

    def is_blocked(self) -> bool:
        pass

    def block(self) -> bool:
        pass

    def unblock(self) -> bool:
        pass

    def return_book(self, book_lending: BookLending) -> bool:
        pass

    def checkout(self, book_item: BookItem) -> BookLending:
        pass
