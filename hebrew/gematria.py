from enum import Enum
from typing import Dict


class GematriaTypes(Enum):
    """
    Types of Gematria supported in this library.
    """

    # Simple methods where the value is calculated off of a value map to each letter
    MISPAR_HECHRACHI = "mispar_hechrachi"
    MISPAR_GADOL = "mispar_gadol"
    MISPAR_SIDURI = "mispar_siduri"
    MISPAR_KATAN = "mispar_katan"
    MISPAR_PERATI = "mispar_perati"
    ATBASH = "atbash"
    ALBAM = "albam"
    MISPAR_MESHULASH = "mispar_meshulash"
    MISPAR_KIDMI = "mispar_kidmi"
    MISPAR_MISPARI = "mispar_mispari"
    AYAK_BACHAR = "ayak_bachar"
    AYAK_BAKAR: str = AYAK_BACHAR  # type: ignore
    OFANIM = "ofanim"
    ACHAS_BETA = "achas_beta"
    AVGAD = "avgad"
    REVERSE_AVGAD = "reverse_avgad"

    # Complex methods involving logic on top of MISPAR_HECHRACHI
    MISPAR_MUSAFI = "mispar_musafi"
    MISPAR_BONEEH = "mispar_boneeh"
    MISPAR_HAMERUBAH_HAKLALI = "mispar_hamerubah_haklali"
    MISPAR_HAACHOR = "mispar_haachor"
    MISPAR_KATAN_MISPARI = "mispar_katan_mispari"
    MISPAR_KOLEL = "mispar_kolel"
    MISPAR_SHEMI_MILUI = "mispar_shemi_milui"
    MISPAR_NEELAM = "mispar_neelam"


