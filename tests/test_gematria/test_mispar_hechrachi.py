from hebrew import Hebrew
from hebrew.chars import HEBREW_CHARS
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
