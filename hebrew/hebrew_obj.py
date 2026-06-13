import unicodedata
from functools import reduce
from typing import List, Optional, TypeVar, Dict, Callable, Tuple
from operator import add

from hebrew.numerical_conversion.substitute import Substitutions

from .grapheme_string import GraphemeString
from .chars import (
    MAQAF,
    NIQQUD_CHARS,
    TAAMIM_CHARS,
    PASEQ,
    SOF_PASSUK,
    _NON_LETTER_CHARS,
    CHARS,
    HEBREW_CHARS,
    FINAL_MINOR_LETTER_MAPPINGS,
    HebrewChar,
    SPECIAL_CHARACTER_NORMALIZED_MAPPING,
    YiddishChar,
)
from .numerical_conversion.convert import number_to_hebrew_string
from hebrew.gematria import GematriaTypes

HebrewT = TypeVar("HebrewT", bound="Hebrew")


def get_hebrew_name(letter: HebrewChar, name_dict) -> str:
    """
    Helper function to get the letters name from the library definition
    or from the alts provided by the user.

    The name value passed *must* be a name that is defined in the characters `HebrewChar` instance or a
    ValueError will be thrown. This is done to make sure that only valid naming is used.
    """
    if not name_dict:
        name_dict = {}

    if name_dict and letter.char in name_dict.keys():
        name = name_dict.get(letter.char)
        clean_name = Hebrew(name).text_only()
        if clean_name not in [Hebrew(nm).text_only() for nm in letter.hebrew_names]:
            raise ValueError(f"{name} is not a valid name for {letter}")
        return clean_name.string
    else:
        return letter.hebrew_name


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

    def normalize(self, normalize_yiddish: bool = False) -> HebrewT:
        """
        Replaces all non-standard hebrew characters with their equivalent values
        using normal hebrew letters and symbols. This is important when using hebrew fonts. Some fonts may not
        support these special characters, normalization helps by changing all the characters to be ones that would be
        supported.

        :param normalize_yiddish: By default, yiddish characters are left alone since they are typically desired.
        :return:
        """
        normalized = unicodedata.normalize("NFC", self.string)
        # normalized = self.string
        special_chars: dict = (
            SPECIAL_CHARACTER_NORMALIZED_MAPPING
            if normalize_yiddish
            else {
                k: v
                for k, v in SPECIAL_CHARACTER_NORMALIZED_MAPPING.items()
                if not isinstance(k, YiddishChar)
            }
        )
        special_chars = {
            k.char: "".join([val.char for val in v]) if isinstance(v, list) else v.char
            for k, v in special_chars.items()
        }
        if any(char in normalized for char in special_chars):
            for k, v in special_chars.items():
                normalized = normalized.replace(k, v)
        self.string = normalized
        return self

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

    def gematria(
        self,
        method: GematriaTypes = GematriaTypes.MISPAR_HECHRACHI,
        alt_letter_name_spelling: Dict[str, str] = None,
    ) -> int:
        """
        Returns the gematria of the string.

        If the contains no hebrew characters, the value returned is 0. Mixing hebrew and english characters is ok!

        :param method: The method to use for calculating the gematria.
        :param alt_letter_name_spelling: Used only with MISPAR_SHEMI_MILUI: A dict of alternate spellings for a letter
        that should be used to make the calculation. Eg: `{"ו": "ואו"}`.
        :return:
        """
        # Remove non hebrew characters
        cleaned_string: str = "".join(
            [c for c in self.string if c in [x.char for x in HEBREW_CHARS] or c == " "]
        )

        # Dispatch to the appropriate complex gematria calculator
        _complex_dispatch = {
            GematriaTypes.MISPAR_MUSAFI: self._gematria_musafi,
            GematriaTypes.MISPAR_KOLEL: self._gematria_kolel,
            GematriaTypes.MISPAR_BONEEH: self._gematria_boneeh,
            GematriaTypes.MISPAR_HAMERUBAH_HAKLALI: self._gematria_hamerubah,
            GematriaTypes.MISPAR_HAACHOR: self._gematria_haachor,
            GematriaTypes.MISPAR_KATAN_MISPARI: self._gematria_katan_mispari,
            GematriaTypes.MISPAR_SHEMI_MILUI: self._gematria_shemi_milui,
            GematriaTypes.MISPAR_NEELAM: self._gematria_neelam,
        }

        calculator = _complex_dispatch.get(method)
        if calculator is not None:
            return calculator(cleaned_string, alt_letter_name_spelling)

        # Simple gematria that can be calculated by simply adding each letters value up to a final number.
        return self.__calculate_simple_gematria(self.string, method)

    # ─── Complex Gematria Calculators ────────────────────────────────────────

    def _gematria_musafi(self, cleaned_string: str, _alt_spelling=None) -> int:
        """Mispar Musafi: standard value + letter count."""
        value = self.__calculate_simple_gematria(cleaned_string)
        hebrew_letters = [c for c in cleaned_string if c != " "]
        return value + len(hebrew_letters)

    def _gematria_kolel(self, cleaned_string: str, _alt_spelling=None) -> int:
        """Mispar Kolel: standard value + word count."""
        value = self.__calculate_simple_gematria(cleaned_string)
        hebrew_words = cleaned_string.split()
        return value + len(hebrew_words)

    def _gematria_boneeh(self, cleaned_string: str, _alt_spelling=None) -> int:
        """Mispar Bone'eh: progressive building value (each letter adds sum of all previous)."""
        values = [
            self.__calculate_simple_gematria(c)
            for c in [x for x in cleaned_string if x != " "]
        ]
        total = 0
        for i, n in enumerate(values):
            total += sum(values[:i]) + n
        return total

    def _gematria_hamerubah(self, cleaned_string: str, _alt_spelling=None) -> int:
        """Mispar HaMerubah HaKlali: standard value squared."""
        return self.__calculate_simple_gematria(cleaned_string) ** 2

    def _gematria_haachor(self, cleaned_string: str, _alt_spelling=None) -> int:
        """Mispar Ha'achor: position-weighted value (letter value × position)."""
        values = [
            self.__calculate_simple_gematria(c)
            for c in [x for x in cleaned_string if x != " "]
        ]
        total = 0
        for i, n in enumerate(values):
            total += n * (i + 1)
        return total

    def _gematria_katan_mispari(self, cleaned_string: str, _alt_spelling=None) -> int:
        """Mispar Katan Mispari: digital root of the standard value."""
        calculated_value = self.__calculate_simple_gematria(cleaned_string)
        while calculated_value > 9:
            calculated_value = sum([int(x) for x in str(calculated_value)])
        return calculated_value

    def _gematria_shemi_milui(self, cleaned_string: str, alt_letter_name_spelling=None) -> int:
        """Mispar Shemi (Milui): value of each letter's full name."""
        chars = self._get_letters_with_replaced_finals(cleaned_string)
        values = [
            self.__calculate_simple_gematria(
                get_hebrew_name(c, alt_letter_name_spelling)
            )
            for c in chars
        ]
        return sum(values)

    def _gematria_neelam(self, cleaned_string: str, alt_letter_name_spelling=None) -> int:
        """Mispar Ne'elam (hidden value): value of each letter's name without the letter itself."""
        chars = self._get_letters_with_replaced_finals(cleaned_string)
        names = [
            get_hebrew_name(c, alt_letter_name_spelling)
            for c in chars
        ]
        values = [self.__calculate_simple_gematria(c[1:]) for c in names]
        return sum(values)

    @staticmethod
    def _get_letters_with_replaced_finals(cleaned_string: str) -> List[HebrewChar]:
        """Extract HebrewChar instances, replacing final letters with non-final equivalents."""
        chars: List[HebrewChar] = [
            CHARS[c] for c in [x for x in cleaned_string if x != " "]
        ]
        return [
            CHARS[FINAL_MINOR_LETTER_MAPPINGS.get(c.char)] if c.final_letter else c
            for c in chars
        ]

    @classmethod
    def from_number(
        cls,
        number: int,
        punctuate: bool = True,
        geresh: bool = True,
        substitution_functions: Optional[
            Tuple[Callable[[str], str], ...]
        ] = Substitutions.DEFAULT,
    ):
        """
        Convert a number into its Hebrew letter form, returning it as an instance of Hebrew.

        :param number: The number to convert to Hebrew letters. Must be greater than 0...
        :param punctuate: Whether to add punctuation in the appropriate places.
        :param geresh: If punctuate is true, whether to use the unicode geresh or an apostrophe.
        :param substitution_functions: A tuple of functions that replaces some hebrew values in the result with an
        appropriate equivalent. By default, "יה" and "יו" are replaced with "טו" and "טז" respectively. To replace all
        values such as שמד ,רע, and others, use `Substitutions.ALL`.
        :return:
        """
        return cls(
            number_to_hebrew_string(number, punctuate, geresh, substitution_functions)
        )

    @staticmethod
    def __calculate_simple_gematria(
        string: str, method: GematriaTypes = GematriaTypes.MISPAR_HECHRACHI
    ) -> int:
        """Calculate Gematria for simple Gematria that use a value map for each letter."""
        chars = [
            CHARS[c] for c in string if CHARS.get(c) and hasattr(CHARS[c], method.value)
        ]
        if len(chars) == 0:
            # The list will be 0 if there are no letters in the string or if the letters are not hebrew.
            return 0
        else:
            return reduce(add, [getattr(c, method.value) for c in chars])
