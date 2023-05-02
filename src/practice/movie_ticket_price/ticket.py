import datetime

import pydash
from pyrsistent import PMap, pvector, PVector

from src.practice.movie_ticket_price import screening_datetime, user


def calculate_price(
        ticket_data: PMap,
        user_data: PMap,
        screening_datetime_data: datetime.datetime
) -> PMap:
    prices = []
    for user_type in _get_user_types(user_data):
        for date_type in _get_screening_date_types(screening_datetime_data):
            time_type = _get_screening_time_type(screening_datetime_data)
            prices.append(pydash.get(ticket_data, [user_type, date_type, time_type]))
    return min(prices, key=lambda price_data: price_data['price'])


def _get_user_types(user_data: PMap) -> PVector:
    types = ['general']
    if pydash.get(user_data, 'is_member', False):
        types.append('member')
    if user.is_senior(user_data):
        types.append('senior')
    return pvector(types)


def _get_screening_date_types(screening_datetime_data: datetime.datetime) -> PVector:
    types = []
    if screening_datetime.is_movie_day(screening_datetime_data):
        types.append('movie_day')
    if screening_datetime.is_weekend(screening_datetime_data):
        types.append('weekend')
    else:
        types.append('weekday')
    return pvector(types)


def _get_screening_time_type(screening_datetime_data: datetime.datetime) -> str:
    if screening_datetime.is_late_show(screening_datetime_data):
        return 'late_show'
    return 'daytime'
