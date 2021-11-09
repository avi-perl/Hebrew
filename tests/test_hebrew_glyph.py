import pytest

from hebrew import HebrewGlyph
from hebrew.hebrew_glyph import _HebrewGlyphMetadata, HebrewGlyphTypes


def test_hebrew_glyph_types():
    assert str(HebrewGlyphTypes.LETTER) == "letter"


def test_only_one_letter():
    assert isinstance(HebrewGlyph("א"), HebrewGlyph)
    with pytest.raises(ValueError):
        HebrewGlyph("אא")


def test_only_valid_glyph():
    assert isinstance(HebrewGlyph("א"), HebrewGlyph)
    with pytest.raises(ValueError):
        HebrewGlyph("a")


def test_str():
    assert str(HebrewGlyph("א")) == "א"


def test_repr():
    assert isinstance(repr(HebrewGlyph("א")), str)


def test_hebrew_names():
    metadata = _HebrewGlyphMetadata(
        glyph="פ", name="Pe", hebrew_name="פֵא", hebrew_name_alts=["פֵה"]
    )
    assert metadata.hebrew_name_alts == ["פֵה"]
    assert metadata.hebrew_name == "פֵא"
    assert metadata.hebrew_names == ["פֵא", "פֵה"]

    metadata = _HebrewGlyphMetadata(glyph="א", name="Aleph", hebrew_name="אָלֶף")
    assert metadata.hebrew_name_alts is None
    assert metadata.hebrew_name == "אָלֶף"
    assert metadata.hebrew_names == ["אָלֶף"]
