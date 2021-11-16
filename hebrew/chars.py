"""
Constants for each Hebrew character and classes to represent them, and metadata about them.
"""

from dataclasses import dataclass
from typing import Optional, List, Dict, Union

from hebrew.gematria import MISPAR_HECHRACHI


# TODO: Future properties:
#  - Number/order of the char in aleph bes if the letter is HebrewCharTypes.Letter.
#  - Maybe a reference to a minor/final letter when applicable.
#  - Gematria value of the letter for future use in `Hebrew` methods such as
#    `Hebrew.get_gematria_value(type=Gematria.MisparGadol)`.
#     - This is a bit tricky because the gematria value of a letter is not a single value, there are different values
#       used by different systems.
@dataclass
class BaseHebrewChar:
    """
    Base class with the metadata that all Hebrew characters share.
    This class should be used internally by `hebrew.Chars` only.
    """

    char: str
    """Unicode character(s) for this class instance."""

    name: str
    """Primary name of the character in English."""

    hebrew_name: Optional[str] = None
    """Primary name of the character in Hebrew."""

    name_alts: Optional[List[str]] = None
    """Alternative names of the character in English."""

    hebrew_name_alts: Optional[List[str]] = None
    """Alternative names of the character in Hebrew."""

    @property
    def hebrew_names(self) -> List[str]:
        """
        All Hebrew names for this character.
        :return: A list of all Hebrew names for this character made up of the `hebrew_name` and `hebrew_name_alts`.
        """
        return [self.hebrew_name] + (self.hebrew_name_alts or [])

    @property
    def names(self) -> List[str]:
        """
        All english names for this character.
        :return: A list of all english names for this character made up of the `name` and `name_alts`.
        """
        return [self.name] + (self.name_alts or [])

    def __str__(self):
        return self.char


@dataclass
class HebrewChar(BaseHebrewChar):
    """
    A class representing characters that are part of the Hebrew alphabet (to the exclusion of Nekuds, etc).
    """

    final_letter: bool = False
    """Whether or not the letter is a "final" or "Sofit" letter."""

    @property
    def base_letter(self) -> "HebrewChar":
        """
        Returns the base letter of the character.

        This library provides HebrewChar values for both standard Hebrew letters and user-perceived letters such as "בּ".
        This property will always return the base letter of the HebrewChar instance, in the above example, "ב".

        :return: An instance of `HebrewChar` representing a single unicode character; the base letter of
         this instance of `HebrewChar`.
        """
        return CHARS[self.char[0]]

    @property
    def mispar_hechrachi(self) -> int:
        """
        :return: The value of the character for use in the mispar_hechrachi method of gematria.
        """
        return MISPAR_HECHRACHI.get(self.base_letter.char)

    @classmethod
    def search(cls, char_name: str) -> Optional["HebrewChar"]:
        """
        Searches for an instance of `HebrewChar` by name.
        The search input is case insensitive and is compared to `names` list for this search.

        To search for any Hebrew character, use `hebrew.chars.char_search`.

        :param char_name: A single string representing the name of the character to search for.
        :return: An instance of `HebrewChar` representing the character with the given name, or `None` if no
        character is found.
        """
        return char_search(char_name, HEBREW_CHARS)


@dataclass
class YiddishChar(BaseHebrewChar):
    """
    A class representing special characters used in Yiddish text.
    """

    @classmethod
    def search(cls, char_name: str) -> Optional["YiddishChar"]:
        """
        Searches for an instance of `YiddishChar` by name.
        The search input is case insensitive and is compared to `names` list for this search.

        To search for any Hebrew character, use `hebrew.chars.char_search`.

        :param char_name: A single string representing the name of the character to search for.
        :return: An instance of `YiddishChar` representing the character with the given name, or `None` if no
        character is found.
        """
        return char_search(char_name, YIDDISH_CHARS)


