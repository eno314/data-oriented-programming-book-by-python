from typing import List

from src.library.oop.book_lending import BookLending
from src.library.oop.catalog import Catalog
from src.library.oop.user_management import UserManagement


class Library:
    name: str
    address: str

    catalog: Catalog
    user_management: UserManagement

    def get_book_lendings(self, user_id: str, member_id: str) -> List[BookLending]:
        """
        会員が借りている本の一覧を取得する
        :param user_id: 司書ID
        :param member_id: 会員ID
        :return: 会員が借りている本の一覧を
        """
        # this.catalogとthis.user_managementを使ってlibraryの状態にアクセス
        pass
