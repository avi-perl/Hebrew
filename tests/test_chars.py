import collections

from hebrew.chars import *


def test_all_hebrew_letters_represented():
    all_unicode_chars_defined = [c.char for c in ALL_CHARS if len(c.char) == 1]
    all_unicode_chars = [
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
        "֢",
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
        "ְ",
        "ֱ",
        "ֲ",
        "ֳ",
        "ִ",
        "ֵ",
        "ֶ",
        "ַ",
        "ָ",
        "ֹ",
        "ֺ",
        "ֻ",
        "ּ",
        "ֽ",
        "־",
        "ֿ",
        "׀",
        "ׁ",
        "ׂ",
        "׃",
        "ׄ",
        "ׅ",
        "׆",
        "ׇ",
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
        "ך",
        "כ",
        "ל",
        "ם",
        "מ",
        "ן",
        "נ",
        "ס",
        "ע",
        "ף",
        "פ",
        "ץ",
        "צ",
        "ק",
        "ר",
        "ש",
        "ת",
        "ׯ",
        "װ",
        "ױ",
        "ײ",
        "׳",
        "״",
        "ℵ",
        "ℶ",
        "ℷ",
        "ℸ",
        "יִ",
        "ﬞ",
        "ײַ",
        "ﬠ",
        "ﬡ",
        "ﬢ",
        "ﬣ",
        "ﬤ",
        "ﬥ",
        "ﬦ",
        "ﬧ",
        "ﬨ",
        "﬩",
        "שׁ",
        "שׂ",
        "שּׁ",
        "שּׂ",
        "אַ",
        "אָ",
        "אּ",
        "בּ",
        "גּ",
        "דּ",
        "הּ",
        "וּ",
        "זּ",
        "טּ",
        "יּ",
        "ךּ",
        "כּ",
        "לּ",
        "מּ",
        "נּ",
        "סּ",
        "ףּ",
        "פּ",
        "צּ",
        "קּ",
        "רּ",
        "שּ",
        "תּ",
        "וֹ",
        "בֿ",
        "כֿ",
        "פֿ",
        "ﭏ",
    ]

    assert len(all_unicode_chars) == len(
        set(all_unicode_chars)
    ), "There are duplicate values in all_unicode_chars"
    for char in all_unicode_chars:
        assert (
            len(char) == 1
        ), f"all_unicode_chars contains a char that is not a single character: {char}"
    assert sorted(all_unicode_chars_defined) == sorted(all_unicode_chars), (
        f"The following hebrew related chars are missing from `hebrew.chars`: "
        f"{[c for c in all_unicode_chars if c not in all_unicode_chars_defined]}"
    )


def test_hebrew_char_hebrew_names():
    tsadi_sofit = HebrewChar(
        char="ץ",
        name="Tsadi Sofit",
        final_letter=True,
        hebrew_name="צַדִי סוֹפִית",
        hebrew_name_alts=["צדיק סופית"],
    )
    assert sorted(tsadi_sofit.hebrew_names) == sorted(["צַדִי סוֹפִית", "צדיק סופית"])


def test_hebrew_char_names():
    aleph = HebrewChar(char="א", name="Aleph", hebrew_name="אָלֶף", name_alts=["Alef"])
    assert sorted(aleph.names) == sorted(["Aleph", "Alef"])


def test_hebrew_char_str():
    aleph = HebrewChar(char="א", name="Aleph", hebrew_name="אָלֶף", name_alts=["Alef"])
    assert str(aleph) == "א"


def test_base_letter():
    bet_with_dot = HebrewChar(char="בּ", name="Bet")
    assert bet_with_dot.base_letter.char == "ב"


def test_final_letters():
    final_chars = ["ץ", "ף", "ן", "ם", "ך"]
    assert len(final_chars) == len(FINAL_LETTERS)
    for char in final_chars:
        assert char in [c.char for c in FINAL_LETTERS]


def test_hebrew_chars():
    assert len(HEBREW_CHARS) > 0
    for char in HEBREW_CHARS:
        assert type(char) == HebrewChar


def test_yiddish_chars():
    yiddish_letters = ["ױ", "װ", "ײ"]
    assert len(yiddish_letters) == len(YIDDISH_CHARS)
    for char in yiddish_letters:
        assert char in [c.char for c in YIDDISH_CHARS]