@dataclass
class NiqqudChar(BaseHebrewChar):
    """
    A class representing Niqqud characters used in Hebrew and Yiddish text.
    """

    @classmethod
    def search(cls, char_name: str) -> Optional["NiqqudChar"]:
        """
        Searches for an instance of `NiqqudChar` by name.
        The search input is case insensitive and is compared to `names` list for this search.

        To search for any Hebrew character, use `hebrew.chars.char_search`.

        :param char_name: A single string representing the name of the character to search for.
        :return: An instance of `NiqqudChar` representing the character with the given name, or `None` if no
        character is found.
        """
        return char_search(char_name, NIQQUD_CHARS)


@dataclass
class TaamimChar(BaseHebrewChar):
    """
    A class representing the "Trup" or [Hebrew cantillation](https://en.wikipedia.org/wiki/Hebrew_cantillation) 
    characters used alongside Hebrew letters.
    """

    @classmethod
    def search(cls, char_name: str) -> Optional["TaamimChar"]:
        """
        Searches for an instance of `TaamimChar` by name.
        The search input is case insensitive and is compared to `names` list for this search.

        To search for any Hebrew character, use `hebrew.chars.char_search`.

        :param char_name: A single string representing the name of the character to search for.
        :return: An instance of `TaamimChar` representing the character with the given name, or `None` if no
        character is found.
        """
        return char_search(char_name, TAAMIM_CHARS)


@dataclass
class OtherChar(BaseHebrewChar):
    """
    A class representing the "other" or "uncharacterized" characters used in Hebrew (and Yiddish) text.
    """

    @classmethod
    def search(cls, char_name: str) -> Optional["OtherChar"]:
        """
        Searches for an instance of `TaamimChar` by name.
        The search input is case insensitive and is compared to `names` list for this search.

        To search for any Hebrew character, use `hebrew.chars.char_search`.

        :param char_name: A single string representing the name of the character to search for.
        :return: An instance of `OtherChar` representing the character with the given name, or `None` if no
        character is found.
        """
        return char_search(char_name, OTHER_CHARS)


# TODO:
#  - Populate the alt hebrew and english names with additional spellings, this is helpful for the
#    `HebrewGlyph.search()` method.
#  - Add the rest of the hebrew unicode characters as `HebrewChar` instances instead of plain strings`


ALEPH = HebrewChar(char="א", name="Aleph", hebrew_name="אָלֶף", name_alts=["Alef"])
"""An instance of `HebrewChar` representing the letter `'א'`"""

BET = HebrewChar(char="בּ", name="Bet", hebrew_name="בֵּית")
"""
An instance of `HebrewChar` representing the letter **`'בּ'`**. 
*This is not strictly a letter, but is included because it is often treated as one.*
"""

BES = BET
"""Simple pointer to `BET`."""

VET = HebrewChar(char="ב", name="Vet", hebrew_name="בֵית")
"""An instance of `HebrewChar` representing the letter **`'ב'`**."""

GIMEL = HebrewChar(char="ג", name="Gimel", hebrew_name="גִימֵל")
"""An instance of `HebrewChar` representing the letter **`'ג'`**."""

DALET = HebrewChar(char="ד", name="Dalet", hebrew_name="דָלֶת", name_alts=["Daled"])
"""An instance of `HebrewChar` representing the letter **`'ד'`**."""

DALED = DALET
"""Simple pointer to `DALET`."""

HE = HebrewChar(char="ה", name="He", hebrew_name="הֵא", name_alts=["Hei", "Hey"])
"""An instance of `HebrewChar` representing the letter **`'ה'`**."""

HEI = HEY = HE
"""Simple pointer to `HE`."""

VAV = HebrewChar(char="ו", name="Vav", hebrew_name="וָו", name_alts=["Vuv"])
"""An instance of `HebrewChar` representing the letter **`'ו'`**."""

VUV = VAV
"""Simple pointer to `VAV`."""

ZAYIN = HebrewChar(char="ז", name="Zayin", hebrew_name="זַיִן")
"""An instance of `HebrewChar` representing the letter **`'ז'`**."""

