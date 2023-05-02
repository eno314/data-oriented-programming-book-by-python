from pyrsistent import pmap


def price_data(price: int) -> pmap:
    return pmap({
        'price': price,
        'currency': 'JPY',
    })


def datetime_price_data(
        daytime_price: int,
        late_show_price: int,
        movie_day_price: int
) -> pmap:
    return pmap({
        'daytime': price_data(daytime_price),
        'late_show': price_data(late_show_price),
        'movie_day': price_data(movie_day_price),
    })


ticket_data = pmap({
    'general': pmap({
        'weekday': datetime_price_data(1900, 1400, 1200),
    })
})
