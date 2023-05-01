def get(m, path: list):
    res = m
    for key in path:
        res = res[key]
    return res
