from pyrsistent import pmap


def price_data(price: int) -> pmap:
    return pmap({
        'price': price,
        'currency': 'JPY',
    })


def datetime_price_data(
        daytime_price: int,
        late_show_price: int,
) -> pmap:
    return pmap({
        'daytime': price_data(daytime_price),
        'late_show': price_data(late_show_price),
    })


ticket_data = pmap({
    'general': pmap({
        'weekday': datetime_price_data(1900, 1400),
        'holiday': datetime_price_data(1900, 1400),
        'movie_day': datetime_price_data(1200, 1200),
    }),
    'senior': pmap({
        'weekday': datetime_price_data(1200, 1200),
        'holiday': datetime_price_data(1200, 1200),
        'movie_day': datetime_price_data(1200, 1200),
    }),
    'member': pmap({
        'weekday': datetime_price_data(1000, 1000),
        'holiday': datetime_price_data(1300, 1000),
        'movie_day': datetime_price_data(1200, 1200),
    }),
    'senior_member': pmap({
        'weekday': datetime_price_data(1000, 1000),
        'holiday': datetime_price_data(1000, 1000),
        'movie_day': datetime_price_data(1000, 1000),
    }),
    'student': pmap({
        'weekday': datetime_price_data(1500, 1400),
        'holiday': datetime_price_data(1500, 1400),
        'movie_day': datetime_price_data(1200, 1200),
    }),
    'middle_or_high_school_student': pmap({
        'weekday': datetime_price_data(1000, 1000),
        'holiday': datetime_price_data(1000, 1000),
        'movie_day': datetime_price_data(1000, 1000),
    }),
    'elementary_school_or_younger_student': pmap({
        'weekday': datetime_price_data(1000, 1000),
        'holiday': datetime_price_data(1000, 1000),
        'movie_day': datetime_price_data(1000, 1000),
    }),
})
