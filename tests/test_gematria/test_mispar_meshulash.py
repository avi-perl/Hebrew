from hebrew import Hebrew
from hebrew.chars import HEBREW_CHARS
from hebrew.gematria import GematriaTypes


def test_mispar_meshulash_char_values():
    values = {
        "א": 1,
        "ב": 8,
        "ג": 27,
        "ד": 64,
        "ה": 125,
        "ו": 216,
        "ז": 343,
        "ח": 512,
        "ט": 729,
        "י": 1_000,
        "כ": 8_000,
        "ך": 8_000,
        "ל": 27_000,
        "מ": 64_000,
        "ם": 64_000,
        "נ": 125_000,
        "ן": 125_000,
        "ס": 216_000,
        "ע": 343_000,
        "פ": 512_000,
        "ף": 512_000,
        "צ": 729_000,
        "ץ": 729_000,
        "ק": 1_000_000,
        "ר": 8_000_000,
        "ש": 27_000_000,
        "ת": 64_000_000,
    }
    for char in HEBREW_CHARS:
        assert char.mispar_meshulash == values[char.char[0]]


def test_mispar_meshulash_type_value():
    assert GematriaTypes.MISPAR_MESHULASH.value == "mispar_meshulash"


def test_mispar_meshulash():
    assert Hebrew("ךָ").gematria(GematriaTypes.MISPAR_MESHULASH) == 8000
    assert Hebrew("כ").gematria(GematriaTypes.MISPAR_MESHULASH) == 8000
    assert Hebrew("מספר משולש").gematria(GematriaTypes.MISPAR_MESHULASH) == 62_883_216
    assert Hebrew("English" + "מספר משולש").gematria(GematriaTypes.MISPAR_MESHULASH) == 62_883_216
    assert (
        Hebrew(
            "אבגדהוזחטיכךלמםנןסעפףצץקרשת"
        ).gematria(GematriaTypes.MISPAR_MESHULASH)
        == 103_465_025
    )