"""
A dictionary of values with each letter of the alphabet as a key, and the numerical value used in the mispar_hechrachi
gematria method as its value.
"""
MISPAR_HECHRACHI: Dict[str, int] = {
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
MISPAR_GADOL: Dict[str, int] = {
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
MISPAR_SIDURI: Dict[str, int] = {
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
MISPAR_KATAN: Dict[str, int] = {
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
MISPAR_PERATI: Dict[str, int] = {
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
ATBASH: Dict[str, int] = {
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
ALBAM: Dict[str, int] = {
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
MISPAR_MESHULASH: Dict[str, int] = {
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

"""
A dictionary of values with each letter of the alphabet as a key, and the numerical value used in the Mispar Kidmi
gematria method as its value. This method adds the value of all preceding letters in the alphabet to each 
letter's value. (ex. "Aleph" = 1, "Beis" = 1 + 2 = 3, "Gimmel" = 1 + 2 + 3 = 6).
"""
MISPAR_KIDMI: Dict[str, int] = {
    "א": 1,
    "ב": 3,
    "ג": 6,
    "ד": 10,
    "ה": 15,
    "ו": 21,
    "ז": 28,
    "ח": 36,
    "ט": 45,
    "י": 55,
    "כ": 75,
    "ך": 75,
    "ל": 105,
    "מ": 145,
    "ם": 145,
    "נ": 195,
    "ן": 195,
    "ס": 255,
    "ע": 325,
    "פ": 405,
    "ף": 405,
    "צ": 495,
    "ץ": 495,
    "ק": 595,
    "ר": 795,
    "ש": 1095,
    "ת": 1495,
}

"""
A dictionary of values with each letter of the alphabet as a key, and the numerical value used in the Mispar Mispari
gematria method as its value. This method spells out the Hebrew name of each of the letter's standard values and adds 
up their values. (ex. "Aleph" = one (Echad) = 1 + 8 + 4 = 13).
"""
MISPAR_MISPARI: Dict[str, int] = {
    "א": 13,
    "ב": 760,
    "ג": 636,
    "ד": 273,
    "ה": 348,
    "ו": 600,
    "ז": 372,
    "ח": 401,
    "ט": 770,
    "י": 570,
    "כ": 620,
    "ך": 620,
    "ל": 686,
    "מ": 323,
    "ם": 323,
    "נ": 408,
    "ן": 408,
    "ס": 660,
    "ע": 422,
    "פ": 446,
    "ף": 446,
    "צ": 820,
    "ץ": 820,
    "ק": 46,
    "ר": 501,
    "ש": 1083,
    "ת": 720,
}

"""
A dictionary of values with each letter of the alphabet as a key, and the numerical value used in the Ayak Bachar 
(or Ayak Bakar) gematria method as its value. This method splits the alphabet into three groups of nine with the final 
(sofit) letters at the end. The letters in the first group replace the ones in the second group, the letters in the 
second group replace the ones in the third group, and the letters in the third group replace the ones in 
the first group. (ex. "Aleph" takes the place of "Yud", "Yud" takes the place of "Kuf", 
"Kuf" takes the place of "Aleph", "Beis" takes the place of "Chaf" etc.).
"""
AYAK_BACHAR: Dict[str, int] = {
    "א": 10,
    "ב": 20,
    "ג": 30,
    "ד": 40,
    "ה": 50,
    "ו": 60,
    "ז": 70,
    "ח": 80,
    "ט": 90,
    "י": 100,
    "כ": 200,
    "ך": 5,
    "ל": 300,
    "מ": 400,
    "ם": 6,
    "נ": 500,
    "ן": 7,
    "ס": 600,
    "ע": 700,
    "פ": 800,
    "ף": 8,
    "צ": 900,
    "ץ": 9,
    "ק": 1,
    "ר": 2,
    "ש": 3,
    "ת": 4,
}

"""
A dictionary of values with each letter of the alphabet as a key, and the numerical value used in the Ofanim 
gematria method as its value. This method replaces each letter with the last letter of its name. (ex. "Aleph" becomes 
"Fey", "Beis" becomes "Tav").
"""
OFANIM: Dict[str, int] = {
    "א": 80,
    "ב": 400,
    "ג": 30,
    "ד": 400,
    "ה": 1,
    "ו": 6,
    "ז": 50,
    "ח": 400,
    "ט": 400,
    "י": 4,
    "כ": 80,
    "ך": 80,
    "ל": 4,
    "מ": 40,
    "ם": 40,
    "נ": 50,
    "ן": 50,
    "ס": 20,
    "ע": 50,
    "פ": 1,
    "ף": 1,
    "צ": 10,
    "ץ": 10,
    "ק": 80,
    "ר": 300,
    "ש": 50,
    "ת": 6,
}

"""
A dictionary of values with each letter of the alphabet as a key, and the numerical value used in the Ofanim 
gematria method as its value. This method splits the alphabet into groups of 7, 7, and 8 letters. 
The letters in the first group replace the ones in the second group, the letters in the second group replace 
the ones in the third group, and the letters in the third group replace the ones in the first group. The letter "Tav" 
does not change.
"""
ACHAS_BETA: Dict[str, int] = {
    "א": 8,
    "ב": 9,
    "ג": 10,
    "ד": 20,
    "ה": 30,
    "ו": 40,
    "ז": 50,
    "ח": 60,
    "ט": 70,
    "י": 80,
    "כ": 90,
    "ך": 90,
    "ל": 100,
    "מ": 200,
    "ם": 200,
    "נ": 300,
    "ן": 300,
    "ס": 1,
    "ע": 2,
    "פ": 3,
    "ף": 3,
    "צ": 4,
    "ץ": 4,
    "ק": 5,
    "ר": 6,
    "ש": 7,
    "ת": 400,
}

"""
A dictionary of values with each letter of the alphabet as a key, and the numerical value used in the Avgad  
gematria method as its value. This method replaces each letter with the next one. (ex. "Aleph" becomes "Beis", "Beis" 
becomes "Gimmel", "Tav" becomes "Aleph").
"""
AVGAD: Dict[str, int] = {
    "א": 2,
    "ב": 3,
    "ג": 4,
    "ד": 5,
    "ה": 6,
    "ו": 7,
    "ז": 8,
    "ח": 9,
    "ט": 10,
    "י": 20,
    "כ": 30,
    "ך": 30,
    "ל": 40,
    "מ": 50,
    "ם": 50,
    "נ": 60,
    "ן": 60,
    "ס": 70,
    "ע": 80,
    "פ": 90,
    "ף": 90,
    "צ": 100,
    "ץ": 100,
    "ק": 200,
    "ר": 300,
    "ש": 400,
    "ת": 1,
}

"""
A dictionary of values with each letter of the alphabet as a key, and the numerical value used in the Reverse Avgad  
gematria method as its value. This method replaces each letter with the previous one. (ex. "Beis" becomes "Aleph", 
"Gimmel" becomes "Beis", "Aleph" becomes "Tav").
"""
REVERSE_AVGAD: Dict[str, int] = {
    "א": 400,
    "ב": 1,
    "ג": 2,
    "ד": 3,
    "ה": 4,
    "ו": 5,
    "ז": 6,
    "ח": 7,
    "ט": 8,
    "י": 9,
    "כ": 10,
    "ך": 10,
    "ל": 20,
    "מ": 30,
    "ם": 30,
    "נ": 40,
    "ן": 40,
    "ס": 50,
    "ע": 60,
    "פ": 70,
    "ף": 70,
    "צ": 80,
    "ץ": 80,
    "ק": 90,
    "ר": 100,
    "ש": 200,
    "ת": 300,
}
