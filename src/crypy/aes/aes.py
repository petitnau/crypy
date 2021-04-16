from Crypto.Util.strxor import strxor


def padding_oracle_attack(oracle, ct):
    blocks = [ct[i:i+16] for i in range(0, len(ct), 16)]

    founds = []
    for i in range(1, len(blocks))[::-1]:
        found = b""
        for j in range(1, 17):
            base_xor = b"\x00"*(16*(i-1)) + b"\x00"*(16-j) + bytes([j])*j + b"\x00"*16
            for k in range(0, 256):
                if k == j:
                    continue
                new_byte = bytes([k])
                xor = b"\x00"*(16*(i-1)) + b"\x00"*(16-j) + new_byte + found + b"\x00"*16

                if oracle(strxor(base_xor, strxor(b"".join(blocks[:i+1]), xor))):
                    found = new_byte + found
                    break
            else:
                found = bytes([j]) + found
        founds = [found] + founds
    return b"".join(founds)
