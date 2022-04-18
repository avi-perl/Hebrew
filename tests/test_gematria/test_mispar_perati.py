from hebrew import Hebrew
from hebrew.chars import HEBREW_CHARS
from hebrew.gematria import GematriaTypes


def test_mispar_perati_char_values():
    values = {
        "א": 1,
        "ב": 4,
        "ג": 9,
        "ד": 16,
        "ה": 25,
        "ו": 36,
        "ז": 49,
        "ח": 64,
        "ט": 81,
        "י": 100,
        "כ": 400,
        "ך": 400,
        "ל": 900,
        "מ": 1600,
        "ם": 1600,
        "נ": 2500,
        "ן": 2500,
        "ס": 3600,
        "ע": 4900,
        "פ": 6400,
        "ף": 6400,
        "צ": 8100,
        "ץ": 8100,
        "ק": 10000,
        "ר": 40000,
        "ש": 90000,
        "ת": 160000,
    }
    for char in HEBREW_CHARS:
        assert char.mispar_perati == values[char.char[0]]


def test_mispar_perati_type_value():
    assert GematriaTypes.MISPAR_PERATI.value == "mispar_perati"


def test_mispar_perati():
    assert Hebrew("ךָ").gematria(GematriaTypes.MISPAR_PERATI) == 400
    assert Hebrew("כ").gematria(GematriaTypes.MISPAR_PERATI) == 400
    assert Hebrew("מספר הפרטי").gematria(GematriaTypes.MISPAR_PERATI) == 98206
    assert (
        Hebrew("English" + "מספר הפרטי").gematria(GematriaTypes.MISPAR_PERATI) == 98206
    )
    assert (
        Hebrew(
            "אבגדהוזחטיכךלמםנןסעפףצץקרשת"
        ).gematria(GematriaTypes.MISPAR_PERATI)
        == 347785
    )
