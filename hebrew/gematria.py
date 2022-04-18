from enum import Enum


class GematriaTypes(Enum):
    """
    Types of Gematria supported in this library.
    """

    MISPAR_HECHRACHI = "mispar_hechrachi"
    MISPAR_GADOL = "mispar_gadol"
    MISPAR_SIDURI = "mispar_siduri"


"""
A dictionary of values with each letter of the alphabet as a key, and the numerical value used in the mispar_hechrachi
gematria method as its value.
"""
MISPAR_HECHRACHI = {
    "א": 1,
    "ב": 2,
    "ג": 3,
    "ד": 4,
    "ה": 5,
    "ו": 6,
    "ז": 7,
    "ח": 8,
    "ט": 9,
    "י": 10,
    "כ": 20,
    "ך": 20,
    "ל": 30,
    "מ": 40,
    "ם": 40,
    "נ": 50,
    "ן": 50,
    "ס": 60,
    "ע": 70,
    "פ": 80,
    "ף": 80,
    "צ": 90,
    "ץ": 90,
    "ק": 100,
    "ר": 200,
    "ש": 300,
    "ת": 400,
}

"""
A dictionary of values with each letter of the alphabet as a key, and the numerical value used in the mispar_gadol
gematria method as its value. Non-final letter values are all the same, but final kaf/chaf, mem, nun, pe/fe are
moved to the end of the alphabet and continue on from where tav left off
"""
MISPAR_GADOL = {
    "א": 1,
    "ב": 2,
    "ג": 3,
    "ד": 4,
    "ה": 5,
    "ו": 6,
    "ז": 7,
    "ח": 8,
    "ט": 9,
    "י": 10,
    "כ": 20,
    "ך": 500,
    "ל": 30,
    "מ": 40,
    "ם": 600,
    "נ": 50,
    "ן": 700,
    "ס": 60,
    "ע": 70,
    "פ": 80,
    "ף": 800,
    "צ": 90,
    "ץ": 900,
    "ק": 100,
    "ר": 200,
    "ש": 300,
    "ת": 400,
}

"""
A dictionary of values with each letter of the alphabet as a key, and the numerical value used in the mispar_siduri
gematria method as its value. This method assigns each letter a number from 1 to 22 in the order of the alphabet.
"""
MISPAR_SIDURI = {
    "א": 1,
    "ב": 2,
    "ג": 3,
    "ד": 4,
    "ה": 5,
    "ו": 6,
    "ז": 7,
    "ח": 8,
    "ט": 9,
    "י": 10,
    "כ": 11,
    "ך": 23,
    "ל": 12,
    "מ": 13,
    "ם": 24,
    "נ": 14,
    "ן": 25,
    "ס": 15,
    "ע": 16,
    "פ": 17,
    "ף": 26,
    "צ": 18,
    "ץ": 27,
    "ק": 19,
    "ר": 20,
    "ש": 21,
    "ת": 22,
}
