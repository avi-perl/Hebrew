from hebrew.chars import *
from hebrew.chars import _ALL_CHARS


def test_hebrew_char_hebrew_names():
    tsadi_sofit = HebrewChar(
        char="ץ",
        name="Tsadi Sofit",
        final_letter=True,
        hebrew_name="צַדִי סוֹפִית",
        hebrew_name_alts=["צדיק סופית"],
    )
    assert sorted(tsadi_sofit.hebrew_names) == sorted(["צַדִי סוֹפִית", "צדיק סופית"])


def test_hebrew_char_names():
    aleph = HebrewChar(char="א", name="Aleph", hebrew_name="אָלֶף", name_alts=["Alef"])
    assert sorted(aleph.names) == sorted(["Aleph", "Alef"])


def test_hebrew_char_str():
    aleph = HebrewChar(char="א", name="Aleph", hebrew_name="אָלֶף", name_alts=["Alef"])
    assert str(aleph) == "א"


def test_hebrew_char_search():
    assert isinstance(
        HebrewChar.search("Aleph"), HebrewChar
    ), "HebrewChar.search should return a HebrewChar instance"
    assert isinstance(
        HebrewChar.search("aLEPH"), HebrewChar
    ), "Should be case insensitive"
    assert HebrewChar.search("Bad Value") is None


def test_hebrew_char_search_use_alt_names():
    search_result = HebrewChar.search("Hei")
    assert isinstance(search_result, HebrewChar)
    assert search_result.char == "ה"
    assert search_result.name != "Hei"


def test_final_letters():
    final_chars = ["ץ", "ף", "ן", "ם", "ך"]
    assert len(final_chars) == len(FINAL_LETTERS)
    for char in final_chars:
        assert char in [c.char for c in FINAL_LETTERS]


def test_yiddish_chars():
    yiddish_letters = ["ױ", "װ", "ײ"]
    assert len(yiddish_letters) == len(YIDDISH_CHARS)
    for char in yiddish_letters:
        assert char in [c.char for c in YIDDISH_CHARS]


def test_niqqud_chars():
    assert len(NIQQUD_CHARS) > 0
    for char in NIQQUD_CHARS:
        assert type(char) == NiqqudChar


def test_punctuation_chars():
    assert len(PUNCTUATION_CHARS) > 0
    for char in PUNCTUATION_CHARS:
        assert type(char) == PunctuationChar


def test_char_dict():
    assert len(CHARS) == len(
        _ALL_CHARS
    ), "The _ALL_CHARS array may contain values with duplicate char values"