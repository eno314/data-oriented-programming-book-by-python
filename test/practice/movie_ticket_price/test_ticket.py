import datetime

import pytest
from pyrsistent import pmap

from src.practice.movie_ticket_price import ticket
from src.practice.movie_ticket_price.data.ticket import ticket_data

screening_datetime_test_data = {
    'weekday_daytime': datetime.datetime(2023, 4, 28, 10, 0, 0),
    'weekday_late_show': datetime.datetime(2023, 5, 2, 23, 0, 0),
    'weekend_daytime': datetime.datetime(2023, 4, 30, 10, 0, 0),
    'weekend_late_show': datetime.datetime(2023, 5, 6, 23, 0, 0),
    'movie_day_daytime': datetime.datetime(2023, 5, 1, 10, 0, 0),
    'movie_day_late_show': datetime.datetime(2023, 5, 1, 23, 0, 0),
}


@pytest.fixture
def general_user():
    return pmap({
        'age': 30,
        'is_student': False,
        'is_middle_or_high_school': False,
        'is_elementary_school_or_younger': False,
        'has_disability': False,
        'is_member': False,
    })


@pytest.mark.parametrize('screening_datetime, expected', [
    (screening_datetime_test_data['weekday_daytime'], pmap({'price': 1900, 'currency': 'JPY'})),
    (screening_datetime_test_data['weekday_late_show'], pmap({'price': 1400, 'currency': 'JPY'})),
    (screening_datetime_test_data['weekend_daytime'], pmap({'price': 1900, 'currency': 'JPY'})),
    (screening_datetime_test_data['weekend_late_show'], pmap({'price': 1400, 'currency': 'JPY'})),
    (screening_datetime_test_data['movie_day_daytime'], pmap({'price': 1200, 'currency': 'JPY'})),
    (screening_datetime_test_data['movie_day_late_show'], pmap({'price': 1200, 'currency': 'JPY'})),
])
def test_general_weekday_daytime(general_user, screening_datetime, expected):
    assert expected == ticket.calculate_price(ticket_data, general_user, screening_datetime)
