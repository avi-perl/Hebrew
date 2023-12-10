from typing import Optional
import re
from hebrew.numerical_conversion.flags import SubstitutionFlag, SubstitutionFlags
from hebrew.numerical_conversion.mappings import (
    HEBREW_LETTER_TO_VALUE_MAPPINGS,
    STANDARD_HEBREW_LETTERS_VALUES_REVERSED,
)


def number_to_hebrew_string(
    number: int,
    punctuate: bool = True,
    geresh: bool = True,
    substitution_flags: Optional[SubstitutionFlag] = SubstitutionFlags.DEFAULT,
) -> str:
    """
    Create a new instance of the Hebrew class representing a given number in its Hebrew letter form.

    :param number: The number to convert to Hebrew letters. Must be greater than 0.
    :param punctuate: Whether to add punctuation in the appropriate places.
    :param geresh: If punctuate is true, whether to use the unicode geresh or an apostrophe.
    :param substitution_flags: Flags to use when converting the number to Hebrew letters. By default, the "יה" and "יו" are replaced with "טו" and "טז" respectively.
    :return:
    """
    # Handle 0
    if number < 1:
        raise ValueError("Number must be greater than 0")

    result = ""

    # Prepare the numbers
    ones_value = _ones_column_value(number)
    if ones_value > 0:
        result += HEBREW_LETTER_TO_VALUE_MAPPINGS[ones_value]
    tens_value = _tens_column_value(number)
    if tens_value > 0:
        result += HEBREW_LETTER_TO_VALUE_MAPPINGS[tens_value]
    hundreds_value = _hundreds_and_above_column_value(number)
    if hundreds_value > 0:
        result += _hundreds_to_letters(hundreds_value)

    # Reverse the string
    result = result[::-1]

    # Substitute flags
    if substitution_flags:
        for flag in substitution_flags.flags:
            result = flag.sub(result)

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
    Returns the value of all columns of a number above the tens column.
    """
    return (number // 100) * 100


def _hundreds_to_letters(number: int) -> str:
    """
    Given a single digit number over 0 and a power of ten, return the Hebrew letters that represent that number.

    :param digit: The digit to convert to Hebrew letters. Must be greater than 0 and less than 10.
    :param powers_of_ten: The power of ten that the digit should be multiplied by.
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
