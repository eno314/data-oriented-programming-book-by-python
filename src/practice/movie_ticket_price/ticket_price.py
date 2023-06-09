import datetime

import pydash
from pyrsistent import PMap, pvector, PVector

from src.practice.movie_ticket_price import screening_datetime, user


def calculate(
        ticket_price_data: PMap,
        user_data: PMap,
        screening_datetime_data: datetime.datetime
) -> PMap:
    target_prices = _get_target_prices(ticket_price_data, user_data, screening_datetime_data)
    print(len(target_prices))
    return min(target_prices, key=lambda price_data: pydash.get(price_data, 'price'))


def _get_target_prices(
        ticket_price_data: PMap,
        user_data: PMap,
        screening_datetime_data: datetime.datetime
) -> PVector:
    prices = set()
    for user_type in _get_user_types(user_data):
        for date_type in _get_screening_date_types(screening_datetime_data):
            time_type = _get_screening_time_type(screening_datetime_data)
            prices.add(pydash.get(ticket_price_data, [user_type, date_type, time_type]))
    return pvector(list(prices))


def _get_user_types(user_data: PMap) -> PVector:
    return pvector(list({
        _get_user_senior_type(user_data),
        _get_user_member_type(user_data),
        _get_user_student_type(user_data),
        _get_user_disability_type(user_data),
    }))


def _get_user_senior_type(user_data: PMap) -> str:
    if not user.is_senior(user_data):
        return 'general'
    return 'senior'


def _get_user_member_type(user_data: PMap) -> str:
    if not pydash.get(user_data, 'is_member', False):
        return 'general'
    if user.is_senior_for_member(user_data):
        return 'senior_member'
    return 'member'


def _get_user_student_type(user_data: PMap) -> str:
    if not pydash.get(user_data, 'is_student', False):
        return 'general'
    if pydash.get(user_data, 'is_elementary_school_or_younger', False):
        return 'elementary_school_or_younger_student'
    if pydash.get(user_data, 'is_middle_or_high_school', False):
        return 'middle_or_high_school_student'
    return 'student'


def _get_user_disability_type(user_data: PMap) -> str:
    if not pydash.get(user_data, 'has_disability', False):
        return 'general'
    student_type = _get_user_student_type(user_data)
    if student_type in ['elementary_school_or_younger_student', 'middle_or_high_school_student']:
        return 'younger_with_disability'
    return 'general_with_disability'


def _get_screening_date_types(screening_datetime_data: datetime.datetime) -> PVector:
    types = []
    if screening_datetime.is_movie_day(screening_datetime_data):
        types.append('movie_day')
    if screening_datetime.is_holiday(screening_datetime_data):
        types.append('holiday')
    else:
        types.append('weekday')
    return pvector(types)


def _get_screening_time_type(screening_datetime_data: datetime.datetime) -> str:
    if screening_datetime.is_late_show(screening_datetime_data):
        return 'late_show'
    return 'daytime'
