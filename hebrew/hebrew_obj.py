from functools import reduce
from typing import List, TypeVar
from operator import add

from .grapheme_string import GraphemeString
from .chars import (
    MAQAF,
    NIQQUD_CHARS,
    TAAMIM_CHARS,
    PASEQ,
    SOF_PASSUK,
    CHARS,
    _NON_LETTER_CHARS,
)
from hebrew.gematria import GematriaTypes

HebrewT = TypeVar("HebrewT", bound="Hebrew")


class Hebrew(GraphemeString):
    """
    A class representing a Hebrew String.

    A `Hebrew` string can contain pure Hebrew letters, or can be composed of any additional characters.
    """

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
        return Hebrew(self.string.replace(MAQAF.char, " "))

    def no_sof_passuk(self) -> HebrewT:
        """
        Removes all sof_passuk chars.

        :return:
        """
        return Hebrew(self.string.replace(SOF_PASSUK.char, ""))

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

        :param remove_maqaf: Whether to remove the maqaf characters if they are encountered
        :return:
        """
        string = self.no_maqaf().string if remove_maqaf else self.string
        chars_to_remove = [c.char for c in _NON_LETTER_CHARS if c not in (MAQAF, PASEQ)]
        string = string.replace(
            f" {PASEQ.char} ", " "
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
        for char in [c.char for c in NIQQUD_CHARS]:
            string = string.replace(char, "")
        return Hebrew(string)

    def no_taamim(
        self, remove_maqaf: bool = False, remove_sof_passuk: bool = False
    ) -> HebrewT:
        """
        Removes all [Ta'amim](https://en.wikipedia.org/wiki/Hebrew_cantillation) characters.
        Result is a string with just letters and Niqqud characters.

        :param remove_maqaf: Whether to remove the maqaf characters if they are encountered.
        :param remove_sof_passuk: Whether to remove the remove_sof_passuk character if they are encountered.
        :return:
        """
        string = self.no_maqaf().string if remove_maqaf else self.string
        string = Hebrew(string).no_sof_passuk().string if remove_sof_passuk else string
        chars_to_remove = [
            p.char for p in TAAMIM_CHARS if p not in (MAQAF, PASEQ, SOF_PASSUK)
        ]
        string = string.replace(
            f" {PASEQ.char} ", " "
        )  # Handled separately to avoid double spaces.
        for char in chars_to_remove:
            string = string.replace(char, "")
        return Hebrew(string)

    def gematria(self, method: GematriaTypes = GematriaTypes.MISPAR_HECHRACHI) -> int:
        """
        Returns the gematria of the string.

        If the contains no hebrew characters, the value returned is 0. Mixing hebrew and english characters is ok!

        :param method: The method to use for calculating the gematria.
        :return:
        """
        chars = [
            CHARS[c]
            for c in self.string
            if CHARS.get(c) and hasattr(CHARS[c], method.value)
        ]
        if len(chars) == 0:
            # The list will be 0 if there are no letters in the string or if the letters are not hebrew.
            return 0
        else:
            return reduce(add, [getattr(c, method.value) for c in chars])
