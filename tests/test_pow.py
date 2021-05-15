from crypy.utils.pow import proof_of_work
from hashlib import sha256, md5
import secrets

def test_pow_sha256():
    prefix = secrets.token_bytes(nbytes=4)
    postfix = secrets.token_bytes(nbytes=4)
    prehash = secrets.token_bytes(nbytes=1)
    posthash = secrets.token_bytes(nbytes=1)

    s = proof_of_work(prefix, postfix, prehash, posthash)
    h = sha256(s).digest()

    assert s.startswith(prefix) and s.endswith(postfix) and h.startswith(prehash) and h.endswith(posthash)

def test_pow_md5():
    prefix = secrets.token_bytes(nbytes=4)
    postfix = secrets.token_bytes(nbytes=4)
    prehash = secrets.token_bytes(nbytes=1)
    posthash = secrets.token_bytes(nbytes=1)

    s = proof_of_work(prefix, postfix, prehash, posthash, lambda x: md5(x).digest())
    h = md5(s).digest()

    assert s.startswith(prefix) and s.endswith(postfix) and h.startswith(prehash) and h.endswith(posthash)
