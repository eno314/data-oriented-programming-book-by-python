from pyrsistent import PMap, pmap


def get() -> PMap:
    return pmap({
        'general': pmap({
            'weekday': _datetime_price_data(1900, 1400),
            'holiday': _datetime_price_data(1900, 1400),
            'movie_day': _datetime_price_data(1200, 1200),
        }),
        'senior': pmap({
            'weekday': _datetime_price_data(1200, 1200),
            'holiday': _datetime_price_data(1200, 1200),
            'movie_day': _datetime_price_data(1200, 1200),
        }),
        'member': pmap({
            'weekday': _datetime_price_data(1000, 1000),
            'holiday': _datetime_price_data(1300, 1000),
            'movie_day': _datetime_price_data(1200, 1200),
        }),
        'senior_member': pmap({
            'weekday': _datetime_price_data(1000, 1000),
            'holiday': _datetime_price_data(1000, 1000),
            'movie_day': _datetime_price_data(1000, 1000),
        }),
        'student': pmap({
            'weekday': _datetime_price_data(1500, 1400),
            'holiday': _datetime_price_data(1500, 1400),
            'movie_day': _datetime_price_data(1200, 1200),
        }),
        'middle_or_high_school_student': pmap({
            'weekday': _datetime_price_data(1000, 1000),
            'holiday': _datetime_price_data(1000, 1000),
            'movie_day': _datetime_price_data(1000, 1000),
        }),
        'elementary_school_or_younger_student': pmap({
            'weekday': _datetime_price_data(1000, 1000),
            'holiday': _datetime_price_data(1000, 1000),
            'movie_day': _datetime_price_data(1000, 1000),
        }),
        'general_with_disability': pmap({
            'weekday': _datetime_price_data(1000, 1000),
            'holiday': _datetime_price_data(1000, 1000),
            'movie_day': _datetime_price_data(1000, 1000),
        }),
        'younger_with_disability': pmap({
            'weekday': _datetime_price_data(900, 900),
            'holiday': _datetime_price_data(900, 900),
            'movie_day': _datetime_price_data(900, 900),
        }),
    })


def _datetime_price_data(daytime_price: int, late_show_price: int) -> PMap:
    return pmap({
        'daytime': _price_data(daytime_price),
        'late_show': _price_data(late_show_price),
    })


def _price_data(price: int) -> PMap:
    return pmap({
        'price': price,
        'currency': 'JPY',
    })
