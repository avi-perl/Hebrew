import pytest

from HebrewString import GraphemeString


@pytest.fixture
def hebrew_grapheme_string():
    return GraphemeString(
        "וְהָאָ֗רֶץ הָיְתָ֥ה תֹ֙הוּ֙ וָבֹ֔הוּ וְחֹ֖שֶׁךְ עַל־פְּנֵ֣י תְה֑וֹם וְר֣וּחַ אֱלֹהִ֔ים מְרַחֶ֖פֶת עַל־פְּנֵ֥י הַמָּֽיִם"
    )


@pytest.fixture
def hebrew_string_no_nikkud():
    return "והארץ היתה תהו ובהו וחשך על־פני תהום ורוח אלהים מרחפת על־פני המים"


def test_graphemes(hebrew_grapheme_string):
    graphemes = hebrew_grapheme_string.graphemes
    assert hasattr(graphemes, "__iter__")
    assert list(hebrew_grapheme_string.graphemes) == [
        "וְ",
        "הָ",
        "אָ֗",
        "רֶ",
        "ץ",
        " ",
        "הָ",
        "יְ",
        "תָ֥",
        "ה",
        " ",
        "תֹ֙",
        "ה",
        "וּ֙",
        " ",
        "וָ",
        "בֹ֔",
        "ה",
        "וּ",
        " ",
        "וְ",
        "חֹ֖",
        "שֶׁ",
        "ךְ",
        " ",
        "עַ",
        "ל",
        "־",
        "פְּ",
        "נֵ֣",
        "י",
        " ",
        "תְ",
        "ה֑",
        "וֹ",
        "ם",
        " ",
        "וְ",
        "ר֣",
        "וּ",
        "חַ",
        " ",
        "אֱ",
        "לֹ",
        "הִ֔",
        "י",
        "ם",
        " ",
        "מְ",
        "רַ",
        "חֶ֖",
        "פֶ",
        "ת",
        " ",
        "עַ",
        "ל",
        "־",
        "פְּ",
        "נֵ֥",
        "י",
        " ",
        "הַ",
        "מָּֽ",
        "יִ",
        "ם",
    ]


def test_length(hebrew_grapheme_string, hebrew_string_no_nikkud):
    assert hebrew_grapheme_string.length == len(hebrew_string_no_nikkud)


def test_get_length(hebrew_grapheme_string):
    assert hebrew_grapheme_string.get_length(5) == 5


def test_grapheme_lengths(hebrew_grapheme_string):
    graphemes_length = hebrew_grapheme_string.grapheme_lengths
    assert hasattr(graphemes_length, "__iter__")
    assert list(graphemes_length) == [
        2,
        2,
        3,
        2,
        1,
        1,
        2,
        2,
        3,
        1,
        1,
        3,
        1,
        3,
        1,
        2,
        3,
        1,
        2,
        1,
        2,
        3,
        3,
        2,
        1,
        2,
        1,
        1,
        3,
        3,
        1,
        1,
        2,
        2,
        2,
        1,
        1,
        2,
        2,
        2,
        2,
        1,
        2,
        2,
        3,
        1,
        1,
        1,
        2,
        2,
        3,
        2,
        1,
        1,
        2,
        1,
        1,
        3,
        3,
        1,
        1,
        2,
        4,
        2,
        1,
    ]


def test_slice(hebrew_grapheme_string):
    assert hebrew_grapheme_string.slice(start=0, end=5) == "וְהָאָ֗רֶץ"
    assert hebrew_grapheme_string.slice(start=6, end=10) == "הָיְתָ֥ה"


def test_contains(hebrew_grapheme_string):
    assert "ו" in str(hebrew_grapheme_string)  # Assert that test case is valid
    assert not hebrew_grapheme_string.contains("ו")


def test_safe_split_index(hebrew_grapheme_string):
    assert hebrew_grapheme_string.safe_split_index(12) == 11


def test_startswith(hebrew_grapheme_string):
    assert hebrew_grapheme_string.string.startswith(
        "ו"
    )  # Assert that test case is valid
    assert not hebrew_grapheme_string.startswith("ו")


def test_endswith():
    assert GraphemeString("וְ").string.endswith("ְ")  # Assert that test case is valid
    assert not GraphemeString("וְ").endswith("ְ")


def test_string_repr(hebrew_grapheme_string):
    assert isinstance(hebrew_grapheme_string.string, str)
    assert hebrew_grapheme_string.__str__() == hebrew_grapheme_string.string
    assert hebrew_grapheme_string.__repr__() == hebrew_grapheme_string.string
