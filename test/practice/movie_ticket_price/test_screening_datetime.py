import datetime

import pytest

from src.practice.movie_ticket_price import screening_datetime


@pytest.mark.parametrize('screening_datetime_data, expected', [
    (datetime.datetime(2023, 4, 30, 23, 59, 59), False),
    (datetime.datetime(2023, 5, 1, 0, 0, 0), True),
    (datetime.datetime(2023, 5, 1, 23, 59, 59), True),
    (datetime.datetime(2023, 5, 2, 0, 0, 0), False),
    (datetime.datetime(2023, 6, 1, 0, 0, 0), True),
])
def test_is_movie_day(screening_datetime_data, expected):
    assert screening_datetime.is_movie_day(screening_datetime_data) == expected


@pytest.mark.parametrize('screening_datetime_data, expected', [
    (datetime.datetime(2023, 4, 28, 23, 59, 59), False),
    (datetime.datetime(2023, 4, 29, 0, 0, 0), True),
    (datetime.datetime(2023, 4, 30, 23, 59, 59), True),
    (datetime.datetime(2023, 5, 1, 0, 0, 0), False),
])
def test_is_weekend(screening_datetime_data, expected):
    assert screening_datetime.is_weekend(screening_datetime_data) == expected


@pytest.mark.parametrize('screening_datetime_data, expected', [
    (datetime.datetime(2023, 4, 30, 19, 59, 59), False),
    (datetime.datetime(2023, 4, 30, 20, 0, 0), True),
    (datetime.datetime(2023, 4, 30, 23, 59, 59), True),
    (datetime.datetime(2023, 5, 1, 0, 0, 0), False),
    (datetime.datetime(2023, 5, 1, 19, 59, 59), False),
    (datetime.datetime(2023, 5, 1, 20, 0, 0), True),
])
def test_is_late_show(screening_datetime_data, expected):
    assert screening_datetime.is_late_show(screening_datetime_data) == expected