CHET = HebrewChar(
    char="ח",
    name="Chet",
    hebrew_name="חֵית",
    name_alts=["Het", "Ches"],
)
"""An instance of `HebrewChar` representing the letter **`'ז'`**."""

HET = CHES = CHET
"""Simple pointer to `CHET`."""

TET = HebrewChar(char="ט", name="Tet", hebrew_name="טֵית", name_alts=["Tes"])
"""An instance of `HebrewChar` representing the letter **`'ט'`**."""

TES = TET
"""Simple pointer to `TET`."""

YOD = HebrewChar(char="י", name="Yod", hebrew_name="יוֹד", name_alts=["Yud"])
"""An instance of `HebrewChar` representing the letter **`'י'`**."""

YUD = YOD
"""Simple pointer to `YOD`."""

CAF = HebrewChar(char="כּ", name="Kaf", hebrew_name="כַּף")
"""
An instance of `HebrewChar` representing the letter **`'כּ'`**. 
*This is not strictly a letter, but is included because it is often treated as one.*
"""

KAF_SOFIT = HebrewChar(
    char="ךּ",
    name="Kaf Sofit",
    final_letter=True,
    hebrew_name="כַּף סוֹפִית",
    name_alts=["Final Kaf"],
)
"""
An instance of `HebrewChar` representing the letter **`'ךּ'`**. 
*This is not strictly a letter, but is included because it is often treated as one.*
"""

FINAL_KAF = KAF_SOFIT
"""Simple pointer to `KAF_SOFIT`."""

CHAF = HebrewChar(char="כ", name="Chaf", hebrew_name="כַף")
"""An instance of `HebrewChar` representing the letter **`'כ'`**."""

CHAF_SOFIT = HebrewChar(
    char="ך",
    name="Chaf Sofit",
    final_letter=True,
    hebrew_name="כַף סוֹפִית",
    name_alts=["Final Chaf"],
)
"""An instance of `HebrewChar` representing the letter **`'ך'`**."""

FINAL_CHAF = CHAF_SOFIT
"""Simple pointer to `CHAF_SOFIT`."""

LAMED = HebrewChar(
    char="ל",
    name="Lamed",
    hebrew_name="לָמֶד",
    name_alts=["Lamid"],
)
"""An instance of `HebrewChar` representing the letter **`'ל'`**."""

LAMID = LAMED
"""Simple pointer to `LAMED`."""

MEM = HebrewChar(char="מ", name="Mem", hebrew_name="מֵם")
"""An instance of `HebrewChar` representing the letter **`'מ'`**."""

MEM_SOFIT = HebrewChar(
    char="ם",
    name="Mem Sofit",
    final_letter=True,
    hebrew_name="מֵם סוֹפִית",
    name_alts=["Final Mem"],
)
"""An instance of `HebrewChar` representing the letter **`'ם'`**."""

FINAL_MEM = MEM_SOFIT
"""Simple pointer to `MEM_SOFIT`."""

NUN = HebrewChar(char="נ", name="Nun", hebrew_name="נוּן")
"""An instance of `HebrewChar` representing the letter **`'נ'`**."""

NUN_SOFIT = HebrewChar(
    char="ן",
    name="Nun Sofit",
    final_letter=True,
    hebrew_name="נוּן סוֹפִית",
    name_alts=["Final Nun"],
)
"""An instance of `HebrewChar` representing the letter **`'ן'`**."""

FINAL_NUN = NUN_SOFIT
"""Simple pointer to `NUN_SOFIT`."""


SAMEKH = HebrewChar(
    char="ס",
    name="Samekh",
    hebrew_name="סָמֶך",
    name_alts=["Samach"],
)
"""An instance of `HebrewChar` representing the letter **`'ס'`**."""

SAMACH = SAMEKH
"""Simple pointer to `SAMEKH`."""

AYIN = HebrewChar(char="ע", name="Ayin", hebrew_name="עַיִן")
"""An instance of `HebrewChar` representing the letter **`'ע'`**."""

