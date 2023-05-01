def my_map(coll, f):
    res = []
    for col in coll:
        res.append(f(col))
    return res