def test_niqqud_chars():
    assert len(NIQQUD_CHARS) > 0
    for char in NIQQUD_CHARS:
        assert type(char) == NiqqudChar


def test_taamim_chars():
    assert len(TAAMIM_CHARS) > 0
    for char in TAAMIM_CHARS:
        assert type(char) == TaamimChar


def test_other_chars():
    assert len(OTHER_CHARS) > 0
    for char in OTHER_CHARS:
        assert type(char) == OtherChar


def test_char_dict():
    assert len(CHARS) == len(
        ALL_CHARS
    ), "The _ALL_CHARS array may contain values with duplicate char values"


def test_char_search():
    assert isinstance(
        char_search("Aleph"), HebrewChar
    ), "HebrewChar.search should return a HebrewChar instance"
    assert isinstance(char_search("aLEPH"), HebrewChar), "Should be case insensitive"
    assert char_search("Bad Value") is None


def test_char_search_use_alt_names():
    search_result = char_search("Hei")
    assert isinstance(search_result, HebrewChar)
    assert search_result.char == "ה"
    assert search_result.name != "Hei"


def test_char_search_use_char_list():
    assert char_search("Aleph") == ALEPH
    assert char_search("Alef", NIQQUD_CHARS) is None
    assert char_search("Kumatz", NIQQUD_CHARS) == KUMATZ


def test_hebrew_char_search():
    assert HebrewChar.search("Aleph") == ALEPH
    assert HebrewChar.search("Double Vav") is None


def test_yiddish_char_search():
    assert YiddishChar.search("Double Vav") == DOUBLE_VAV
    assert YiddishChar.search("Aleph") is None


def test_niqqud_char_search():
    assert NiqqudChar.search("Kumatz") == KUMATZ
    assert NiqqudChar.search("Double Vav") is None


def test_taamim_char_search():
    assert TaamimChar.search("Shalshelet") == SHALSHELET
    assert TaamimChar.search("Kumatz") is None


def test_other_char_search():
    assert OtherChar.search("Geresh") == GERESH
    assert OtherChar.search("Kumatz") is None


def test_hebrew_char_hashable():
    assert hash(
        HebrewChar(char="א", name="Aleph", hebrew_name="אָלֶף", name_alts=["Alef"])
    )


def test_yiddish_char_hashable():
    assert hash(YiddishChar(char="ײ", name="Double Yod", name_alts=["Saf"]))


def test_taamim_char_hashable():
    assert hash(TaamimChar(char="֧", name="Darga"))


def test_niqqud_char_hashable():
    assert hash(NiqqudChar(char="ׂ", name="Sin Dot"))


def test_other_char_hashable():
    assert hash(OtherChar(char="׃", name="Sof Passuk"))


def test_hebrew_char_eq():
    hebrew_one = HebrewChar(
        char="א", name="Aleph", hebrew_name="אָלֶף", name_alts=["Alef"]
    )
    hebrew_two = HebrewChar(
        char="בּ", name="Bet", hebrew_name="בֵּית", hebrew_name_alts=["בת"]
    )
    assert hebrew_one == hebrew_one
    assert hebrew_one != hebrew_two
    assert hebrew_one != 5


def test_yiddish_char_eq():
    yiddish_one = YiddishChar(char="ױ", name="Vav Yod")
    yiddish_two = YiddishChar(
        char="װ",
        name="Double Vav",
        name_alts=["Double Vuv"],
    )
    assert yiddish_one == yiddish_one
    assert yiddish_one != yiddish_two
    assert yiddish_one != 5


def test_niqqud_char_eq():
    niqqud_one = NiqqudChar(char="ׂ", name="Sin Dot")
    niqqud_two = NiqqudChar(char="ׁ", name="Shin Dot")
    assert niqqud_one == niqqud_one
    assert niqqud_one != niqqud_two
    assert niqqud_one != 5


def test_taamim_char_eq():
    taamim_one = TaamimChar(char="֙", name="Pashta")
    taamim_two = TaamimChar(char="֚", name="Yetiv")
    assert taamim_one == taamim_one
    assert taamim_one != taamim_two
    assert taamim_one != 5


def test_other_char_eq():
    other_one = OtherChar(char="־", name="Maqaf")
    other_two = OtherChar(char="׀", name="Paseq")
    assert other_one == other_one
    assert other_one != other_two
    assert other_one != 5
