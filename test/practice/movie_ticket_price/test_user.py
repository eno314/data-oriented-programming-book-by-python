import pytest
from pyrsistent import pmap

from src.practice.movie_ticket_price import user


@pytest.mark.parametrize('user_data, expected', [
    (pmap({'age': 69}), False),
    (pmap({'age': 70}), True),
    (pmap({'age': 71}), True),
])
def test_is_senior(user_data, expected):
    assert user.is_senior(user_data) == expected


@pytest.mark.parametrize('user_data, expected', [
    (pmap({'age': 59}), False),
    (pmap({'age': 60}), True),
    (pmap({'age': 61}), True),
])
def test_is_senior_for_member(user_data, expected):
    assert user.is_senior_for_member(user_data) == expected
