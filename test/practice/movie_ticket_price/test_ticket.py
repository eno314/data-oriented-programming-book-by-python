import datetime

import pytest
from pyrsistent import pmap

from src.practice.movie_ticket_price import ticket
from src.practice.movie_ticket_price.data.ticket import ticket_data


@pytest.fixture
def test_data():
    return {
        'general_user': pmap({
            'age': 30,
            'is_student': False,
            'is_middle_or_high_school': False,
            'is_elementary_school_or_younger': False,
            'has_disability': False,
            'is_member': False,
        }),
        'normal_day_daytime': datetime.datetime(2023, 5, 2, 10, 0, 0),
        'normal_day_late_show': datetime.datetime(2023, 5, 2, 23, 0, 0),
        'movie_day_daytime': datetime.datetime(2023, 5, 1, 10, 0, 0),
        'movie_day_late_show': datetime.datetime(2023, 5, 1, 23, 0, 0),
    }


def test_general_weekday_daytime(test_data):
    actual = ticket.calculate_price(
        ticket_data,
        test_data['general_user'],
        test_data['normal_day_daytime']
    )
    expected = pmap({'price': 1900, 'currency': 'JPY'})
    assert expected == actual


def test_general_weekday_late_show(test_data):
    actual = ticket.calculate_price(
        ticket_data,
        test_data['general_user'],
        test_data['normal_day_late_show']
    )
    expected = pmap({'price': 1400, 'currency': 'JPY'})
    assert expected == actual


def test_general_weekday_movie_day_daytime(test_data):
    actual = ticket.calculate_price(
        ticket_data,
        test_data['general_user'],
        test_data['movie_day_daytime']
    )
    expected = pmap({'price': 1200, 'currency': 'JPY'})
    assert expected == actual


def test_general_weekday_movie_day_late_show(test_data):
    actual = ticket.calculate_price(
        ticket_data,
        test_data['general_user'],
        test_data['movie_day_late_show']
    )
    expected = pmap({'price': 1200, 'currency': 'JPY'})
    assert expected == actual
