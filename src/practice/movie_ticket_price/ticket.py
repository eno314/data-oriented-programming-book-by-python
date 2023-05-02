import datetime

import pydash
from pyrsistent import PMap

from src.practice.movie_ticket_price import screening_datetime


def calculate_price(
        ticket_data: PMap,
        user_data: PMap,
        screening_datetime_data: datetime.datetime
) -> PMap:
    screening_datetime_type = _get_screening_datetime_type(screening_datetime_data)
    return pydash.get(ticket_data, ['general', 'weekday', screening_datetime_type])


def _get_screening_datetime_type(screening_datetime_data: datetime.datetime) -> str:
    if screening_datetime.is_movie_day(screening_datetime_data):
        return 'movie_day'
    if screening_datetime.is_late_show(screening_datetime_data):
        return 'late_show'
    else:
        return 'daytime'
