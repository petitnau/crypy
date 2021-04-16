from crypy.random.mt import MT19937
import random


def test_mersenne_seed0():
    mt = MT19937(0)
    generated = [mt.random() for _ in range(20)]
    correct = [2357136044, 2546248239, 3071714933, 3626093760, 2588848963, 3684848379, 2340255427, 3638918503, 1819583497, 2678185683, 2774094101, 1650906866, 1879422756, 1277901399, 3830135878, 243580376, 4138900056, 1171049868, 1646868794, 2051556033]
    assert correct == generated


def test_mersenne_623():
    mt = MT19937(random.randint(0, 2**32))
    clone = MT19937(0, [mt.random() for _ in range(624)])

    assert [mt.random() for _ in range(100)] == [clone.random() for _ in range(100)]
