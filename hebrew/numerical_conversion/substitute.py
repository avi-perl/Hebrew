import re
from typing import Callable, Optional, Tuple, TypeVar

SUBSTITUTION = Callable[[str], str]


class SubstitutionFlag:
    def __init__(self, data: SUBSTITUTION | Tuple[SUBSTITUTION, ...]):
        if isinstance(data, Tuple):
            self.flags = data
        else:
            self.flags = (data,)

    def __add__(self, other: "SubstitutionFlag") -> "SubstitutionFlag":
        flags = self.flags + other.flags
        return SubstitutionFlag(flags)

    def __eq__(self, __value: "SubstitutionFlag") -> bool:
        return self.flags == __value.flags

    def __repr__(self):
        return f"SubstitutionFlag({self.flags})"


class Substitutions:
    """
    A collection of flags to use when converting numbers to Hebrew letters.
    The logic for each of these flags was sourced from DavkaWriters polite page numbers.
    """

    YUD_HEY = SubstitutionFlag(lambda x: re.sub(r"יה$", "טו", x))
    "Substitute the word 'יה' for 'טו'"

    YUD_VAV = SubstitutionFlag(lambda x: re.sub(r"יו$", "טז", x))
    "Substitute the word 'יו' for 'טז'"

    RA = SubstitutionFlag(lambda x: re.sub(r"רע$", "ער", x))
    "Substitute the word 'רע' for 'ער'"

    RAAV = SubstitutionFlag(lambda x: re.sub(r"רעב$", "ערב", x))
    "Substitute the word 'רעב' for 'ערב'"

    RAAH = SubstitutionFlag(lambda x: re.sub(r"^רעה$", "ערה", x))
    "Substitute the word 'רעה' for 'ערה'"

    ROTZEACH = SubstitutionFlag(lambda x: re.sub(r"רצח$", "רחצ", x))
    "Substitute the word 'רצח' for 'רחצ'"

    SHAID = SubstitutionFlag(lambda x: re.sub(r"^שד$", "דש", x))
    "Substitute the word 'שד' for 'דש'"

    SHMAAD = SubstitutionFlag(lambda x: re.sub(r"שמד$", "שדמ", x))
    "Substitute the word 'שמד' for 'שדמ'"

    DEFAULT = YUD_HEY + YUD_VAV
    "The default flags to use when converting numbers to Hebrew letters. By default, the 'יה' and 'יו' are replaced with 'טו' and 'טז' respectively."

    ALL = YUD_HEY + YUD_VAV + RA + RAAV + RAAH + ROTZEACH + SHAID + SHMAAD
    "All available flags."
