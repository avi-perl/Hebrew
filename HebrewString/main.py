from typing import List, TypeVar

import grapheme

HebrewStringT = TypeVar("HebrewStringT", bound="HebrewString")


class HebrewString:
    YIDDISH_LETTERS = ["װ", "ױ", "ײ"]
    HEBREW_LETTERS = [
        "א",
        "ב",
        "ג",
        "ד",
        "ה",
        "ו",
        "ז",
        "ח",
        "ט",
        "י",
        "כ",
        "ך",
        "ל",
        "מ",
        "ם",
        "נ",
        "ן",
        "ס",
        "ע",
        "פ",
        "ף",
        "צ",
        "ץ",
        "ק",
        "ר",
        "ש",
        "ת",
    ]
    LETTERS = YIDDISH_LETTERS + HEBREW_LETTERS
    NIQQUD = ["ׂ", "ׁ", "ּ", "ֻ", "ֹ", "ָ", "ַ", "ֶ", "ֵ", "ִ", "ֳ", "ֲ", "ֱ", "ְ", "ׄ"]
    MAQAF = "־"
    PUNCTUATION = ["״", "׳", "׃", "ׂ", "ׁ", "׀", "ֿ", "ֽ", MAQAF]
    TRUP = [
        "֑",
        "֒",
        "֓",
        "֔",
        "֕",
        "֖",
        "֗",
        "֘",
        "֙",
        "֚",
        "֛",
        "֜",
        "֝",
        "֞",
        "֟",
        "֠",
        "֡",
        "֣",
        "֤",
        "֥",
        "֦",
        "֧",
        "֨",
        "֩",
        "֪",
        "֫",
        "֬",
        "֭",
        "֮",
        "֯",
    ]

    def __init__(self, string: str):
        self.string = string
        self.graphemes = [g for g in grapheme.graphemes(string)]

    def __str__(self) -> str:
        return self.string

    def __repr__(self) -> str:
        return self.__str__()

    def as_str(self) -> str:
        return self.string

    @property
    def without_maqaf(self) -> str:
        return self.string.replace(self.MAQAF, " ")

    @property
    def words(self) -> List[HebrewStringT]:
        return [HebrewString(s) for s in self.without_maqaf.split()]

    @property
    def strip_non_letters(self) -> str:
        string = "".join(
            [l for l in self.string if l in self.LETTERS or l in (" ", self.MAQAF)]
        )
        return " ".join(string.split())

    @property
    def strip_non_letters_no_maqaf(self) -> str:
        return self.strip_non_letters.replace(self.MAQAF, " ")

    @property
    def strip_niqqud(self) -> str:
        return "".join([l for l in self.string if l not in self.NIQQUD])

    @property
    def strip_trup(self) -> str:
        return "".join([l for l in self.string if l not in self.TRUP])
