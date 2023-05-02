import datetime

import pydash
from pyrsistent import PMap

from src.practice.movie_ticket_price import screening_datetime, user


def calculate_price(
        ticket_data: PMap,
        user_data: PMap,
        screening_datetime_data: datetime.datetime
) -> PMap:
    user_type = _get_user_type(user_data)
    date_type = _get_screening_date_type(screening_datetime_data)
    time_type = _get_screening_time_type(screening_datetime_data)
    return pydash.get(ticket_data, [user_type, date_type, time_type])


def _get_user_type(user_data: PMap) -> str:
    if user.is_senior(user_data):
        return 'senior'
    return 'general'


def _get_screening_date_type(screening_datetime_data: datetime.datetime) -> str:
    if screening_datetime.is_movie_day(screening_datetime_data):
        return 'movie_day'
    if screening_datetime.is_weekend(screening_datetime_data):
        return 'weekend'
    return 'weekday'


def _get_screening_time_type(screening_datetime_data: datetime.datetime) -> str:
    if screening_datetime.is_late_show(screening_datetime_data):
        return 'late_show'
    return 'daytime'
