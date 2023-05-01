from src.library import user_management
from src.library.data.user_management import user_management_data


def test_is_librarian_true():
    assert user_management.is_librarian(user_management_data, "frank@hoge.com")


def test_is_librarian_false():
    assert not user_management.is_librarian(
        user_management_data, "samantha@hoge.com"
    )


def test_is_vip_member():
    assert not user_management.is_vip_member(
        user_management_data, "samantha@hoge.com"
    )
