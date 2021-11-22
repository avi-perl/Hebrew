from hebrew.chars import *
from hebrew import Hebrew
from hebrew.gematria import GematriaTypes


def test_mispar_hechrachi_char_values():
    values = {
        "א": 1,
        "ב": 2,
        "ג": 3,
        "ד": 4,
        "ה": 5,
        "ו": 6,
        "ז": 7,
        "ח": 8,
        "ט": 9,
        "י": 10,
        "כ": 20,
        "ך": 20,
        "ל": 30,
        "מ": 40,
        "ם": 40,
        "נ": 50,
        "ן": 50,
        "ס": 60,
        "ע": 70,
        "פ": 80,
        "ף": 80,
        "צ": 90,
        "ץ": 90,
        "ק": 100,
        "ר": 200,
        "ש": 300,
        "ת": 400,
    }
    for char in HEBREW_CHARS:
        assert char.mispar_hechrachi == values[char.char[0]]


def test_mispar_hechrachi_type_value():
    assert GematriaTypes.MISPAR_HECHRACHI.value == "mispar_hechrachi"


def test_mispar_hechrachi():
    assert Hebrew("בּ").gematria(GematriaTypes.MISPAR_HECHRACHI) == 2
    assert Hebrew("ב").gematria(GematriaTypes.MISPAR_HECHRACHI) == 2
    assert Hebrew("תורה").gematria(GematriaTypes.MISPAR_HECHRACHI) == 611
    assert Hebrew("English" + "תורה").gematria(GematriaTypes.MISPAR_HECHRACHI) == 611
    assert (
        Hebrew(
            "בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָרֶץ׃"
        ).gematria(GematriaTypes.MISPAR_HECHRACHI)
        == 2701
    )


def test_mispar_gadol_char_values():
    values = {
        "א": 1,
        "ב": 2,
        "ג": 3,
        "ד": 4,
        "ה": 5,
        "ו": 6,
        "ז": 7,
        "ח": 8,
        "ט": 9,
        "י": 10,
        "כ": 20,
        "ך": 500,
        "ל": 30,
        "מ": 40,
        "ם": 600,
        "נ": 50,
        "ן": 700,
        "ס": 60,
        "ע": 70,
        "פ": 80,
        "ף": 800,
        "צ": 90,
        "ץ": 900,
        "ק": 100,
        "ר": 200,
        "ש": 300,
        "ת": 400,
    }
    for char in HEBREW_CHARS:
        assert char.mispar_gadol == values[char.char[0]]


def test_mispar_gadol_type_value():
    assert GematriaTypes.MISPAR_GADOL.value == "mispar_gadol"


def test_mispar_gadol():
    assert Hebrew("ךָ").gematria(GematriaTypes.MISPAR_GADOL) == 500
    assert Hebrew("כ").gematria(GematriaTypes.MISPAR_GADOL) == 20
    assert Hebrew("קשת בענן").gematria(GematriaTypes.MISPAR_GADOL) == 1622
    assert Hebrew("English" + "קשת בענן").gematria(GematriaTypes.MISPAR_GADOL) == 1622
    assert (
        Hebrew(
            "עֲשָׂרָה דְבָרִים נִבְרְאוּ בְּעֶרֶב שַׁבָּת בֵּין הַשְּׁמָשׁוֹת"
        ).gematria(GematriaTypes.MISPAR_GADOL)
        == 4389
    )


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
