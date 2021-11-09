from typing import List, TypeVar

from .grapheme_string import GraphemeString
from .hebrew_glyph import HebrewGlyph

HebrewT = TypeVar("HebrewT", bound="Hebrew")


class Hebrew(GraphemeString):
    # TODO Move all letter definitions to hebrew_glyph.py
    # Letters of the hebrew alphabet
    ALEPH = HebrewGlyph("א")
    VET = HebrewGlyph("ב")
    GIMEL = HebrewGlyph("ג")
    DALET = HebrewGlyph("ד")
    HE = HebrewGlyph("ה")
    VAV = HebrewGlyph("ו")
    ZAYIN = HebrewGlyph("ז")
    HET = HebrewGlyph("ח")
    TET = HebrewGlyph("ט")
    YOD = HebrewGlyph("י")
    KAF = HebrewGlyph("כ")
    FINAL_KAF = HebrewGlyph("ך")
    LAMED = HebrewGlyph("ל")
    MEM = HebrewGlyph("מ")
    FINAL_MEM = HebrewGlyph("ם")
    NUN = HebrewGlyph("נ")
    FINAL_NUN = HebrewGlyph("ן")
    SAMEKH = HebrewGlyph("ס")
    AYIN = HebrewGlyph("ע")
    PE = HebrewGlyph("פ")
    FINAL_PE = HebrewGlyph("ף")
    TSADI = HebrewGlyph("צ")
    FINAL_TSADI = HebrewGlyph("ץ")
    QOF = HebrewGlyph("ק")
    RESH = HebrewGlyph("ר")
    SHIN = HebrewGlyph("ש")
    TAV = HebrewGlyph("ת")

    HEBREW_LETTERS = [
        ALEPH,
        VET,
        GIMEL,
        DALET,
        HE,
        VAV,
        ZAYIN,
        HET,
        TET,
        YOD,
        KAF,
        FINAL_KAF,
        LAMED,
        MEM,
        FINAL_MEM,
        NUN,
        FINAL_NUN,
        SAMEKH,
        AYIN,
        PE,
        FINAL_PE,
        TSADI,
        FINAL_TSADI,
        QOF,
        RESH,
        SHIN,
        TAV,
    ]

    FINAL_LETTERS = [letter for letter in HEBREW_LETTERS if letter.final_letter]

    # Yiddish specific letters
    DOUBLE_YUD = HebrewGlyph("ײ")
    DOUBLE_VAV = HebrewGlyph("װ")
    VAV_YUD = HebrewGlyph("ױ")

    YIDDISH_LETTERS = [DOUBLE_YUD, DOUBLE_VAV, VAV_YUD]

    LETTERS = YIDDISH_LETTERS + HEBREW_LETTERS

    # Niqqudot or Vowel characters
    SIN_DOT = "ׂ"
    SHIN_DOT = "ׁ"
    DAGESH = "ּ"
    QUBUTS = KUBUTZ = "ֻ"
    SHURUK = "וּ"
    HOLAM = "ֹ"
    QAMATS = KUMATZ = "ָ"
    PATAH = PATACH = "ַ"
    SEGOL = "ֶ"
    TSERE = "ֵ"
    HIRIQ = CHIRIK = "ִ"
    HATAF_QAMATS = "ֳ"
    HATAF_PATAH = "ֲ"
    HATAF_SEGOL = "ֱ"
    SHEVA = SHIVAH = "ְ"
    UPPER_DOT = "ׄ"
    NIQQUD = [
        SIN_DOT,
        SHIN_DOT,
        DAGESH,
        QUBUTS,
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
    ]

    # Punctuation characters
    MAQAF = "־"
    PASEQ = "׀"
    SOF_PASSUK = "׃"
    ETNAHTA = "֑"
    SEGOL_TOP = "֒"
    SHALSHELET = "֓"
    ZAQEF_QATAN = "֔"
    ZAQEF_GADOL = "֕"
    TIFCHA = "֖"
    REVIA = "֗"
    ZINOR = "֮"
    PASHTA = "֙"
    PASHTA_2 = QADMA = "֨"
    YETIV = "֚"
    TEVIR = "֛"
    PAZER = "֡"
    TELISHA_GEDOLA = "֠"
    TELISHA_KETANNAH = "֩"
    PAZER_GADOL = "֟"
    GERESH = "׳"
    AZLA_GERESH = "֜"
    GERSHAYIM = "״"
    GERSHAYIM_2 = "֞"
    MERCHA = "֥"
    MUNACH = "֣"
    MAHPACH = "֤"
    DARGA = "֧"
    MERCHA_KEFULA = "֦"
    YERACH_BEN_YOMO = "֪"
    MASORA = "֯"
    DEHI = "֭"
    ZARQA = "֘"
    GERESH_MUQDAM = "֝"
    QARNEY_PARA = "֟"
    OLA = "֫"
    ILUY = "֬"
    RAFE = "ֿ"
    METEG = "ֽ"
    PUNCTUATION = [
        MAQAF,
        PASEQ,
        SOF_PASSUK,
        GERESH,
        GERSHAYIM,
        GERSHAYIM_2,
        RAFE,
        METEG,
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
        PAZER_GADOL,
        TELISHA_GEDOLA,
        TELISHA_KETANNAH,
        AZLA_GERESH,
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
    ]

    def __init__(self, string: str):
        super().__init__(string)

    def __str__(self) -> str:
        return self.string

    def __repr__(self) -> str:
        return self.__str__()

    def no_maqaf(self) -> HebrewT:
        """
        Replaces all maqafs with spaces.

        This is useful for splitting a string into words when you want words connected by maqafs to be considered as one word.
        Example: You may think of "עַל־פְּנֵ֥י" as one word in some cases but want to split it into "עַל" and "פְּנֵי" in other cases.

        :return:
        """
        return Hebrew(self.string.replace(self.MAQAF, " "))

    def no_sof_passuk(self) -> HebrewT:
        """
        Removes all sof_passuk chars.

        :return:
        """
        return Hebrew(self.string.replace(self.SOF_PASSUK, ""))

    def words(self, split_maqaf: bool = False) -> List[HebrewT]:
        """
        Splits the string into a list of words.

        :param split_maqaf: Whether to split a single word such as "עַל־פְּנֵ֥י" into "עַל" and "פְּנֵי" when a maqaf is encountered.
        :return:
        """
        string = self.string if not split_maqaf else self.no_maqaf().string
        return [Hebrew(s) for s in string.split()]

    def text_only(self, remove_maqaf: bool = False) -> HebrewT:
        """
        Returns a string with all non-letter characters removed.
        This will remove both niqqud and punctuation.

        :param remove_maqaf: Wheather to remove the maqaf characters if they are encountered
        :return:
        """
        string = self.no_maqaf().string if remove_maqaf else self.string
        chars_to_remove = self.NIQQUD + [
            p for p in self.PUNCTUATION if p not in (self.MAQAF, self.PASEQ)
        ]
        string = string.replace(
            f" {self.PASEQ} ", " "
        )  # Handled separately to avoid double spaces.
        for char in chars_to_remove:
            string = string.replace(char, "")
        return Hebrew(string)

    def no_niqqud(self) -> HebrewT:
        """
        Removes all niqqud characters.
        This may be useful to practice reading from the torah.

        :return:
        """
        string = self.string
        for char in self.NIQQUD:
            string = string.replace(char, "")
        return Hebrew(string)

    def no_punctuation(
        self, remove_maqaf: bool = False, remove_sof_passuk: bool = False
    ) -> HebrewT:
        """
        Removes all punctuation characters.
        Result is a string with just letters and Nekkudot.

        :param remove_maqaf: Whether to remove the maqaf characters if they are encountered.
        :param remove_sof_passuk: Whether to remove the remove_sof_passuk character if they are encountered.
        :return:
        """
        string = self.no_maqaf().string if remove_maqaf else self.string
        string = Hebrew(string).no_sof_passuk().string if remove_sof_passuk else string
        chars_to_remove = [
            p
            for p in self.PUNCTUATION
            if p not in (self.MAQAF, self.PASEQ, self.SOF_PASSUK)
        ]
        string = string.replace(
            f" {self.PASEQ} ", " "
        )  # Handled separately to avoid double spaces.
        for char in chars_to_remove:
            string = string.replace(char, "")
        return Hebrew(string)
