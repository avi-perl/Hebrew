from hebrew import Hebrew
from hebrew.chars import HEBREW_CHARS
from hebrew.gematria import GematriaTypes


def test_mispar_siduri_char_values():
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
        "כ": 11,
        "ך": 23,
        "ל": 12,
        "מ": 13,
        "ם": 24,
        "נ": 14,
        "ן": 25,
        "ס": 15,
        "ע": 16,
        "פ": 17,
        "ף": 26,
        "צ": 18,
        "ץ": 27,
        "ק": 19,
        "ר": 20,
        "ש": 21,
        "ת": 22,
    }
    for char in HEBREW_CHARS:
        assert char.mispar_siduri == values[char.char[0]]


def test_mispar_siduri_type_value():
    assert GematriaTypes.MISPAR_SIDURI.value == "mispar_siduri"


def test_mispar_siduri():
    assert Hebrew("ךָ").gematria(GematriaTypes.MISPAR_SIDURI) == 23
    assert Hebrew("כ").gematria(GematriaTypes.MISPAR_SIDURI) == 11
    assert Hebrew("מספר סידורי").gematria(GematriaTypes.MISPAR_SIDURI) == 130
    assert (
        Hebrew("English" + "מספר סידורי").gematria(GematriaTypes.MISPAR_SIDURI) == 130
    )
    assert (
        Hebrew(
            "וְאֵ֗לֶּה שְׁמוֹת֙ בְּנֵ֣י יִשְׂרָאֵ֔ל הַבָּאִ֖ים מִצְרָ֑יְמָה אֵ֣ת יַעֲקֹ֔ב אִ֥ישׁ וּבֵית֖וֹ בָּֽאוּ׃"
        ).gematria(GematriaTypes.MISPAR_SIDURI)
        == 454
    )