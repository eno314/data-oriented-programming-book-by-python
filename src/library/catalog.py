from src.custom.get import my_get


def search_book(catalog_data, search_query):
    """
    本を検索する
    :param catalog_data: カタログの状態
    :param search_query: 検索クエリ
    """
    pass


def add_book_item(catalog_data, book_item_info):
    """
    本を追加する
    :param catalog_data: カタログの状態
    :param book_item_info: 本の情報
    """
    pass


def checkout_book(catalog_data, book_item_id):
    """
    本を借りる
    :param catalog_data: カタログの状態
    :param book_item_id: 本のID
    """
    pass


def return_book(catalog_data, book_item_id):
    """
    本を返す
    :param catalog_data: カタログの状態
    :param book_item_id: 本のID
    """
    pass


def get_book_lendings(catalog_data, member_id):
    """
    会員が借りている本の一覧を取得する
    :param catalog_data: カタログの状態
    :param member_id: 会員ID
    """
    pass


def search_books_by_title(catalog_data, query):
    all_books = my_get(catalog_data, ["booksByIsbn"]).values()
    matching_books = [
        book
        for book in all_books
        if query in my_get(book, ["title"])
    ]
    return [
        book_info(catalog_data, book)
        for book in matching_books
    ]


def book_info(catalog_data, book):
    return {
        "title": my_get(book, ["title"]),
        "isbn": my_get(book, ["isbn"]),
        "authorNames": author_names(catalog_data, book),
    }


def author_names(catalog_data, book):
    author_ids = my_get(book, ["authorIds"])
    return [
        my_get(catalog_data, ["authorsById", author_id, "name"])
        for author_id in author_ids
    ]
