from crypy.hash.md5 import MD5


def test_md5_extend():
    secret = b"123SECRET"
    msg = b"messaggio normale"
    h = MD5(secret+msg)
    h.test()
    dig = h.digest()

    base, h_clone = MD5.clone(len(secret), msg, dig)
    extension = b"extended"
    h_clone.update(extension)
    tot_msg = base+extension

    assert h_clone.digest() == MD5(secret+tot_msg).digest()

def test_md5():
    hashes = [
        ("ciao", "6e6bc4e49dd477ebc98ef4046c067b5f"),
        ("long long long long long long long really long test", "024b394e7c7693798abb230ae256787e")
    ]

    md5 = MD5()
    md5.update(hashes[0][0])
    assert md5.hexdigest() == hashes[0][1]

    assert MD5().update(hashes[0][0]).hexdigest() == hashes[0][1]

    assert MD5(hashes[0][0]).hexdigest() == hashes[0][1]

    assert MD5(hashes[1][0]).hexdigest() == hashes[1][1]
