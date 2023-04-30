from src.library.oop.book_item import BookItem
from src.library.oop.book_lending import BookLending
from src.library.oop.user import User


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
