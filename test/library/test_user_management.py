from pyrsistent import pmap

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


def test_add_member():
    new_member = pmap({
        "email": "new@hoge.com",
        "encryptedPassword": "dGVzdAo=",
    })
    actual = user_management.add_member(user_management_data, new_member)
    expected = {
        "librariansByEmail": user_management_data["librariansByEmail"],
        "membersByEmail": {
            "samantha@hoge.com": user_management_data["membersByEmail"]["samantha@hoge.com"],
            "new@hoge.com": new_member,
        }
    }
    assert expected == actual
