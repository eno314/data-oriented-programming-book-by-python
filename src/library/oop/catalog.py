from typing import List

from src.library.oop.book import Book
from src.library.oop.book_item import BookItem
from src.library.oop.librarian import Librarian


class Catalog:

    def search(self, search_criteria: str, query_str: str) -> List[Book]:
        pass

    def add_book_item(self, librarian: Librarian, book_item: BookItem) -> BookItem:
        pass
