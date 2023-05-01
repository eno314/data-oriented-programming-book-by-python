def block_member(user_management_data, member_id):
    """
    会員をブロックする
    :param user_management_data: ユーザー管理の状態
    :param member_id: 会員ID
    """
    pass


def unblock_member(user_management_data, member_id):
    """
    会員のブロックを解除する
    :param user_management_data: ユーザー管理の状態
    :param member_id: 会員ID
    """
    pass


def login(user_management_data, login_info):
    """
    ログインする
    :param user_management_data: ユーザー管理の状態
    :param login_info: ログイン情報
    """
    pass


def is_librarian(user_management_data, email):
    return email in user_management_data['librariansByEmail']


def is_super_member(user_management_data, email):
    return user_management_data['membersByEmail'][email].get('isSuper') is True


def is_vip_member(user_management_data, user_id):
    return user_management_data['membersByEmail'][user_id].get('isVip') is True
