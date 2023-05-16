from base62_token import base62


def test_encode():
    assert base62.encode(bytes([0])) == "00"
    assert base62.encode(b"") == ""


def test_decode():
    assert base62.decode("00") == bytes([0])
    assert base62.decode("") == b""


def test_compat():
    raw = "Hello, 世界".encode()
    encoded = "1wJfrzvdbuFbL65vcS"

    assert base62.encode(raw) == encoded
    assert base62.decode(encoded) == raw

    raw = b"Hello World"
    encoded = "73XpUgyMwkGr29M"

    assert base62.encode(raw) == encoded
    assert base62.decode(encoded) == raw

    raw = bytes([0, 0, 0, 0, 255, 255, 255, 255])
    encoded = "000004gfFC3"

    assert base62.encode(raw) == encoded
    assert base62.decode(encoded) == raw

    raw = bytes([255, 255, 255, 255, 0, 0, 0, 0])
    encoded = "LygHZwPV2MC"

    assert base62.encode(raw) == encoded
    assert base62.decode(encoded) == raw


def test_random():
    import secrets

    for _ in range(1024):
        r = secrets.token_bytes()
        assert base62.decode(base62.encode(r)) == r
