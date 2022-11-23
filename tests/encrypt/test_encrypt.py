from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("AABBCC", 3) == "BAA_CCB"
    assert encrypt_message("ABBCCA", 4) == "AC_CBBA"
    assert encrypt_message("AABBCC", -1) == "CCBBAA"

    with pytest.raises(TypeError):
        encrypt_message(2, 5)
    with pytest.raises(TypeError):
        encrypt_message(None, None)
    with pytest.raises(TypeError):
        encrypt_message("AABBCC", "AA")
