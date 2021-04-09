from crypy.utils import maths

def test_introot():
    assert maths.int_root(2, 9) == 3
    assert maths.int_root(5, 14348907) == 27
    assert maths.int_root(27, 7450580596923828125) == 5
