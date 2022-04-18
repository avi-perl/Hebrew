from enum import Enum


class GematriaTypes(Enum):
    """
    Types of Gematria supported in this library.
    """

    MISPAR_HECHRACHI = "mispar_hechrachi"
    MISPAR_GADOL = "mispar_gadol"
    MISPAR_SIDURI = "mispar_siduri"
    MISPAR_KATAN = "mispar_katan"
    MISPAR_PERATI = "mispar_perati"
    ATBASH = "atbash"
    ALBAM = "albam"
    MISPAR_MESHULASH = "mispar_meshulash"

    MISPAR_MUSAFI = "mispar_musafi"


"""
List of Gematria methods that can be calculated by simply adding each letters value
up to a final number. 
"""
SIMPLE_GEMATRIA_METHODS = [
    GematriaTypes.MISPAR_HECHRACHI,
    GematriaTypes.MISPAR_GADOL,
    GematriaTypes.MISPAR_SIDURI,
    GematriaTypes.MISPAR_KATAN,
    GematriaTypes.MISPAR_PERATI,
    GematriaTypes.ATBASH,
    GematriaTypes.ALBAM,
    GematriaTypes.MISPAR_MESHULASH,
]

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

"""
A dictionary of values with each letter of the alphabet as a key, and the numerical value used in the mispar_katan
gematria method as its value. This method uses the value of the letters but without the zeros after large numbers. 
(ex. "Yud" is 1 instead of 10, "Tav" is 4 instead of 400).
"""
MISPAR_KATAN = {
    "א": 1,
    "ב": 2,
    "ג": 3,
    "ד": 4,
    "ה": 5,
    "ו": 6,
    "ז": 7,
    "ח": 8,
    "ט": 9,
    "י": 1,
    "כ": 2,
    "ך": 2,
    "ל": 3,
    "מ": 4,
    "ם": 4,
    "נ": 5,
    "ן": 5,
    "ס": 6,
    "ע": 7,
    "פ": 8,
    "ף": 8,
    "צ": 9,
    "ץ": 9,
    "ק": 1,
    "ר": 2,
    "ש": 3,
    "ת": 4,
}

"""
A dictionary of values with each letter of the alphabet as a key, and the numerical value used in the mispar_perati
gematria method as its value. This method assigns each letter its standard value squared. (ex. "Aleph" = 1 x 1 = 1, "Beis" = 2 x 2 = 4).
"""
MISPAR_PERATI = {
    "א": 1,
    "ב": 4,
    "ג": 9,
    "ד": 16,
    "ה": 25,
    "ו": 36,
    "ז": 49,
    "ח": 64,
    "ט": 81,
    "י": 100,
    "כ": 400,
    "ך": 400,
    "ל": 900,
    "מ": 1_600,
    "ם": 1_600,
    "נ": 2_500,
    "ן": 2_500,
    "ס": 3_600,
    "ע": 4_900,
    "פ": 6_400,
    "ף": 6_400,
    "צ": 8_100,
    "ץ": 8_100,
    "ק": 10_000,
    "ר": 40_000,
    "ש": 90_000,
    "ת": 160_000,
}

"""
A dictionary of values with each letter of the alphabet as a key, and the numerical value used in the AtBash
gematria method as its value. This method exchanges each letter's value for its opposite letter's value. 
(ex. "Aleph" switches values with "Tav", "Beis" switches values with "Shin").
"""
ATBASH = {
    "א": 400,
    "ב": 300,
    "ג": 200,
    "ד": 100,
    "ה": 90,
    "ו": 80,
    "ז": 70,
    "ח": 60,
    "ט": 50,
    "י": 40,
    "כ": 30,
    "ך": 30,
    "ל": 20,
    "מ": 10,
    "ם": 10,
    "נ": 9,
    "ן": 9,
    "ס": 8,
    "ע": 7,
    "פ": 6,
    "ף": 6,
    "צ": 5,
    "ץ": 5,
    "ק": 4,
    "ר": 3,
    "ש": 2,
    "ת": 1,
}

"""
A dictionary of values with each letter of the alphabet as a key, and the numerical value used in the AlBam
gematria method as its value. This method splits the alphabet in half and letters from the first half switch 
values with letters from the second half. (ex. "Aleph" switches values with "Lamed", "Beis" switches values with "Mem").
"""
ALBAM = {
    "א": 30,
    "ב": 40,
    "ג": 50,
    "ד": 60,
    "ה": 70,
    "ו": 80,
    "ז": 90,
    "ח": 100,
    "ט": 200,
    "י": 300,
    "כ": 400,
    "ך": 400,
    "ל": 1,
    "מ": 2,
    "ם": 2,
    "נ": 3,
    "ן": 3,
    "ס": 4,
    "ע": 5,
    "פ": 6,
    "ף": 6,
    "צ": 7,
    "ץ": 7,
    "ק": 8,
    "ר": 9,
    "ש": 10,
    "ת": 20,
}

"""
A dictionary of values with each letter of the alphabet as a key, and the numerical value used in the AtBash
gematria method as its value. This method splits the alphabet in half and letters from the first half switch 
values with letters from the second half. (ex. "Aleph" switches values with "Lamed", "Beis" switches values with "Mem").
"""
MISPAR_MESHULASH = {
    "א": 1,
    "ב": 8,
    "ג": 27,
    "ד": 64,
    "ה": 125,
    "ו": 216,
    "ז": 343,
    "ח": 512,
    "ט": 729,
    "י": 1_000,
    "כ": 8_000,
    "ך": 8_000,
    "ל": 27_000,
    "מ": 64_000,
    "ם": 64_000,
    "נ": 125_000,
    "ן": 125_000,
    "ס": 216_000,
    "ע": 343_000,
    "פ": 512_000,
    "ף": 512_000,
    "צ": 729_000,
    "ץ": 729_000,
    "ק": 1_000_000,
    "ר": 8_000_000,
    "ש": 27_000_000,
    "ת": 64_000_000,
}
