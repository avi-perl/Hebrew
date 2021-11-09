from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


class HebrewGlyphTypes(Enum):
    """
    The types of glyphs used in Hebrew.
    """

    LETTER: str = "letter"
    YIDDISH_LETTER: str = "yiddish_letter"
    PUNCTUATION: str = "punctuation"
    NIKUD: str = "nikud"

    def __str__(self) -> str:
        return self.value


# TODO: Future properties:
#  - Number/order of the glyph in aleph bes if the letter is HebrewGlyphTypes.Letter.
#  - Maybe a reference to a minor/final letter when applicable.
#  - Gematria value of the letter for future use in `Hebrew` methods such as
#    `Hebrew.get_gematria_value(type=Gematria.MisparGadol)`.
#     - This is a bit tricky because the gematria value of a letter is not a single value, there are different values
#       used by different systems.
@dataclass
class _HebrewGlyphMetadata:
    """
    A class to hold the metadata for a Hebrew glyph.

    This class is used internally by HebrewGlyph only.
    """

    glyph: str
    name: str
    hebrew_name: str
    name_alts: Optional[List[str]] = None
    hebrew_name_alts: Optional[List[str]] = None
    final_letter: bool = False
    type: HebrewGlyphTypes = HebrewGlyphTypes.LETTER

    @property
    def hebrew_names(self) -> List[str]:
        return [self.hebrew_name] + (self.hebrew_name_alts or [])

    @property
    def names(self) -> List[str]:
        return [self.name] + (self.name_alts or [])


# TODO:
#  - Populate the alt hebrew and english names with additional spellings, this is helpful for the
#    `HebrewGlyph.search()` method.
#  - Add the rest of the hebrew unicode characters as seen in `hebrew_obj.Hebrew`.
_valid_hebrew_glyphs = {
    "א": _HebrewGlyphMetadata(
        glyph="א", name="Aleph", hebrew_name="אָלֶף", name_alts=["Alef"]
    ),
    "בּ": _HebrewGlyphMetadata(glyph="בּ", name="Bet", hebrew_name="בֵּית"),
    "ב": _HebrewGlyphMetadata(glyph="ב", name="Vet", hebrew_name="בֵית"),
    "ג": _HebrewGlyphMetadata(glyph="ג", name="Gimel", hebrew_name="גִימֵל"),
    "ד": _HebrewGlyphMetadata(
        glyph="ד", name="Dalet", hebrew_name="דָלֶת", name_alts=["Daled"]
    ),
    "ה": _HebrewGlyphMetadata(
        glyph="ה", name="He", hebrew_name="הֵא", name_alts=["Hei", "Hey"]
    ),
    "ו": _HebrewGlyphMetadata(
        glyph="ו", name="Vav", hebrew_name="וָו", name_alts=["Vuv"]
    ),
    "ז": _HebrewGlyphMetadata(glyph="ז", name="Zayin", hebrew_name="זַיִן"),
    "ח": _HebrewGlyphMetadata(
        glyph="ח", name="Chet", hebrew_name="חֵית", name_alts=["Het", "Ches"]
    ),
    "ט": _HebrewGlyphMetadata(
        glyph="ט", name="Tet", hebrew_name="טֵית", name_alts=["Tes"]
    ),
    "י": _HebrewGlyphMetadata(
        glyph="י", name="Yod", hebrew_name="יוֹד", name_alts=["Yud"]
    ),
    "כּ": _HebrewGlyphMetadata(glyph="כּ", name="Kaf", hebrew_name="כַּף"),
    "ךּ": _HebrewGlyphMetadata(
        glyph="ךּ",
        name="Kaf Sofit",
        final_letter=True,
        hebrew_name="כַּף סוֹפִית",
        name_alts=["Final Kaf"],
    ),
    "כ": _HebrewGlyphMetadata(glyph="כ", name="Chaf", hebrew_name="כַף"),
    "ך": _HebrewGlyphMetadata(
        glyph="ך",
        name="Chaf Sofit",
        final_letter=True,
        hebrew_name="כַף סוֹפִית",
        name_alts=["Final Chaf"],
    ),
    "ל": _HebrewGlyphMetadata(
        glyph="ל", name="Lamed", hebrew_name="לָמֶד", name_alts=["Lamid"]
    ),
    "מ": _HebrewGlyphMetadata(glyph="מ", name="Mem", hebrew_name="מֵם"),
    "ם": _HebrewGlyphMetadata(
        glyph="ם",
        name="Mem Sofit",
        final_letter=True,
        hebrew_name="מֵם סוֹפִית",
        name_alts=["Final Mem"],
    ),
    "נ": _HebrewGlyphMetadata(glyph="נ", name="Nun", hebrew_name="נוּן"),
    "ן": _HebrewGlyphMetadata(
        glyph="ן",
        name="Nun Sofit",
        final_letter=True,
        hebrew_name="נוּן סוֹפִית",
        name_alts=["Final Nun"],
    ),
    "ס": _HebrewGlyphMetadata(glyph="ס", name="Samekh", hebrew_name="סָמֶך"),
    "ע": _HebrewGlyphMetadata(glyph="ע", name="Ayin", hebrew_name="עַיִן"),
    "פּ": _HebrewGlyphMetadata(
        glyph="פ", name="Pe", hebrew_name="פֵּא", hebrew_name_alts=["פֵּה"]
    ),
    "פ": _HebrewGlyphMetadata(
        glyph="פ", name="Pe", hebrew_name="פֵא", hebrew_name_alts=["פֵה"]
    ),
    "ף": _HebrewGlyphMetadata(
        glyph="ף",
        name="Pe Sofit",
        final_letter=True,
        hebrew_name="פֵא סוֹפִית",
        hebrew_name_alts=["פֵה סוֹפִית"],
        name_alts=["Final Pe"],
    ),
    "צ": _HebrewGlyphMetadata(
        glyph="צ", name="Tsadi", hebrew_name="צַדִי", hebrew_name_alts=["צדיק"]
    ),
    "ץ": _HebrewGlyphMetadata(
        glyph="ץ",
        name="Tsadi Sofit",
        final_letter=True,
        hebrew_name="צַדִי סוֹפִית",
        hebrew_name_alts=["צדיק סופית"],
        name_alts=["Final Tsadi"],
    ),
    "ק": _HebrewGlyphMetadata(glyph="ק", name="Qof", hebrew_name="קוֹף"),
    "ר": _HebrewGlyphMetadata(glyph="ר", name="Resh", hebrew_name="רֵישׁ"),
    # TODO: The naming here might need help. We should definitely support all 3 versions as this is likely to be found
    #  in text, but the naming might be unexpected.
    "ש": _HebrewGlyphMetadata(
        glyph="ש", name="Shin", hebrew_name="שִׁין", hebrew_name_alts=["שִׂין"]
    ),
    "שׁ": _HebrewGlyphMetadata(glyph="שׁ", name="Shin", hebrew_name="שִׁין"),
    "שׂ": _HebrewGlyphMetadata(glyph="שׂ", name="Sin", hebrew_name="שִׂין"),
    "תּ": _HebrewGlyphMetadata(glyph="תּ", name="Tav", hebrew_name="תּו"),
    "ת": _HebrewGlyphMetadata(glyph="ת", name="Tav", hebrew_name="תָו"),
    "ײ": _HebrewGlyphMetadata(glyph="ײ", name="Double Yod", hebrew_name=""),
    "װ": _HebrewGlyphMetadata(glyph="ײ", name="Double Vav", hebrew_name=""),
    "ױ": _HebrewGlyphMetadata(glyph="ײ", name="Vav Yod", hebrew_name=""),
}


