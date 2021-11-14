from enum import Enum


class GematriaTypes(Enum):
    """
    Types of Gematria supported in this library.
    """

    MISPAR_HECHRACHI = "mispar_hechrachi"


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
A dictionary of values with each letter of the alphabet as a key, and the numerical value used in the mispar_hechrachi
gematria method as its value.
"""
