from crypy.rsa.rsa import RSA

import functools
import operator
from Crypto.Util.number import getPrime
from sympy import nextprime

def test_no_modulo_attack():
    n = 124583092829974391600467668877327614386279463848745073431816780729414525076648674364985001549546545152978862199879341112048846547008259952102848496766653125298852453324023664866682307604444862714811837979157632738565310818890959586170060523117996098784222836036866708911323582660878065405959413009853186245737
    e = 5
    ct = 58813852308064219943699940485659581072340499649260269048860030761053147517476995198116610746394475714151238095349070361396803406144949533629373226279384045848075813366308294614452894658772009087450526287659127382318633844024267741646775949
    rsa = RSA(n, e)
    pt = rsa.no_modulo_attack(ct)
    assert bytearray.fromhex(hex(pt)[2:]) == b"cc{usa_e_piu_grandi}"


def test_find_pq():
    n = 134871459832923860099882590902411996710996766501756653086495354300954191050110475349218593219906710987168729946490859346117437393705213066464123381634516073655104369957424501917959364716066521838138728063315157921217685558557422845878448233922585713677077217815414960315913375048754314176130997193108410703707
    e = 65537
    d = 19546349779408743507159083393977587389734764914989772052665408473846268620686776856842366882870347146743497520969378855752070133900119225861364479282918556646891456167647366904804199245738822376442388779257291859758735359459148377679538927373263135165396852614400167982261412234666697210259242937381901648593
    rsa = RSA(n, e, d)
    for i in range(1000):
        res = rsa.try_find_pq()
        if res:
            break
    else:
        assert False

    assert functools.reduce(operator.mul, res) == n


def test_close_primes_attack():
    for i in range(2, 10):
        primes = [getPrime(128)]
        for j in range(1, i):
            primes.append(nextprime(primes[-1]))
        n = functools.reduce(operator.mul, primes)
        rsa = RSA(n, 65537)
        found = rsa.close_primes_attack(i)
        assert found == primes