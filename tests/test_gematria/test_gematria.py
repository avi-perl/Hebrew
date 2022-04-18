from hebrew.chars import *
from hebrew import Hebrew
from hebrew.gematria import GematriaTypes


def test_bad_input():
    for t in GematriaTypes:
        assert (
            Hebrew("Testing a string that contains no hebrew").gematria(t) == 0
        ), "gematria should return 0 when the input text is not hebrew"


def test_mixed_input():
    for t in GematriaTypes:
        assert (
            Hebrew("Both hebrew: 'שָׁלוֹם' and English: 'Hello dev!'").gematria(t) > 0
        ), "gematria should always have a value > 0 when there is any hebrew text in a string"