PE = HebrewChar(char="פּ", name="Pe")
"""
An instance of `HebrewChar` representing the letter **`'פּ'`**. 
*This is not strictly a letter, but is included because it is often treated as one.*
"""

FE = HebrewChar(char="פ", name="Fe", hebrew_name="פֵא")
"""An instance of `HebrewChar` representing the letter **`'פ'`**."""

PE_SOFIT = HebrewChar(
    char="ףּ",
    name="Fe Sofit",
    final_letter=True,
    hebrew_name="פֵּא סוֹפִית",
    name_alts=["Final Pe"],
)
"""
An instance of `HebrewChar` representing the letter **`'ףּ'`**. 
*This is not strictly a letter, but is included because it is often treated as one.*
"""

FINAL_PE = PE_SOFIT
"""Simple pointer to `PE_SOFIT`."""

FE_SOFIT = HebrewChar(
    char="ף",
    name="Fe Sofit",
    final_letter=True,
    hebrew_name="פֵא סוֹפִית",
    name_alts=["Final Fe"],
)
"""An instance of `HebrewChar` representing the letter **`'ף'`**."""

FINAL_FE = FE_SOFIT
"""Simple pointer to `FE_SOFIT`."""

TSADI = HebrewChar(
    char="צ",
    name="Tsadi",
    hebrew_name="צַדִי",
    hebrew_name_alts=["צדיק"],
    name_alts=["Tzadik"],
)
"""An instance of `HebrewChar` representing the letter **`'צ'`**."""

TZADIK = TSADI
"""Simple pointer to `TSADI`."""

TSADI_SOFIT = HebrewChar(
    char="ץ",
    name="Tsadi Sofit",
    final_letter=True,
    hebrew_name="צַדִי סוֹפִית",
    hebrew_name_alts=["צדיק סופית"],
)
"""An instance of `HebrewChar` representing the letter **`'ץ'`**."""

FINAL_TSADI = TZADIK_SOFIT = FINAL_TZADIK = TSADI_SOFIT
"""Simple pointer to `TSADI_SOFIT`."""

QOF = HebrewChar(char="ק", name="Qof", hebrew_name="קוֹף", name_alts=["Kuf"])
"""An instance of `HebrewChar` representing the letter **`'ק'`**."""

KUF = QOF
"""Simple pointer to `TSADI_SOFIT`."""

RESH = HebrewChar(char="ר", name="Resh", hebrew_name="רֵישׁ")
"""An instance of `HebrewChar` representing the letter **`'ר'`**."""

# TODO: The naming here might need help. We should definitely support all 3 versions as this is likely to be found
#  in text, but the naming might be unexpected.
SHIN = HebrewChar(char="שׁ", name="Shin", hebrew_name="שִׁין")
"""
An instance of `HebrewChar` representing the letter **`'שׁ'`**. 
*This is not strictly a letter, but is included because it is often treated as one.*
"""

SIN = HebrewChar(char="שׂ", name="Sin", hebrew_name="שִׂין")
"""
An instance of `HebrewChar` representing the letter **`'שׂ'`**. 
*This is not strictly a letter, but is included because it is often treated as one.*
"""

PLAIN_SIN = HebrewChar(
    char="ש", name="Plain Sin", hebrew_name="שִׁין", hebrew_name_alts=["שִׂין"]
)
"""An instance of `HebrewChar` representing the letter **`'ש'`**."""

TAV = HebrewChar(char="תּ", name="Tav", hebrew_name="תּו", name_alts=["Taf"])
"""
An instance of `HebrewChar` representing the letter **`'תּ'`**. 
*This is not strictly a letter, but is included because it is often treated as one.*
"""

TAF = TAV
"""Simple pointer to `TAV`."""

SAV = HebrewChar(char="ת", name="Sav", hebrew_name="תָו", name_alts=["Saf"])
"""An instance of `HebrewChar` representing the letter **`'ת'`**."""

