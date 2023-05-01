import pytest
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


class TestAddMember:

    @pytest.fixture
    def new_member(self):
        return pmap({
            "email": "new@hoge.com",
            "encryptedPassword": "dGVzdAo=",
        })

    @pytest.fixture
    def user_management_without_member(self):
        return pmap({})

    @pytest.fixture
    def exists_member(self):
        return pmap({
            "email": "exists@hoge.com",
            "encryptedPassword": "dGVzdAo=",
        })

    @pytest.fixture
    def member_user_management_with_member(self, exists_member):
        return pmap({
            "membersByEmail": pmap({
                "exists@hoge.com": exists_member,
            })
        })

    def test_with_empty_member(
            self,
            new_member,
            user_management_without_member
    ):
        actual = user_management.add_member(user_management_without_member, new_member)
        expected = {
            "membersByEmail": {
                "new@hoge.com": new_member,
            }
        }
        assert expected == actual

    def test_with_exists_member_ok(
            self,
            new_member,
            member_user_management_with_member
    ):
        actual = user_management.add_member(member_user_management_with_member, new_member)
        expected = {
            "membersByEmail": {
                "exists@hoge.com": member_user_management_with_member["membersByEmail"]["exists@hoge.com"],
                "new@hoge.com": new_member,
            }
        }
        assert expected == actual

    def test_with_exists_member_ng(
            self,
            exists_member,
            member_user_management_with_member
    ):
        with pytest.raises(ValueError, match='member already exists'):
            user_management.add_member(member_user_management_with_member, exists_member)
