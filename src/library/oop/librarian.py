from typing import List

from src.library.oop.book_lending import BookLending
from src.library.oop.member import Member
from src.library.oop.user_with_block_member_right import UserWithBlockMemberRight
from src.library.oop.user_with_book_item_right import UserWithBookItemRight


class Librarian(UserWithBookItemRight, UserWithBlockMemberRight):

    def get_book_lendings_of_member(self, member: Member) -> List[BookLending]:
        pass
