from crypy.hash.sha256 import SHA256


def test_sha256_extend():
    secret = b"123SECRET"
    msg = b"messaggio normale"
    dig = SHA256(secret+msg).digest()

    base, h_clone = SHA256.clone(len(secret), msg, dig)
    extension = b"extended"
    h_clone.update(extension)
    tot_msg = base+extension

    assert h_clone.digest() == SHA256(secret+tot_msg).digest()


def test_sha256():
    hashes = [
        ("ciao",
            "b133a0c0e9bee3be20163d2ad31d6248db292aa6dcb1ee087a2aa50e0fc75ae2"),
        ("long long long long long long long really long test",
            "33ab101d3d06a129884dc376c234c57093a4f8b2a21ea22a3a9488dcfc9056a7")
    ]

    sha256 = SHA256()
    sha256.update(hashes[0][0])
    assert sha256.hexdigest() == hashes[0][1]

    assert SHA256().update(hashes[0][0]).hexdigest() == hashes[0][1]

    assert SHA256(hashes[0][0]).hexdigest() == hashes[0][1]

    assert SHA256(hashes[1][0]).hexdigest() == hashes[1][1]
