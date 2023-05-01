def my_get(m: dict, path: list):
    res = m
    for key in path:
        res = res[key]
    return res
