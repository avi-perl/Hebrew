def number_to_hebrew_string(
    number: int,
    punctuate: bool = True,
    geresh: bool = True,
) -> str:
    """
    Create a new instance of the Hebrew class representing a given number in its Hebrew letter form.

    :param number: The number to convert to Hebrew letters. Must be greater than 0.
    :param punctuate: Whether to add punctuation in the appropriate places.
    :param geresh: If punctuate is true, whether to use the unicode geresh or an apostrophe.
    :return:

    >>> Hebrew.from_number(1, punctuate=True, geresh=True)
    "א׳"
    >>> Hebrew.from_number(1, punctuate=False)
    "א"
    >>> Hebrew.from_number(1, punctuate=True, geresh=False)
    "'א"
    """
    # Handle 0
    if number < 1:
        raise ValueError("Number must be greater than 0")

    # Prepare the number
    number_str = str(number)
    number_str = number_str[
        ::-1
    ]  # Reverse the string, so that we are iterating over the digits from right to left

    # Iterate over the digits and convert them to Hebrew letters
    result = ""
    for i, digit in enumerate(number_str):
        if digit == "0":
            continue
        result += _digit_to_letters(int(digit), i)

    # Reverse the string again, so that it is in the correct order
    result = result[::-1]

    # Replace יה and יו with טו and טז
    result = result.replace("יה", "טו")
    result = result.replace("יו", "טז")

    # Add Punctuation
    if punctuate:
        if len(result) > 1:
            punctuation = "״" if geresh else '"'
            result = result[:-1] + punctuation + result[-1]
        else:
            punctuation = "׳" if geresh else "'"
            result += punctuation

    return result


def _digit_to_letters(digit: int, power_of_ten: int) -> str:
    """
    Given a single digit number over 0 and a power of ten, return the Hebrew letters that represent that number.

    :param digit: The digit to convert to Hebrew letters. Must be greater than 0 and less than 10.
    :param powers_of_ten: The power of ten that the digit should be multiplied by.
    :return: The Hebrew letters that represent the number.

    >>> _letters_for_number(1, 0)
    "א"
    >>> _letters_for_number(1, 1)
    "י"
    >>> _letters_for_number(1, 2)
    "ק"
    >>> _letters_for_number(1, 3)
    "תתר"
    """
    # Calculate the number
    number = digit * pow(10, power_of_ten)

    # Check if the number maps directly to a letter
    if number in _HEBREW_LETTER_TO_VALUE_MAPPINGS:
        return _HEBREW_LETTER_TO_VALUE_MAPPINGS[number]
    else:
        # Get the largest letter and letter value that is less than the number
        max_letter_value = next(
            i for i in _STANDARD_HEBREW_LETTERS_VALUES_REVERSED if i < number
        )
        max_letter = _HEBREW_LETTER_TO_VALUE_MAPPINGS[max_letter_value]

        # Calculate the number of times the letter goes into the number
        letter_count, remainder = divmod(number, max_letter_value)

        # If the remainder is 0, we can just return the letter times the letter count
        if remainder == 0:
            return max_letter * letter_count
        else:
            # Otherwise we need to further break down the remainder
            remainder_letters = _digit_to_letters(remainder, 0)
            return remainder_letters + max_letter * letter_count


_STANDARD_HEBREW_LETTERS = [
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
    "כ",
    "ל",
    "מ",
    "נ",
    "ס",
    "ע",
    "פ",
    "צ",
    "ק",
    "ר",
    "ש",
    "ת",
]
"All the Hebrew letters that are used to represent numbers. Does not include final letters."

_STANDARD_HEBREW_LETTERS_VALUES = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100,
    200,
    300,
    400,
]
"Values of the standard Hebrew letters, in order."

_STANDARD_HEBREW_LETTERS_VALUES_REVERSED = _STANDARD_HEBREW_LETTERS_VALUES[::-1]
"Values of the standard Hebrew letters, in reverse order."

"Dictionary mapping standard Hebrew letters to their values."
_HEBREW_LETTER_TO_VALUE_MAPPINGS = dict(
    zip(_STANDARD_HEBREW_LETTERS_VALUES, _STANDARD_HEBREW_LETTERS)
)
"Dictionary mapping standard Hebrew letters to their values."
