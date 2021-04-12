from crypy.random.lcg import LCG


def generate_acms():
    a = 1076867677
    c = 1265354953
    m = 2147483647
    s = 1862611659
    return a, c, m, s


def test_lcg_known():
    a = 1076867677
    c = 1265354953
    m = 2147483647
    s = 1862611659
    lcg = LCG(a, c, m, s)
    generated = [next(lcg) for _ in range(50)]
    correct = [143743627, 1560228317, 453103692, 694699224, 244747178, 1891593979, 885021405, 1031883428, 1547534045, 1221371806, 1960050069, 733022552, 273427025, 965648908, 1039778495, 414535582, 17526272, 1368709488, 36141448, 1464863092, 304508342, 1227762217, 482014640, 1675860288, 713030253, 123494352, 1299850606, 1692258118, 1787641562, 1977845183, 1530977757, 898989051, 1356992132, 778961334, 239419866, 1082932025, 2137004426, 1397524344, 1295498570, 26715490, 776694779, 942833450, 1192451962, 1088583680, 2108344923, 1491323609, 597778573, 2112806192, 2079579906, 328814666]
    assert correct == generated


def test_lcg_missing_c():
    a, c, m, s = generate_acms()
    lcg = LCG(a, c, m, s)
    rep = LCG(a, None, m, [next(lcg) for _ in range(2)])
    assert [next(lcg) for _ in range(50)] == [next(rep) for _ in range(50)]

def test_lcg_missing_a():
    a, c, m, s = generate_acms()
    lcg = LCG(a, c, m, s)
    rep = LCG(None, c, m, [next(lcg) for _ in range(2)])
    assert [next(lcg) for _ in range(50)] == [next(rep) for _ in range(50)]


def test_lcg_missing_ac():
    a, c, m, s = generate_acms()
    lcg = LCG(a, c, m, s)
    rep = LCG(None, None, m, [next(lcg) for _ in range(3)])
    assert [next(lcg) for _ in range(50)] == [next(rep) for _ in range(50)]


def test_lcg_missing_acm():
    a, c, m, s = generate_acms()
    lcg = LCG(a, c, m, s)
    rep = LCG(None, None, None, [next(lcg) for _ in range(5)])
    assert [next(lcg) for _ in range(50)] == [next(rep) for _ in range(50)]
