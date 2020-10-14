def euclid(eiler, e):

    x1, x2, y1, y2 = 1, 0, 0, 1
    while e:
        x1, x2, y1, y2 = x2, x1 - x2 * (eiler // e), y2, y1 - y2 * (eiler // e)
        eiler, e = e, eiler % e

    return y1
