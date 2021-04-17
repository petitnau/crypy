from crypy.aes import padding_oracle_attack, postfix_attack
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def test_prefix_postfix_oracle():
    secret = b"very-long-prefix-damn-this-is-long"
    postfix = b"very-secret-formula-dont-share!!"

    for i in range(1, len(secret)+1):
        prefix = secret[:i]

        def prefix_postfix_oracle(pt):
            key = b"YELLOW SUBMARINE"
            aes = AES.new(key, AES.MODE_ECB)
            return aes.encrypt(pad(prefix+pt+postfix, 16))

        assert postfix == postfix_attack(prefix_postfix_oracle, prefix_len=i)


def test_postfix_oracle():
    secret = b"very-secret-formula-dont-share!!"

    for i in range(len(secret)+1):
        postfix = secret[:i]

        def postfix_oracle(pt):
            key = b"YELLOW SUBMARINE"
            aes = AES.new(key, AES.MODE_ECB)
            return aes.encrypt(pad(pt+postfix, 16))

        assert postfix == postfix_attack(postfix_oracle)


def test_padding_oracle():
    key = b"YELLOW SUBMARINE"
    aes_enc = AES.new(key, AES.MODE_CBC, key)
    aes_dec = AES.new(key, AES.MODE_CBC, key)
    pt = b"In cryptography, a padding oracle attack is an attack which uses the padding validation of a cryptographic message to decrypt the ciphertext."
    ct = aes_enc.encrypt(pad(pt, 16))

    def padding_oracle(ct):
        try:
            unpad(aes_dec.decrypt(ct), 16)
            return True
        except ValueError:
            return False

    assert pad(pt, 16)[16:] == padding_oracle_attack(padding_oracle, ct)
