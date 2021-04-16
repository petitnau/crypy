from crypy.aes import padding_oracle_attack
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def oracle_example(ct, gen_ct=None):
    key = b"YELLOW SUBMARINE"
    iv = key
    aes = AES.new(key, AES.MODE_CBC, iv)

    if gen_ct is not None:
        return aes.encrypt(pad(gen_ct, 16))

    try:
        unpad(aes.decrypt(ct), 16)
        return True
    except ValueError:
        return False


def test_padding_oracle():
    pt = b"In cryptography, a padding oracle attack is an attack which uses the padding validation of a cryptographic message to decrypt the ciphertext."
    ct = oracle_example("", gen_ct=pt)
    assert pad(pt, 16)[16:] == padding_oracle_attack(oracle_example, ct)
