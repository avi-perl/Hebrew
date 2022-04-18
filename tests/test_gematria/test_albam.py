from hebrew import Hebrew
from hebrew.chars import HEBREW_CHARS
from hebrew.gematria import GematriaTypes


def test_albam_char_values():
    values = {
        "א": 30,
        "ב": 40,
        "ג": 50,
        "ד": 60,
        "ה": 70,
        "ו": 80,
        "ז": 90,
        "ח": 100,
        "ט": 200,
        "י": 300,
        "כ": 400,
        "ך": 400,
        "ל": 1,
        "מ": 2,
        "ם": 2,
        "נ": 3,
        "ן": 3,
        "ס": 4,
        "ע": 5,
        "פ": 6,
        "ף": 6,
        "צ": 7,
        "ץ": 7,
        "ק": 8,
        "ר": 9,
        "ש": 10,
        "ת": 20,
    }
    for char in HEBREW_CHARS:
        assert char.albam == values[char.char[0]]


def test_albam_type_value():
    assert GematriaTypes.ALBAM.value == "albam"


def test_albam():
    assert Hebrew("ךָ").gematria(GematriaTypes.ALBAM) == 400
    assert Hebrew("כ").gematria(GematriaTypes.ALBAM) == 400
    assert Hebrew("אלב״ם").gematria(GematriaTypes.ALBAM) == 73
    assert Hebrew("English" + "אלב״ם").gematria(GematriaTypes.ALBAM) == 73
    assert Hebrew("אבגדהוזחטיכךלמםנןסעפףצץקרשת").gematria(GematriaTypes.ALBAM) == 1913