class HebrewGlyph(str):
    """
    A class representing a Hebrew character.

    A HebrewGlyph represents a single *user-perceived* character that is part of the Hebrew alphabet such as a letter,
    a letter with nikud, a punctuation, or a nikud. This is done to support letters such as
    "Bet" and "Vet" who share a single unicode letter but differ in their nikud. However, arbitrary hebrew strings are
    not allowed, you may only initiate a HebrewGlyph that matches a pre specified set of Glyphs found in HebrewGlyphs.
    (For arbitrary hebrew strings, see `hebrew_obj.Hebrew`.)
    """

    def __init__(self, letter: str):

        # TODO BUG: A letter may now have > 1 unicode char. \
        #  Fix and add tests.
        if len(letter) > 1:
            raise ValueError(f"{letter} is not a single letter")
        if letter not in _valid_hebrew_glyphs:
            raise ValueError(f"{letter} is not a Hebrew glyph")

        self.letter = letter
        self.metadata = _valid_hebrew_glyphs[letter]
        self.type = self.metadata.type
        self.final_letter = self.metadata.final_letter
        self.name = self.metadata.name
        self.names = self.metadata.names
        self.name_alts = self.metadata.name_alts
        self.hebrew_name = self.metadata.hebrew_name
        self.names = self.metadata.hebrew_names
        self.name_alts = self.metadata.hebrew_name_alts

    # TODO: if a string like "HebrewGlyph" is the better way to Type this than the way I did HebrewStringT, update that
    #  Typing, or Type it here.
    @classmethod
    def search(cls, glyph_name: str) -> Optional["HebrewGlyph"]:
        """
        Search for a HebrewGlyph by one of its names.
        :param glyph_name:
        :return:
        """
        # TODO : Add search by hebrew_name, which will need to support hebrew text with or without nikud.
        for glyph_metadata in _valid_hebrew_glyphs.values():
            if glyph_name.lower() in [n.lower() for n in glyph_metadata.names]:
                return cls(glyph_metadata.glyph)
        return None