SAF = SAV
"""Simple pointer to `SAV`."""

DOUBLE_YOD = YiddishChar(
    char="ײ",
    name="Double Yod",
    name_alts=["Saf"],
)
"""An instance of `YiddishChar` representing the letter **`'ײ'`**."""

DOUBLE_YUD = DOUBLE_YOD
"""Simple pointer to `DOUBLE_YOD`."""

DOUBLE_VAV = YiddishChar(
    char="װ",
    name="Double Vav",
    name_alts=["Double Vuv"],
)
"""An instance of `YiddishChar` representing the letter **`'װ'`**."""

DOUBLE_VUV = DOUBLE_VAV
"""Simple pointer to `DOUBLE_VAV`."""

VAV_YOD = YiddishChar(char="ױ", name="Vav Yod")
"""An instance of `YiddishChar` representing the letter **`'ױ'`**."""

VAV_YUD = VUV_YOD = VUV_YUD = VAV_YOD
"""Simple pointer to `VAV_YOD`."""

# Niqqudot or Vowel characters
SIN_DOT = NiqqudChar(char="ׂ", name="Sin Dot")
"""An instance of `NiqqudChar` representing the Niqqud **`'ׂ'`**."""
SHIN_DOT = NiqqudChar(char="ׁ", name="Shin Dot")
"""An instance of `NiqqudChar` representing the Niqqud **`'ׁ'`**."""
DAGESH = NiqqudChar(char="ּ", name="Dagesh")
"""An instance of `NiqqudChar` representing the Niqqud **`'ּ'`**."""
QUBUTS = NiqqudChar(char="ֻ", name="Qubuts", name_alts=["Kubutz"])
"""An instance of `NiqqudChar` representing the Niqqud **`'ֻ'`**."""
KUBUTZ = QUBUTS
"""Simple pointer to `QUBUTS`"""
SHURUK = NiqqudChar(char="וּ", name="Shuruk")
"""An instance of `NiqqudChar` representing the Niqqud **`'וּ'`**."""
HOLAM = NiqqudChar(char="ֹ", name="Holam")
"""An instance of `NiqqudChar` representing the Niqqud **`'ֹ'`**."""
QAMATS = NiqqudChar(char="ָ", name="Qamats", name_alts=["Kumatz"])
"""An instance of `NiqqudChar` representing the Niqqud **`'ָ'`**."""
KUMATZ = QAMATS
"""Simple pointer to `QAMATS`"""
PATAH = NiqqudChar(char="ַ", name="Patah", name_alts=["Patach"])
"""An instance of `NiqqudChar` representing the Niqqud **`'ַ'`**."""
PATACH = PATAH
"""Simple pointer to `PATAH`"""
SEGOL = NiqqudChar(char="ֶ", name="Segol")
"""An instance of `NiqqudChar` representing the Niqqud **`'ֶ'`**."""
TSERE = NiqqudChar(char="ֵ", name="Tsere")
"""An instance of `NiqqudChar` representing the Niqqud **`'ֵ'`**."""
HIRIQ = NiqqudChar(char="ִ", name="Hiriq", name_alts=["Chirik"])
"""An instance of `NiqqudChar` representing the Niqqud **`'ִ'`**."""
CHIRIK = HIRIQ
"""Simple pointer to `HIRIQ`"""
HATAF_QAMATS = NiqqudChar(char="ֳ", name="Hataf Qamatz", name_alts=["Hataf Kumatz"])
"""An instance of `NiqqudChar` representing the Niqqud **`'ֳ'`**."""
HATAF_PATAH = NiqqudChar(char="ֲ", name="Hataf Patah", name_alts=["Hataf Patach"])
"""An instance of `NiqqudChar` representing the Niqqud **`'ֲ'`**."""
HATAF_SEGOL = NiqqudChar(char="ֱ", name="Hataf Segol")
"""An instance of `NiqqudChar` representing the Niqqud **`'ֱ'`**."""
SHEVA = NiqqudChar(char="ְ", name="Sheva", name_alts=["Shivah"])
"""An instance of `NiqqudChar` representing the Niqqud **`'ְ'`**."""
SHIVAH = SHEVA
"""Simple pointer to `SHEVA`"""
UPPER_DOT = NiqqudChar(char="ׄ", name="Upper Dot")
"""An instance of `NiqqudChar` representing the Niqqud **`'ׄ'`**."""

