from src.library.dop import catalog, user_management


def search_book(library_data, search_query):
    """
    本を検索する
    :param library_data: libraryの状態
    :param search_query: 検索クエリ
    """
    catalog_data = get_catalog_data_from(library_data)
    return catalog.search_book(catalog_data, search_query)


def add_book_item(library_data, user_id, book_item_info):
    """
    本を追加する
    :param library_data: libraryの状態
    :param user_id: 司書ID
    :param book_item_info: 本の情報
    """
    user_management_data = get_user_management_data_from(library_data)
    if user_management.is_librarian(user_management_data, user_id):
        catalog_data = get_catalog_data_from(library_data)
        catalog.add_book_item(catalog_data, book_item_info)


def block_member(library_data, member_id):
    """
    会員をブロックする
    :param library_data: libraryの状態
    :param member_id: 会員ID
    """
    user_management_data = get_user_management_data_from(library_data)
    user_management.block_member(user_management_data, member_id)


def unblock_member(library_data, member_id):
    """
    会員のブロックを解除する
    :param library_data: libraryの状態
    :param member_id: 会員ID
    """
    user_management_data = get_user_management_data_from(library_data)
    user_management.unblock_member(user_management_data, member_id)


def login(library_data, login_info):
    """
    ログインする
    :param library_data: libraryの状態
    :param login_info: ログイン情報
    """
    user_management_data = get_user_management_data_from(library_data)
    user_management.login(user_management_data, login_info)


def get_book_lendings(libraryData, user_id, member_id):
    """
    会員が借りている本の一覧を取得する
    :param libraryData: libraryの状態
    :param user_id: 司書ID
    :param member_id: 会員ID
    """
    user_management_data = get_user_management_data_from(library_data)
    if user_management.is_librarian(user_management_data, user_id):
        catalog_data = get_catalog_data_from(library_data)
        return catalog.get_book_lendings(catalog_data, member_id)
    else:
        raise Exception("You don't have permission to get book lendings.")


def checkout_book(library_data, user_id, book_item_id):
    """
    本を借りる
    :param library_data: libraryの状態
    :param user_id: 司書ID
    :param book_item_id: 本のID
    """
    user_management_data = get_user_management_data_from(library_data)
    if user_management.is_librarian(user_management_data, user_id):
        catalog_data = get_catalog_data_from(library_data)
        catalog.checkout_book(catalog_data, book_item_id)


def return_book(library_data, user_id, book_item_id):
    """
    本を返す
    :param library_data: libraryの状態
    :param user_id: 司書ID
    :param book_item_id: 本のID
    """
    user_management_data = get_user_management_data_from(library_data)
    if user_management.is_librarian(user_management_data, user_id):
        catalog_data = get_catalog_data_from(library_data)
        catalog.return_book(catalog_data, book_item_id)
