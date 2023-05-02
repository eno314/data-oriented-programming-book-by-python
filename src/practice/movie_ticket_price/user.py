import pydash
from pyrsistent import PMap


def is_senior(user_data: PMap) -> bool:
    return pydash.get(user_data, 'age') >= 70
