from src.ch1.book_item import BookItem
from src.ch1.user import User


class UserWithBookItemRight(User):

    def add_book_item(self, book_item: BookItem) -> BookItem:
        pass
