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
    :return:
    """
    # Handle 0
    if number < 1:
        raise ValueError("Number must be greater than 0")

    reversed_result = ""

    # Prepare the numbers
    ones_value = _ones_column_value(number)
    if ones_value > 0:
        reversed_result += HEBREW_LETTER_TO_VALUE_MAPPINGS[ones_value]
    tens_value = _tens_column_value(number)
    if tens_value > 0:
        reversed_result += HEBREW_LETTER_TO_VALUE_MAPPINGS[tens_value]
    hundreds_value = _hundreds_and_above_column_value(number)
    if hundreds_value > 0:
        reversed_result += _hundreds_to_letters(hundreds_value)

    # Reverse the string
    result = reversed_result[::-1]

    # Substitute flags
    if substitution_functions:
        for func in substitution_functions:
            result = func(result)

    # Add Punctuation
    if punctuate:
        if len(result) > 1:
            punctuation = "״" if geresh else '"'
            result = result[:-1] + punctuation + result[-1]
        else:
            punctuation = "׳" if geresh else "'"
            result += punctuation

    return result


def _ones_column_value(number: int):
    """
    Return the value of the ones column of a number.
    """
    return number % 10


def _tens_column_value(number: int):
    """
    Return the value of the tens column of a number.
    """
    if number < 10:
        return 0
    return ((number % 100) // 10) * 10


def _hundreds_and_above_column_value(number: int):
    """
    Returns the value of all columns of a number above the ten's column.
    """
    return (number // 100) * 100


def _hundreds_to_letters(number: int) -> str:
    """
    Given a single digit number over 0 and a power of ten, return the Hebrew letters that represent that number.

    :param number: The digit to convert to Hebrew letters.
    :return: The Hebrew letters that represent the number.
    """

    # Check if the number maps directly to a letter
    if number in HEBREW_LETTER_TO_VALUE_MAPPINGS:
        return HEBREW_LETTER_TO_VALUE_MAPPINGS[number]
    else:
        # Get the largest letter and value that is less or equal to the number
        max_letter_value = next(
            i for i in STANDARD_HEBREW_LETTERS_VALUES_REVERSED if i <= number
        )
        max_letter = HEBREW_LETTER_TO_VALUE_MAPPINGS[max_letter_value]

        # Calculate the number of times the letter goes into the number
        letter_count, remainder = divmod(number, max_letter_value)

        # If the remainder is 0, we can just return the letter times the letter count
        if remainder == 0:
            return max_letter * letter_count
        else:
            # Otherwise we need to further break down the remainder
            remainder_letters = _hundreds_to_letters(remainder)
            return remainder_letters + max_letter * letter_count
