from src.library.oop.book_item import BookItem
from src.library.oop.user import User


class UserWithBookItemRight(User):

    def add_book_item(self, book_item: BookItem) -> BookItem:
        pass
