from .caesar import *


def test_encrypt():
    key = 1
    pt = "Ciao Come Stai"
    ct = encrypt(pt, key)
    assert ct == "Djbp Dpnf Tubj"
    assert pt == decrypt(ct, key)
    assert breaker(ct) == key

    key = 15
    assert breaker(encrypt("Ciao sono roberto e questo è il mio messaggio", key), language="it") == key