# Other characters
MAQAF = OtherChar(char="־", name="Maqaf")
"""An instance of `TaamimChar` representing the character **`'־'`**."""
PASEQ = OtherChar(char="׀", name="Paseq")
"""An instance of `TaamimChar` representing the character **`'׀'`**."""
SOF_PASSUK = OtherChar(char="׃", name="Sof Passuk")
"""An instance of `TaamimChar` representing the character **`'׃'`**."""
GERSHAYIM = OtherChar(char="״", name="Gershayim")
"""An instance of `OtherChar` representing the character **`'״'`**."""
GERESH = OtherChar(char="׳", name="Geresh")
"""An instance of `OtherChar` representing the character **`'׳'`**."""

# Taamim characters
ETNAHTA = TaamimChar(char="֑", name="Etnahta")
"""An instance of `TaamimChar` representing the Ta'amim **`'֑'`**."""
SEGOL_TOP = TaamimChar(char="֒", name="Segol Top")
"""An instance of `TaamimChar` representing the Ta'amim **`'֒'`**."""
SHALSHELET = TaamimChar(char="֓", name="Shalshelet")
"""An instance of `TaamimChar` representing the Ta'amim **`'֓'`**."""
ZAQEF_QATAN = TaamimChar(char="֔", name="Zaqef Qatan")
"""An instance of `TaamimChar` representing the Ta'amim **`'֔'`**."""
ZAQEF_GADOL = TaamimChar(char="֕", name="Zaqef Gadol")
"""An instance of `TaamimChar` representing the Ta'amim **`'֕'`**."""
TIFCHA = TaamimChar(char="֖", name="Tifcha")
"""An instance of `TaamimChar` representing the Ta'amim **`'֖'`**."""
REVIA = TaamimChar(char="֗", name="Revia")
"""An instance of `TaamimChar` representing the Ta'amim **`'֗'`**."""
ZINOR = TaamimChar(char="֮", name="Zinor")
"""An instance of `TaamimChar` representing the Ta'amim **`'֮'`**."""
PASHTA = TaamimChar(char="֙", name="Pashta")
"""An instance of `TaamimChar` representing the Ta'amim **`'֙'`**."""
PASHTA_2 = TaamimChar(char="֨", name="Pashta 2", name_alts=["Qadma"])
"""An instance of `TaamimChar` representing the Ta'amim **`'֨'`**."""
QADMA = PASHTA_2
"""Simple pointer to `PASHTA_2` since they share the same Unicode character."""
YETIV = TaamimChar(char="֚", name="Yetiv")
"""An instance of `TaamimChar` representing the Ta'amim **`'֚'`**."""
TEVIR = TaamimChar(char="֛", name="Tevir")
"""An instance of `TaamimChar` representing the Ta'amim **`'֛'`**."""
PAZER = TaamimChar(char="֡", name="Pazer")
"""An instance of `TaamimChar` representing the Ta'amim **`'֡'`**."""
TELISHA_GEDOLA = TaamimChar(char="֠", name="Telisha Gedola")
"""An instance of `TaamimChar` representing the Ta'amim **`'֠'`**."""
TELISHA_KETANNAH = TaamimChar(char="֩", name="Telisha Ketannah")
"""An instance of `TaamimChar` representing the Ta'amim **`'֩'`**."""
AZLA_GERESH = TaamimChar(char="֜", name="Azla Geresh")
"""An instance of `TaamimChar` representing the Ta'amim **`'֜'`**."""
GERSHAYIM_2 = TaamimChar(char="֞", name="Gershayim 2")
"""An instance of `TaamimChar` representing the Ta'amim **`'֞'`**."""
MERCHA = TaamimChar(char="֥", name="Mercha")
"""An instance of `TaamimChar` representing the Ta'amim **`'֥'`**."""
MUNACH = TaamimChar(char="֣", name="Munach")
"""An instance of `TaamimChar` representing the Ta'amim **`'֣'`**."""
MAHPACH = TaamimChar(char="֤", name="Mahpach")
"""An instance of `TaamimChar` representing the Ta'amim **`'֤'`**."""
DARGA = TaamimChar(char="֧", name="Darga")
"""An instance of `TaamimChar` representing the Ta'amim **`'֧'`**."""
MERCHA_KEFULA = TaamimChar(char="֦", name="Mercha Kefula")
"""An instance of `TaamimChar` representing the Ta'amim **`'֦'`**."""
YERACH_BEN_YOMO = TaamimChar(char="֪", name="Yerach Ben Yomo")
"""An instance of `TaamimChar` representing the Ta'amim **`'֪'`**."""
MASORA = TaamimChar(char="֯", name="Masora")
"""An instance of `TaamimChar` representing the Ta'amim **`'֯'`**."""
DEHI = TaamimChar(char="֭", name="Dehi")
"""An instance of `TaamimChar` representing the Ta'amim **`'֭'`**."""
ZARQA = TaamimChar(char="֘", name="Zarqa")
"""An instance of `TaamimChar` representing the Ta'amim **`'֘'`**."""
GERESH_MUQDAM = TaamimChar(char="֝", name="Geresh Muqdam")
"""An instance of `TaamimChar` representing the Ta'amim **`'֝'`**."""
QARNEY_PARA = TaamimChar(char="֟", name="Qarney Para", name_alts=["Pazer Gadol"])
"""An instance of `TaamimChar` representing the Ta'amim **`'֟'`**."""
PAZER_GADOL = QARNEY_PARA
"""Simple pointer to `QARNEY_PARA` since they share the same Unicode character."""
OLA = TaamimChar(char="֫", name="Ola")
"""An instance of `TaamimChar` representing the Ta'amim **`'֫'`**."""
ILUY = TaamimChar(char="֬", name="Iluy")
"""An instance of `TaamimChar` representing the Ta'amim **`'֬'`**."""
RAFE = TaamimChar(char="ֿ", name="Rafe")
"""An instance of `TaamimChar` representing the Ta'amim **`'ֿ'`**."""
METEG = TaamimChar(char="ֽ", name="Meteg")
"""An instance of `TaamimChar` representing the Ta'amim **`'ֽ'`**."""


