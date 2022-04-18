import pytest

from hebrew import Hebrew
from hebrew.gematria import GematriaTypes

# Test inputs and their expected values for each method type.
# Add new test cases here!
test_values = {
    "אבגדהוזחטיכךלמםנןסעפףצץקרשת": {
        GematriaTypes.ALBAM: 1913,
        GematriaTypes.ATBASH: 1555,
        GematriaTypes.MISPAR_GADOL: 4995,
        GematriaTypes.MISPAR_HECHRACHI: 1775,
        GematriaTypes.MISPAR_KATAN: 128,
        GematriaTypes.MISPAR_MESHULASH: 103_465_025,
        GematriaTypes.MISPAR_MUSAFI: 1802,
        GematriaTypes.MISPAR_PERATI: 347_785,
        GematriaTypes.MISPAR_SIDURI: 378,
        GematriaTypes.MISPAR_BONEEH: 9915,
        GematriaTypes.MISPAR_HAMERUBAH_HAKLALI: 3_150_625,
        GematriaTypes.MISPAR_HAACHOR: 39_785,
        GematriaTypes.MISPAR_KATAN_MISPARI: 2,
        GematriaTypes.MISPAR_KOLEL: 1776,
        GematriaTypes.MISPAR_KIDMI: 7515,
        GematriaTypes.MISPAR_NEELAM: 2925,
        GematriaTypes.MISPAR_MISPARI: 14_095,
        GematriaTypes.AYAK_BACHAR: 4995,
        GematriaTypes.AYAK_BAKAR: 4995,
        GematriaTypes.OFANIM: 2643,
        GematriaTypes.ACHAS_BETA: 2092,
        GematriaTypes.AVGAD: 1825,
        GematriaTypes.REVERSE_AVGAD: 1725,
        GematriaTypes.MISPAR_SHEMI_MILUI: 4700,
    },
    "בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃": {
        GematriaTypes.ALBAM: 1571,
        GematriaTypes.ATBASH: 3541,
        GematriaTypes.MISPAR_GADOL: 4631,
        GematriaTypes.MISPAR_HECHRACHI: 2701,
        GematriaTypes.MISPAR_KATAN: 82,
        GematriaTypes.MISPAR_MESHULASH: 270_951_613,
        GematriaTypes.MISPAR_MUSAFI: 2729,
        GematriaTypes.MISPAR_PERATI: 794_225,
        GematriaTypes.MISPAR_SIDURI: 329,
        GematriaTypes.MISPAR_BONEEH: 40_035,
        GematriaTypes.MISPAR_HAMERUBAH_HAKLALI: 7_295_401,
        GematriaTypes.MISPAR_HAACHOR: 38_294,
        GematriaTypes.MISPAR_KATAN_MISPARI: 1,
        GematriaTypes.MISPAR_KOLEL: 2708,
        GematriaTypes.MISPAR_KIDMI: 10_338,
        GematriaTypes.MISPAR_NEELAM: 2745,
        GematriaTypes.MISPAR_MISPARI: 13_256,
        GematriaTypes.AYAK_BACHAR: 1355,
        GematriaTypes.AYAK_BAKAR: 1355,
        GematriaTypes.OFANIM: 2453,
        GematriaTypes.ACHAS_BETA: 2372,
        GematriaTypes.AVGAD: 2096,
        GematriaTypes.REVERSE_AVGAD: 4236,
        GematriaTypes.MISPAR_SHEMI_MILUI: 5446,
    },
}

# Prepare the test inputs for the pytest parametrize function
params = ["hebrew_text,gematria_method,expected_val", []]
for text, tests in test_values.items():
    for method, val in tests.items():
        params[1].append((text, method, val))


@pytest.mark.parametrize(*params)
def test_gematria_values(
    hebrew_text: str, gematria_method: GematriaTypes, expected_val: str
):
    assert Hebrew(hebrew_text).gematria(gematria_method) == expected_val
    assert Hebrew(hebrew_text).text_only().gematria(gematria_method) == expected_val
    assert (
        Hebrew(hebrew_text + " Add english letters").gematria(gematria_method)
        == expected_val
    )


