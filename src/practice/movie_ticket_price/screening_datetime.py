import datetime


def is_movie_day(screening_datetime_data: datetime.datetime) -> bool:
    return screening_datetime_data.day == 1


def is_holiday(screening_datetime_data: datetime.datetime) -> bool:
    # TODO: Implement national holiday
    return screening_datetime_data.weekday() >= 5


def is_late_show(screening_datetime_data: datetime.datetime) -> bool:
    return screening_datetime_data.hour >= 20