ALL_CHARS: List[Union[HebrewChar, YiddishChar, NiqqudChar, TaamimChar, OtherChar]] = [
    ALEPH,
    BET,
    VET,
    GIMEL,
    DALET,
    HE,
    VAV,
    ZAYIN,
    CHET,
    TET,
    YOD,
    CAF,
    KAF_SOFIT,
    CHAF,
    CHAF_SOFIT,
    LAMED,
    MEM,
    MEM_SOFIT,
    NUN,
    NUN_SOFIT,
    SAMEKH,
    AYIN,
    PE,
    FE,
    PE_SOFIT,
    FE_SOFIT,
    TSADI,
    TSADI_SOFIT,
    QOF,
    RESH,
    SHIN,
    SIN,
    PLAIN_SIN,
    TAV,
    SAV,
    DOUBLE_YOD,
    DOUBLE_VAV,
    VAV_YOD,
    SIN_DOT,
    SHIN_DOT,
    DAGESH,
    QUBUTS,
    SHURUK,
    HOLAM,
    QAMATS,
    PATAH,
    SEGOL,
    TSERE,
    HIRIQ,
    HATAF_QAMATS,
    HATAF_PATAH,
    HATAF_SEGOL,
    SHEVA,
    UPPER_DOT,
    MAQAF,
    PASEQ,
    SOF_PASSUK,
    ETNAHTA,
    SEGOL_TOP,
    SHALSHELET,
    ZAQEF_QATAN,
    ZAQEF_GADOL,
    TIFCHA,
    REVIA,
    ZINOR,
    PASHTA,
    PASHTA_2,
    YETIV,
    TEVIR,
    PAZER,
    TELISHA_GEDOLA,
    TELISHA_KETANNAH,
    GERESH,
    AZLA_GERESH,
    GERSHAYIM,
    GERSHAYIM_2,
    MERCHA,
    MUNACH,
    MAHPACH,
    DARGA,
    MERCHA_KEFULA,
    YERACH_BEN_YOMO,
    MASORA,
    DEHI,
    ZARQA,
    GERESH_MUQDAM,
    QARNEY_PARA,
    OLA,
    ILUY,
    RAFE,
    METEG,
]
"""
Every instance of a character class.  
This is used for defining collections with list comprehensions based on the Chars metadata. 
It can be relied on as being a complete list of Unicode characters used in Hebrew (and Yiddish etc).
"""


