alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def encode(b: bytes, alphabet=alphabet):
    if b == b"":
        return ""

    leading_zeroes = len(b) - len(b.lstrip(b"\x00"))
    if leading_zeroes == len(b):
        return "0" + "0" * leading_zeroes

    num = int.from_bytes(b, "big")

    arr = encode_int(num, alphabet=alphabet)

    return ("0" * leading_zeroes) + ("0" if leading_zeroes else "") + "".join(arr)


def decode(s: str, alphabet=alphabet):
    base = len(alphabet)
    leading_zeroes = max(0, len(s) - len(s.lstrip("0")) - 1)
    s = s.lstrip("0")

    strlen = len(s)
    num = 0

    idx = 0

    for char in s:
        power = strlen - (idx + 1)
        num += alphabet.index(char) * (base**power)
        idx += 1

    return (b"\x00" * leading_zeroes) + num.to_bytes((num.bit_length() + 7) // 8, "big")

def encode_int(num: int, alphabet=alphabet):
    arr = []
    base = len(alphabet)

    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()

    return "".join(arr)