from crypy.hash.sha256 import SHA256


def test_sha256_yellowsub():
    assert SHA256("YELLOW SUBMARINE").hexdigest() == "876a397347432ede4fb5448a439b62e191e09daa925fdc48e63440a868924ad1"


def test_sha256_extend():
    secret = b"123SECRET"
    msg = b"messaggio normale"
    dig = SHA256(secret+msg).digest()

    base, h_clone = SHA256.clone(len(secret), msg, dig)
    extension = b"extended"
    h_clone.update(extension)
    tot_msg = base+extension

    assert h_clone.digest() == SHA256(secret+tot_msg).digest()