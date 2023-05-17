import secrets

from binascii import crc32
from warnings import warn

from . import base62


class SecurityWarning(Warning):
    """Warning about security risk"""


def generate(prefix: str = "jzr", entropy: int = 40) -> str:
    """Generate a base62 encoded token.

    Args:
        prefix (str, optional): The prefix used to identify the token type. Defaults to "jzr".
        entropy (int, optional): Entropy in bytes before encoding. Defaults to 40.

    Returns:
        str: A base62 encoded token.
    """

    if not isinstance(entropy, int):
        raise TypeError("entropy must be of type int")
    if not isinstance(prefix, str):
        raise TypeError("prefix must be of type str")

    if not prefix.isalnum():
        raise ValueError("prefix must be alphanumerical characters only")

    if entropy < secrets.DEFAULT_ENTROPY:
        warn(SecurityWarning("entropy < secrets.DEFAULT_ENTROPY"))

    secret = base62.encode(secrets.token_bytes(entropy))
    crc = base62.encode(crc32(base62.decode(secret)).to_bytes(4, "big"))
    token = f"{prefix}_{secret}_{crc}"

    return token


def is_valid(token: str) -> bool:
    """Checks if a token has a valid prefix and correct CRC.

    Args:
        token (str): The token to be checked.

    Returns:
        bool: True if the token is valid, False otherwise.
    """

    try:
        prefix, secret, crc = token.split("_")
        return prefix.isalnum() and crc == base62.encode(
            crc32(base62.decode(secret)).to_bytes(4, "big")
        )
    except Exception:
        return False


def is_valid_gh(token: str) -> bool:
    ghp_prefixes = ["ghp", "gho", "ghu", "ghs", "ghr"]

    prefix, tail = token.split("_")
    secret, crc = tail[:-6], tail[-6:]

    try:
        return prefix in ghp_prefixes and crc32(secret.encode()) == int.from_bytes(
            base62.decode(crc), "big"
        )
    except Exception:
        return False


def generate_gh(prefix: str = "ghp"):
    secret = "".join(secrets.choice(base62.alphabet) for _ in range(30))
    crc = base62.encode_int(crc32(secret.encode()))
    return f"{prefix}_{secret}{crc:>06}"
