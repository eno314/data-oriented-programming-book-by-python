from typing import List

from src.ch1.book_lending import BookLending
from src.ch1.member import Member
from src.ch1.user_with_book_item_right import UserWithBookItemRight


class Librarian(UserWithBookItemRight):

    def block_member(self, member) -> bool:
        pass

    def unblock_member(self, member) -> bool:
        pass

    def get_book_lendings_of_member(self, member: Member) -> List[BookLending]:
        pass
