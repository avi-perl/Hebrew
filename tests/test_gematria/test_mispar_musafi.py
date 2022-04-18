from hebrew import Hebrew
from hebrew.chars import HEBREW_CHARS
from hebrew.gematria import GematriaTypes


def test_mispar_musafi_type_value():
    assert GematriaTypes.MISPAR_MUSAFI.value == "mispar_musafi"


def test_mispar_musafi():
    assert Hebrew("בּ").gematria(GematriaTypes.MISPAR_MUSAFI) == 3
    assert Hebrew("ב").gematria(GematriaTypes.MISPAR_MUSAFI) == 3
    assert Hebrew("תורה").gematria(GematriaTypes.MISPAR_MUSAFI) == 615
    assert Hebrew("English" + "תורה").gematria(GematriaTypes.MISPAR_MUSAFI) == 615
    assert (
            Hebrew("אבגדהוזחטיכךלמםנןסעפףצץקרשת").gematria(GematriaTypes.MISPAR_MUSAFI)
            == 1802
    )


def test_mispar_musafi_pasuk():
    assert (
            Hebrew(
                "וְהָאָ֗רֶץ הָיְתָ֥ה תֹ֙הוּ֙ וָבֹ֔הוּ וְחֹ֖שֶׁךְ עַל־פְּנֵ֣י תְה֑וֹם וְר֣וּחַ אֱלֹהִ֔ים מְרַחֶ֖פֶת עַל־פְּנֵ֥י הַמָּֽיִם").gematria(
                GematriaTypes.MISPAR_MUSAFI)
            == 3598
    )