def test_mispar_shemi_milui_change_spelling():
    hebrew_text = "בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃"
    spellings = {
        "ב": "בת",
        "ג": "גמל",
        "ד": "דלית",
        "ה": "הי",
        "ו": "ויו",
        "ח": "חת",
        "ט": "טת",
        "פ": "פי",
        "צ": "צדיק",
        "ר": "רש",
        "ש": "שין",
        "ת": "תיו",
    }
    assert (
        Hebrew(hebrew_text).gematria(
            GematriaTypes.MISPAR_SHEMI_MILUI, alt_letter_name_spelling=spellings
        )
        == 5583
    )
    assert (
        Hebrew(hebrew_text)
        .text_only()
        .gematria(GematriaTypes.MISPAR_SHEMI_MILUI, alt_letter_name_spelling=spellings)
        == 5583
    )
    assert (
        Hebrew(hebrew_text + " Add english letters").gematria(
            GematriaTypes.MISPAR_SHEMI_MILUI, alt_letter_name_spelling=spellings
        )
        == 5583
    )
    hebrew_text = "אבגדהוזחטיכךלמםנןסעפףצץקרשת"
    spellings = {
        "ה": "הה",
        "ו": "ואו",
        "פ": "פה",
        "ת": "תאו",
    }
    assert (
        Hebrew(hebrew_text).gematria(
            GematriaTypes.MISPAR_SHEMI_MILUI, alt_letter_name_spelling=spellings
        )
        == 4714
    )
    assert (
        Hebrew(hebrew_text)
        .text_only()
        .gematria(GematriaTypes.MISPAR_SHEMI_MILUI, alt_letter_name_spelling=spellings)
        == 4714
    )
    assert (
        Hebrew(hebrew_text + " Add english letters").gematria(
            GematriaTypes.MISPAR_SHEMI_MILUI, alt_letter_name_spelling=spellings
        )
        == 4714
    )


def test_mispar_shemi_milui_bad_spelling():
    hebrew_text = "בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃"
    spellings = {
        "ב": "בתבתבתבת",  # bad name that does not exist for this letter
    }
    with pytest.raises(ValueError):
        Hebrew(hebrew_text).gematria(
            GematriaTypes.MISPAR_SHEMI_MILUI, alt_letter_name_spelling=spellings
        )


def test_mispar_neelam_change_spelling():
    hebrew_text = "בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃"
    spellings = {
        "ב": "בת",
        "ג": "גמל",
        "ד": "דלית",
        "ה": "הי",
        "ו": "ויו",
        "ח": "חת",
        "ט": "טת",
        "פ": "פי",
        "צ": "צדיק",
        "ר": "רש",
        "ש": "שין",
        "ת": "תיו",
    }
    assert (
        Hebrew(hebrew_text).gematria(
            GematriaTypes.MISPAR_NEELAM, alt_letter_name_spelling=spellings
        )
        == 2882
    )
    assert (
        Hebrew(hebrew_text)
        .text_only()
        .gematria(GematriaTypes.MISPAR_NEELAM, alt_letter_name_spelling=spellings)
        == 2882
    )
    assert (
        Hebrew(hebrew_text + " Add english letters").gematria(
            GematriaTypes.MISPAR_NEELAM, alt_letter_name_spelling=spellings
        )
        == 2882
    )
    hebrew_text = "אבגדהוזחטיכךלמםנןסעפףצץקרשת"
    spellings = {
        "ה": "הה",
        "ו": "ואו",
        "פ": "פה",
        "ת": "תאו",
    }
    assert (
        Hebrew(hebrew_text).gematria(
            GematriaTypes.MISPAR_NEELAM, alt_letter_name_spelling=spellings
        )
        == 2939
    )
    assert (
        Hebrew(hebrew_text)
        .text_only()
        .gematria(GematriaTypes.MISPAR_NEELAM, alt_letter_name_spelling=spellings)
        == 2939
    )
    assert (
        Hebrew(hebrew_text + " Add english letters").gematria(
            GematriaTypes.MISPAR_NEELAM, alt_letter_name_spelling=spellings
        )
        == 2939
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
