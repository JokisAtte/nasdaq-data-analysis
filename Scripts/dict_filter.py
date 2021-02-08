def dict_filter(it, *keys):
    for d in it:
        yield dict((k, d[k]) for k in keys)
