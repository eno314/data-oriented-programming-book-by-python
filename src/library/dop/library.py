def search_book(library_data, search_query):
    """
    本を検索する
    :param library_data: libraryの状態
    :param search_query: 検索クエリ
    """
    pass


def add_book_item(library_data, user_id, book_item_info):
    """
    本を追加する
    :param library_data: libraryの状態
    :param user_id: 司書ID
    :param book_item_info: 本の情報
    """
    pass


def block_member(library_data, member_id):
    """
    会員をブロックする
    :param library_data: libraryの状態
    :param member_id: 会員ID
    """
    pass


def unblock_member(library_data, member_id):
    """
    会員のブロックを解除する
    :param library_data: libraryの状態
    :param member_id: 会員ID
    """
    pass


def login(library_data, login_info):
    """
    ログインする
    :param library_data: libraryの状態
    :param login_info: ログイン情報
    """
    pass


def get_book_lendings(libraryData, user_id, member_id):
    """
    会員が借りている本の一覧を取得する
    :param libraryData: libraryの状態
    :param user_id: 司書ID
    :param member_id: 会員ID
    """
    pass


def checkout_book(library_data, user_id, book_item_id):
    """
    本を借りる
    :param library_data: libraryの状態
    :param user_id: 司書ID
    :param book_item_id: 本のID
    """
    pass


def return_book(library_data, user_id, book_item_id):
    """
    本を返す
    :param library_data: libraryの状態
    :param user_id: 司書ID
    :param book_item_id: 本のID
    """
    pass
