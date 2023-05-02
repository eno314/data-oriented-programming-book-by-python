import datetime

import pytest
from pyrsistent import pmap

import src.practice.movie_ticket_price.ticket_price_data as tpd
from src.practice.movie_ticket_price import ticket_price

screening_datetime_test_data = {
    'weekday_daytime': datetime.datetime(2023, 4, 28, 10, 0, 0),
    'weekday_late_show': datetime.datetime(2023, 5, 2, 23, 0, 0),
    'holiday_daytime': datetime.datetime(2023, 4, 30, 10, 0, 0),
    'holiday_late_show': datetime.datetime(2023, 5, 6, 23, 0, 0),
    'movie_day_daytime': datetime.datetime(2023, 5, 1, 10, 0, 0),
    'movie_day_late_show': datetime.datetime(2023, 5, 1, 23, 0, 0),
}


@pytest.fixture
def ticket_price_data():
    return tpd.get()


@pytest.fixture
def general_user():
    return pmap({
        'age': 30,
    })


@pytest.fixture
def senior_user():
    return pmap({
        'age': 80,
    })


@pytest.fixture
def member_user():
    return pmap({
        'age': 25,
        'is_member': True,
    })


@pytest.fixture
def senior_member_user():
    return pmap({
        'age': 65,
        'is_member': True,
    })


@pytest.fixture
def students_user():
    return pmap({
        'age': 20,
        'is_student': True,
    })


@pytest.fixture
def middle_or_high_school():
    return pmap({
        'age': 15,
        'is_student': True,
        'is_middle_or_high_school': True,
    })


@pytest.fixture
def elementary_school_or_younger():
    return pmap({
        'age': 10,
        'is_student': True,
        'is_elementary_school_or_younger': True,
    })


@pytest.mark.parametrize('screening_datetime, expected', [
    (screening_datetime_test_data['weekday_daytime'], pmap({'price': 1900, 'currency': 'JPY'})),
    (screening_datetime_test_data['weekday_late_show'], pmap({'price': 1400, 'currency': 'JPY'})),
    (screening_datetime_test_data['holiday_daytime'], pmap({'price': 1900, 'currency': 'JPY'})),
    (screening_datetime_test_data['holiday_late_show'], pmap({'price': 1400, 'currency': 'JPY'})),
    (screening_datetime_test_data['movie_day_daytime'], pmap({'price': 1200, 'currency': 'JPY'})),
    (screening_datetime_test_data['movie_day_late_show'], pmap({'price': 1200, 'currency': 'JPY'})),
])
def test_general_user(ticket_price_data, general_user, screening_datetime, expected):
    assert expected == ticket_price.calculate(ticket_price_data, general_user, screening_datetime)


@pytest.mark.parametrize('screening_datetime, expected', [
    (screening_datetime_test_data['weekday_daytime'], pmap({'price': 1200, 'currency': 'JPY'})),
    (screening_datetime_test_data['weekday_late_show'], pmap({'price': 1200, 'currency': 'JPY'})),
    (screening_datetime_test_data['holiday_daytime'], pmap({'price': 1200, 'currency': 'JPY'})),
    (screening_datetime_test_data['holiday_late_show'], pmap({'price': 1200, 'currency': 'JPY'})),
    (screening_datetime_test_data['movie_day_daytime'], pmap({'price': 1200, 'currency': 'JPY'})),
    (screening_datetime_test_data['movie_day_late_show'], pmap({'price': 1200, 'currency': 'JPY'})),
])
def test_senior_user(ticket_price_data, senior_user, screening_datetime, expected):
    assert expected == ticket_price.calculate(ticket_price_data, senior_user, screening_datetime)


@pytest.mark.parametrize('screening_datetime, expected', [
    (screening_datetime_test_data['weekday_daytime'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['weekday_late_show'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['holiday_daytime'], pmap({'price': 1300, 'currency': 'JPY'})),
    (screening_datetime_test_data['holiday_late_show'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['movie_day_daytime'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['movie_day_late_show'], pmap({'price': 1000, 'currency': 'JPY'})),
    # 土日祝が映画の日で、昼間の場合だけ、映画の日の値段が適用される
    (datetime.datetime(2023, 4, 1, 12, 0, 0), pmap({'price': 1200, 'currency': 'JPY'})),
    (datetime.datetime(2023, 4, 1, 21, 0, 0), pmap({'price': 1000, 'currency': 'JPY'})),
])
def test_member_user(ticket_price_data, member_user, screening_datetime, expected):
    assert expected == ticket_price.calculate(ticket_price_data, member_user, screening_datetime)


@pytest.mark.parametrize('screening_datetime, expected', [
    (screening_datetime_test_data['weekday_daytime'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['weekday_late_show'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['holiday_daytime'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['holiday_late_show'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['movie_day_daytime'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['movie_day_late_show'], pmap({'price': 1000, 'currency': 'JPY'})),
])
def test_senior_member_user(ticket_price_data, senior_member_user, screening_datetime, expected):
    assert expected == ticket_price.calculate(ticket_price_data, senior_member_user, screening_datetime)


@pytest.mark.parametrize('screening_datetime, expected', [
    (screening_datetime_test_data['weekday_daytime'], pmap({'price': 1500, 'currency': 'JPY'})),
    (screening_datetime_test_data['weekday_late_show'], pmap({'price': 1400, 'currency': 'JPY'})),
    (screening_datetime_test_data['holiday_daytime'], pmap({'price': 1500, 'currency': 'JPY'})),
    (screening_datetime_test_data['holiday_late_show'], pmap({'price': 1400, 'currency': 'JPY'})),
    (screening_datetime_test_data['movie_day_daytime'], pmap({'price': 1200, 'currency': 'JPY'})),
    (screening_datetime_test_data['movie_day_late_show'], pmap({'price': 1200, 'currency': 'JPY'})),
])
def test_students_user(ticket_price_data, students_user, screening_datetime, expected):
    assert expected == ticket_price.calculate(ticket_price_data, students_user, screening_datetime)


@pytest.mark.parametrize('screening_datetime, expected', [
    (screening_datetime_test_data['weekday_daytime'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['weekday_late_show'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['holiday_daytime'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['holiday_late_show'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['movie_day_daytime'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['movie_day_late_show'], pmap({'price': 1000, 'currency': 'JPY'})),
])
def test_middle_or_high_school(ticket_price_data, middle_or_high_school, screening_datetime, expected):
    assert expected == ticket_price.calculate(ticket_price_data, middle_or_high_school, screening_datetime)


@pytest.mark.parametrize('screening_datetime, expected', [
    (screening_datetime_test_data['weekday_daytime'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['weekday_late_show'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['holiday_daytime'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['holiday_late_show'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['movie_day_daytime'], pmap({'price': 1000, 'currency': 'JPY'})),
    (screening_datetime_test_data['movie_day_late_show'], pmap({'price': 1000, 'currency': 'JPY'})),
])
def test_elementary_school_or_younger(ticket_price_data, elementary_school_or_younger, screening_datetime, expected):
    assert expected == ticket_price.calculate(ticket_price_data, elementary_school_or_younger, screening_datetime)
