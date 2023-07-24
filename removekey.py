def removekey(d, key):
    r = dict(d)
    r.pop(key, None)

    return r