from hebrew import Hebrew
from hebrew.chars import HEBREW_CHARS
from hebrew.gematria import GematriaTypes


def test_mispar_katan_char_values():
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
        "י": 1,
        "כ": 2,
        "ך": 2,
        "ל": 3,
        "מ": 4,
        "ם": 4,
        "נ": 5,
        "ן": 5,
        "ס": 6,
        "ע": 7,
        "פ": 8,
        "ף": 8,
        "צ": 9,
        "ץ": 9,
        "ק": 1,
        "ר": 2,
        "ש": 3,
        "ת": 4,
    }
    for char in HEBREW_CHARS:
        assert char.mispar_katan == values[char.char[0]]


def test_mispar_katan_type_value():
    assert GematriaTypes.MISPAR_KATAN.value == "mispar_katan"


def test_mispar_katan():
    assert Hebrew("ךָ").gematria(GematriaTypes.MISPAR_KATAN) == 2
    assert Hebrew("כ").gematria(GematriaTypes.MISPAR_KATAN) == 2
    assert Hebrew("מספר קטן").gematria(GematriaTypes.MISPAR_KATAN) == 35
    assert Hebrew("English" + "מספר קטן").gematria(GematriaTypes.MISPAR_KATAN) == 35
    assert (
        Hebrew("אבגדהוזחטיכךלמםנןסעפףצץקרשת").gematria(GematriaTypes.MISPAR_KATAN)
        == 128
    )
