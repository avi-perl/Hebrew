import re
from typing import Callable


def yud_hey_to_tes_vav(value: str) -> str:
    """Substitute 'יה' for 'טו'"""
    return re.sub(r"יה$", "טו", value)


def yud_vav_to_tes_zayen(value: str) -> str:
    """Substitute 'יו' for 'טז'"""
    return re.sub(r"יו$", "טז", value)


def _get_word_substitution_func(bad: str, good: str) -> Callable[[str], str]:
    def word_substitution_func(value: str) -> str:
        """Substitute the first word for the second word"""
        return re.sub(bad, good, value)
    return word_substitution_func


POLITE_WORD_MAP = {
    r"רע$": "ער",
    r"רעב$": "ערב",
    r"^רעה$": "ערה",
    r"רצח$": "רחצ",
    r"^שד$": "דש",
    r"שמד$": "שדמ",
}

_BASIC_FUNCTIONS = [yud_hey_to_tes_vav, yud_vav_to_tes_zayen]


class Substitutions:
    """"""
    DEFAULT = _BASIC_FUNCTIONS
    ALL = [_get_word_substitution_func(w[0], w[1]) for w in POLITE_WORD_MAP.items()] + _BASIC_FUNCTIONS
