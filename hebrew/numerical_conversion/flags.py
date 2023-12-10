import re
from typing import Callable, Optional, Tuple
from unittest.mock import DEFAULT


class SubstitutionLogic:
    def __init__(
        self,
        find: Optional[str] = None,
        replace: Optional[str] = None,
        custom: Optional[Callable[[str], str]] = None,
    ):
        """
        A class to hold the logic for a substitution.
        Either find and replace or custom must be provided.
        If find and replace are provided, they will be used to replace the string.
        If custom is provided, it will be used to replace the string.

        :param find: The string to find.
        :param replace: The string to replace the found string with.
        :param custom: A custom function to use to replace the string.
        :return:

        """
        if custom is None and (find is None or replace is None):
            raise ValueError("Either custom or find and replace must be provided")
        self.find = find
        self.replace = replace
        self.custom = custom

    def sub(self, string: str) -> str:
        if self.custom:
            return self.custom(string)
        elif self.find and self.replace:
            return re.sub(self.find, self.replace, string, flags=re.MULTILINE)
        else:
            raise ValueError("Either custom or find and replace must be provided")

    def __eq__(self, __value: "SubstitutionLogic") -> bool:
        return self.find == __value.find and self.replace == __value.replace

    def __repr__(self):
        return f"_FlagData(find={self.find}, replace={self.replace})"


class SubstitutionFlag:
    def __init__(self, data: SubstitutionLogic | Tuple[SubstitutionLogic, ...]):
        if isinstance(data, SubstitutionLogic):
            self.flags = (data,)
        elif isinstance(data, Tuple):
            self.flags = data
        else:
            raise TypeError(
                "data must be a SubstitutionLogic or a list of SubstitutionLogic"
            )

    def __add__(self, other: "SubstitutionFlag") -> "SubstitutionFlag":
        flags = self.flags + other.flags
        return SubstitutionFlag(flags)

    def __eq__(self, __value: "SubstitutionFlag") -> bool:
        return self.flags == __value.flags

    def __repr__(self):
        return f"SubstitutionFlag({self.flags})"


class SubstitutionFlags:
    """
    A collection of flags to use when converting numbers to Hebrew letters.
    The logic for each of these flags was sourced from DavkaWriters polite page numbers.
    """

    YUD_HEY = SubstitutionFlag(SubstitutionLogic(r"יה$", "טו"))
    "Substitute the word 'יה' for 'טו'"

    YUD_VAV = SubstitutionFlag(SubstitutionLogic(r"יו$", "טז"))
    "Substitute the word 'יו' for 'טז'"

    RA = SubstitutionFlag(SubstitutionLogic(custom=lambda x: re.sub(r"רע$", "ער", x)))
    "Substitute the word 'רע' for 'ער'"

    RAAV = SubstitutionFlag(SubstitutionLogic(r"רעב$", "ערב"))
    "Substitute the word 'רעב' for 'ערב'"

    RAAH = SubstitutionFlag(SubstitutionLogic(r"^רעה$", "ערה"))
    "Substitute the word 'רעה' for 'ערה'"

    ROTZEACH = SubstitutionFlag(SubstitutionLogic(r"רצח$", "רחצ"))
    "Substitute the word 'רצח' for 'רחצ'"

    SHAID = SubstitutionFlag(SubstitutionLogic(r"^שד$", "דש"))
    "Substitute the word 'שד' for 'דש'"

    SHMAAD = SubstitutionFlag(SubstitutionLogic(r"שמד$", "שדמ"))
    "Substitute the word 'שמד' for 'שדמ'"

    DEFAULT = YUD_HEY + YUD_VAV
    "The default flags to use when converting numbers to Hebrew letters. By default, the 'יה' and 'יו' are replaced with 'טו' and 'טז' respectively."

    @staticmethod
    def all() -> SubstitutionFlag:
        """
        Return all the flags in a list.
        """
        return (
            SubstitutionFlags.YUD_HEY
            + SubstitutionFlags.YUD_VAV
            + SubstitutionFlags.RA
            + SubstitutionFlags.RAAV
            + SubstitutionFlags.RAAH
            + SubstitutionFlags.ROTZEACH
            + SubstitutionFlags.SHAID
            + SubstitutionFlags.SHMAAD
        )
