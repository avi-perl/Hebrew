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

STANDARD_HEBREW_LETTERS_VALUES_REVERSED = _STANDARD_HEBREW_LETTERS_VALUES[::-1]
"Values of the standard Hebrew letters, in reverse order."

"Dictionary mapping standard Hebrew letters to their values."
HEBREW_LETTER_TO_VALUE_MAPPINGS = dict(
    zip(_STANDARD_HEBREW_LETTERS_VALUES, _STANDARD_HEBREW_LETTERS)
)
"Dictionary mapping standard Hebrew letters to their values."
