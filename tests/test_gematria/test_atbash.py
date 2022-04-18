from hebrew import Hebrew
from hebrew.chars import HEBREW_CHARS
from hebrew.gematria import GematriaTypes


def test_atbash_char_values():
    values = {
        "א": 400,
        "ב": 300,
        "ג": 200,
        "ד": 100,
        "ה": 90,
        "ו": 80,
        "ז": 70,
        "ח": 60,
        "ט": 50,
        "י": 40,
        "כ": 30,
        "ך": 30,
        "ל": 20,
        "מ": 10,
        "ם": 10,
        "נ": 9,
        "ן": 9,
        "ס": 8,
        "ע": 7,
        "פ": 6,
        "ף": 6,
        "צ": 5,
        "ץ": 5,
        "ק": 4,
        "ר": 3,
        "ש": 2,
        "ת": 1,
    }
    for char in HEBREW_CHARS:
        assert char.atbash == values[char.char[0]]


def test_atbash_type_value():
    assert GematriaTypes.ATBASH.value == "atbash"


def test_atbash():
    assert Hebrew("ךָ").gematria(GematriaTypes.ATBASH) == 30
    assert Hebrew("כ").gematria(GematriaTypes.ATBASH) == 30
    assert Hebrew("אתב״ש").gematria(GematriaTypes.ATBASH) == 703
    assert Hebrew("English" + "אתב״ש").gematria(GematriaTypes.ATBASH) == 703
    assert (
        Hebrew(
            "אבגדהוזחטיכךלמםנןסעפףצץקרשת"
        ).gematria(GematriaTypes.ATBASH)
        == 1555
    )
