from hebrew import Hebrew
from hebrew.chars import HEBREW_CHARS
from hebrew.gematria import GematriaTypes


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
            "אבגדהוזחטיכךלמםנןסעפףצץקרשת"
        ).gematria(GematriaTypes.MISPAR_GADOL)
        == 4995
    )
