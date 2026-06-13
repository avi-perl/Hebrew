from typing import Optional, Callable, Tuple

from hebrew.numerical_conversion.substitute import Substitutions
from hebrew.numerical_conversion.mappings import (
    HEBREW_LETTER_TO_VALUE_MAPPINGS,
    STANDARD_HEBREW_LETTERS_VALUES_REVERSED,
)


def number_to_hebrew_string(
    number: int,
    punctuate: bool = True,
    geresh: bool = True,
    substitution_functions: Optional[
        Tuple[Callable[[str], str], ...]
    ] = Substitutions.DEFAULT,
) -> str:
    """
    Convert a number into its Hebrew letter form.

    :param number: The number to convert to Hebrew letters. Must be greater than 0.
    :param punctuate: Whether to add punctuation in the appropriate places.
    :param geresh: If punctuate is true, whether to use the unicode geresh or an apostrophe.
    :param substitution_functions: A tuple of functions that replaces some hebrew values in the result with an
    appropriate equivalent. By default, "יה" and "יו" are replaced with "טו" and "טז" respectively. To replace all
    values such as שמד ,רע, and others, use `Substitutions.ALL`.
    :return: The Hebrew letter representation of the number.
    """
    if number < 1:
        raise ValueError("Number must be greater than 0")

    # Decompose number into place-value components
    ones, tens, hundreds = _decompose_number(number)

    # Build the Hebrew letter string (in reverse, then flip)
    reversed_result = _build_letter_components(ones, tens, hundreds)
    result = reversed_result[::-1]

    # Apply substitution rules (e.g., יה → טו, יו → טז)
    if substitution_functions:
        for func in substitution_functions:
            result = func(result)

    # Add geresh/gershayim punctuation
    if punctuate:
        result = _add_punctuation(result, geresh)

    return result


def _decompose_number(number: int) -> Tuple[int, int, int]:
    """Split a number into ones, tens, and hundreds-and-above components."""
    ones = number % 10
    tens = ((number % 100) // 10) * 10 if number >= 10 else 0
    hundreds = (number // 100) * 100
    return ones, tens, hundreds


def _build_letter_components(ones: int, tens: int, hundreds: int) -> str:
    """Build reversed Hebrew letter string from decomposed number components."""
    reversed_result = ""
    if ones > 0:
        reversed_result += HEBREW_LETTER_TO_VALUE_MAPPINGS[ones]
    if tens > 0:
        reversed_result += HEBREW_LETTER_TO_VALUE_MAPPINGS[tens]
    if hundreds > 0:
        reversed_result += _hundreds_to_letters(hundreds)
    return reversed_result


def _hundreds_to_letters(number: int) -> str:
    """
    Convert a hundreds-and-above value to Hebrew letters (in reverse order).

    :param number: The value to convert (must be a multiple of 100).
    :return: Hebrew letters representing the number, in reverse order.
    """
    # Check if the number maps directly to a letter
    if number in HEBREW_LETTER_TO_VALUE_MAPPINGS:
        return HEBREW_LETTER_TO_VALUE_MAPPINGS[number]

    # Get the largest letter value that fits into the number
    max_letter_value = next(
        i for i in STANDARD_HEBREW_LETTERS_VALUES_REVERSED if i <= number
    )
    max_letter = HEBREW_LETTER_TO_VALUE_MAPPINGS[max_letter_value]

    # Calculate how many times the letter goes into the number
    letter_count, remainder = divmod(number, max_letter_value)

    if remainder == 0:
        return max_letter * letter_count
    else:
        # Recursively handle the remainder
        remainder_letters = _hundreds_to_letters(remainder)
        return remainder_letters + max_letter * letter_count


def _add_punctuation(result: str, geresh: bool) -> str:
    """Add geresh (׳) or gershayim (״) punctuation to a Hebrew number string."""
    if len(result) > 1:
        punctuation = "״" if geresh else '"'
        result = result[:-1] + punctuation + result[-1]
    else:
        punctuation = "׳" if geresh else "'"
        result += punctuation
    return result