CHARS: Dict[str, Union[HebrewChar, YiddishChar, NiqqudChar, TaamimChar, OtherChar]] = {
    c.char: c for c in ALL_CHARS
}
"""
A dict of all instances of all supported Char types where the key is the char
and the value is an instance of BaseHebrewChar.
This is useful for when you have a hebrew char and want to get its metadata class.

``` python
assert CHARS['א'] == ALEPH
```
"""


FINAL_LETTERS: List[HebrewChar] = [
    c
    for c in ALL_CHARS
    if isinstance(c, HebrewChar) and c.final_letter and len(c.char) == 1
]
"""
A list of all Hebrew characters that are final letters.
While we do have letters like 'ףּ' defined, they do not return in this array; it contains only the plain final letters.
"""

HEBREW_CHARS: List[HebrewChar] = [c for c in ALL_CHARS if isinstance(c, HebrewChar)]
"""A List of all instances of `HebrewChar`. This will include letters like 'ףּ'"""

YIDDISH_CHARS: List[YiddishChar] = [c for c in ALL_CHARS if isinstance(c, YiddishChar)]
"""A List of all instances of `YiddishChar`."""

NIQQUD_CHARS: List[NiqqudChar] = [c for c in ALL_CHARS if isinstance(c, NiqqudChar)]
"""A List of all instances of `NiqqudChar`."""

TAAMIM_CHARS: List[TaamimChar] = [
    c for c in ALL_CHARS if isinstance(c, TaamimChar)
]
"""A List of all instances of `TaamimChar`."""

OTHER_CHARS: List[OtherChar] = [
    c for c in ALL_CHARS if isinstance(c, OtherChar)
]
"""A List of all instances of `OtherChar`."""

_NON_LETTER_CHARS: List[Union[NiqqudChar, TaamimChar, OtherChar]] = [
    c for c in ALL_CHARS if not isinstance(c, HebrewChar) and not isinstance(c, YiddishChar)
]
"""A List of all chars that are not letters. Used internally for filtering non letter chars."""


def char_search(
    char_name: str,
    char_list: Optional[
        List[Union[HebrewChar, YiddishChar, NiqqudChar, TaamimChar, OtherChar]]
    ] = None,
) -> Optional[Union[HebrewChar, YiddishChar, NiqqudChar, TaamimChar, OtherChar]]:
    """
    Search for a character by its name.

    Character classes contain alternate names which are supported by this function!
    Currently, only english names are supported.
    TODO: Support search in hebrew, which will need to support hebrew text with or without nikud.

    :param char_name: A string containing the name of the character to search for.
    :param char_list: A list of `BaseHebrewChar` characters to use for this search.
    When None, defaults to all characters (ALL_CHARS).
    :return:
    """
    char_list = char_list if char_list else ALL_CHARS
    for char in char_list:
        if char_name.lower() in [n.lower() for n in char.names]:
            return CHARS[char.char]
    return None
