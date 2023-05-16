from base62_token import generate, is_valid, generate_gh, is_valid_gh
from base62_token.base62 import alphabet

import pytest


def test_token():
    with pytest.raises(ValueError):
        generate("")
    with pytest.raises(ValueError):
        generate("?")

    with pytest.warns():
        generate(entropy=1)

    for c in alphabet:
        assert is_valid(generate(c))

    assert not is_valid("zzz_aaa_zzz")
    assert not is_valid("_LH8WenA1DH7JtM1ShLEVv0fXu1Apqg3tVSPWMIbPcltwZPI2DL1vo0_BVmfh")
    assert not is_valid(
        "???_LH8WenA1DH7JtM1ShLEVv0fXu1Apqg3tVSPWMIbPcltwZPI2DL1vo0_BVmfh"
    )

    assert not is_valid(
        "jzr_LH8WenA1DH7JtM1ShLEVv0fXu1Apqg3tVSPWMIbPcltwZPI2DL1vo0_BVmf"
    )

    assert is_valid("jzr_LH8WenA1DH7JtM1ShLEVv0fXu1Apqg3tVSPWMIbPcltwZPI2DL1vo0_BVmfh")

def test_gh():
    # The scanners are going to go crazy over this. 
    token = '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'
    assert is_valid_gh(token)

    token = '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'
    assert is_valid_gh(token)

