import itertools
import string
from hashlib import sha256


def proof_of_work(prefix=b"", postfix=b"", prehash=b"", posthash=b"", hashfun=lambda x: sha256(x).digest(), noncelength=8):
    if type(prefix) == str:
        prefix = prefix.encode()
    if type(postfix) == str:
        postfix = postfix.encode()
    if type(prehash) == str:
        prehash = prehash.encode()
    if type(posthash) == str:
        posthash = posthash.encode()
    
    for c in itertools.product(string.ascii_lowercase, repeat=noncelength):
        s = prefix + "".join(c).encode() + postfix
        h = hashfun(s)
        if h[-len(posthash):] == posthash and h[:len(prehash)] == prehash:
            return s
