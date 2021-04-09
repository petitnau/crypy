def int_root (n, radicand):
    if radicand < 2:
        return radicand
    a1 = n - 1
    c = 1
    d = (a1 * c + radicand // (c ** a1)) // n
    e = (a1 * d + radicand // (d ** a1)) // n
    while c not in (d, e):
        c, d, e = d, e, (a1 * e + radicand // (e ** a1)) // n
    return min(d, e)


def test_introot():
    assert int_root(2, 9) == 3
    assert int_root(5, 14348907) == 27
    assert int_root(27, 7450580596923828125) == 5
