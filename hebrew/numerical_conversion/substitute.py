import re
from typing import Callable


def yud_hey_to_tes_vav(value: str) -> str:
    """Used to substitute 'יה' for 'טו' in a string"""
    return re.sub(r"יה$", "טו", value)


def yud_vav_to_tes_zayen(value: str) -> str:
    """Used to substitute 'יו' for 'טז' in a string"""
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
'Map of "impolite" words, and their polite equivalents.'

_BASIC_FUNCTIONS = (yud_hey_to_tes_vav, yud_vav_to_tes_zayen)


class Substitutions:
    """
    Constants containing sets of functions for use in substitution_functions.
    """

    DEFAULT = _BASIC_FUNCTIONS
    "The default set of substitutions; 'טו' and 'טז'"

    ALL = (
        tuple(_get_word_substitution_func(w[0], w[1]) for w in POLITE_WORD_MAP.items())
        + _BASIC_FUNCTIONS
    )

    "All available substitution functions. See `POLITE_WORD_MAP` and `DEFAULT`; 'טו' and 'טז'"
