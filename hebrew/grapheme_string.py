from typing import Iterator, TypeVar, Optional

import grapheme
from grapheme.finder import GraphemeIterator

GraphemeStringT = TypeVar("GraphemeStringT", bound="GraphemeString")


class GraphemeString:
    """
    An object that unifies the functions available from the grapheme library under an object.
    Functions all work as they do in the grapheme library, this is simply an interface.
    """

    UNICODE_VERSION: str = grapheme.UNICODE_VERSION

    def __init__(self, string: str):
        self.string = string

    @property
    def graphemes(self) -> GraphemeIterator:
        """
        Returns an iterator of all graphemes of given string.

        ``` python
        >>> rainbow_flag = "🏳️‍🌈"
        >>> [codepoint for codepoint in rainbow_flag]
        ['🏳', '️', '\u200d', '🌈']
        >>> list(GraphemeString("multi codepoint grapheme: " + rainbow_flag).graphemes)
        ['m', 'u', 'l', 't', 'i', ' ', 'c', 'o', 'd', 'e', 'p', 'o', 'i', 'n', 't', ' ', 'g', 'r', 'a', 'p', 'h', 'e', 'm', 'e', ':', ' ', '🏳️‍🌈']
        ```
        """
        return grapheme.graphemes(self.string)

    @property
    def length(self) -> int:
        """
        Returns the number of graphemes in the string.

        Note that this functions needs to traverse the full string to calculate the length,
        unlike `len(string)` and it's time consumption is linear to the length of the string
        (up to the `until` value).

        Only counts up to the `until` argument, if given. This is useful when testing
        the length of a string against some limit and the excess length is not interesting.

        ``` python
        >>> rainbow_flag = "🏳️‍🌈"
        >>> len(rainbow_flag)
        4
        >>> GraphemeString(rainbow_flag).length
        1
        ```
        """
        return grapheme.length(self.string)

    def get_length(self, until: int) -> int:
        """
        Returns the number of graphemes in the string.

        Note that this functions needs to traverse the full string to calculate the length,
        unlike `len(string)` and it's time consumption is linear to the length of the string
        (up to the `until` value).

        Only counts up to the `until` argument, if given. This is useful when testing
        the length of a string against some limit and the excess length is not interesting.

        ``` python
        >>> rainbow_flag = "🏳️‍🌈"
        >>> len(rainbow_flag)
        4
        >>> GraphemeString(rainbow_flag).length
        1
        >>> GraphemeString("".join(str(i) for i in range(100))).get_length(30)
        30
        ```
        """
        return grapheme.length(self.string, until)

    @property
    def grapheme_lengths(self) -> Iterator[int]:
        """
        Returns an iterator of number of code points in each grapheme of the string.
        """
        return grapheme.grapheme_lengths(self.string)

    def slice(self, start: Optional[int] = None, end: Optional[int] = None) -> str:
        """
        Returns a substring of the given string, counting graphemes instead of codepoints.

        Negative indices is currently not supported.

        ``` python
        >>> string = "tamil நி (ni)"

        >>> string[:7]
        'tamil ந'
        >>> GraphemeString(string).slice(end=7)
        'tamil நி'
        >>> string[7:]
        'ி (ni)'
        >>> GraphemeString(string).slice(start=7)
        ' (ni)'
        ```
        """
        return grapheme.slice(self.string, start, end)

    def contains(self, substring: str) -> bool:
        """
        Returns true if the sequence of graphemes in substring is also present in string.

        This differs from the normal python `in` operator, since the python operator will return
        true if the sequence of codepoints are withing the other string without considering
        grapheme boundaries.

        Performance notes: Very fast if `substring not in string`, since that also means that
        the same graphemes can not be in the two strings. Otherwise this function has linear time
        complexity in relation to the string length. It will traverse the sequence of graphemes until
        a match is found, so it will generally perform better for grapheme sequences that match early.

        ``` python
        >>> "🇸🇪" in "🇪🇸🇪🇪"
        True
        >>> GraphemeString("🇪🇸🇪🇪").contains("🇸🇪")
        False
        ```
        """
        return grapheme.contains(self.string, substring)

    def safe_split_index(self, max_length: int) -> int:
        """
        Returns the highest index up to `max_len` at which the given string can be sliced, without breaking a grapheme.

        This is useful for when you want to split or take a substring from a string, and don't really care about
        the exact grapheme length, but don't want to risk breaking existing graphemes.

        This function does normally not traverse the full grapheme sequence up to the given length, so it can be used
        for arbitrarily long strings and high `max_len`s. However, some grapheme boundaries depend on the previous state,
        so the worst case performance is O(n). In practice, it's only very long non-broken sequences of country flags
        (represented as Regional Indicators) that will perform badly.

        The return value will always be between `0` and `len(string)`.

        ``` python
        >>> string = "tamil நி (ni)"
        >>> i = GraphemeString(string).safe_split_index(7)
        >>> i
        6
        >>> string[:i]
        'tamil '
        >>> string[i:]
        'நி (ni)'
        ```
        """
        return grapheme.safe_split_index(self.string, max_length)

    def startswith(self, prefix: str) -> bool:
        """
        Like str.startswith, but also checks that the string starts with the given prefixes sequence of graphemes.

        str.startswith may return true for a prefix that is not visually represented as a prefix if a grapheme cluster
        is continued after the prefix ends.

        ``` python
        >>> GraphemeString("✊🏾").startswith("✊")
        False
        >>> "✊🏾".startswith("✊")
        True
        ```
        """
        return grapheme.startswith(self.string, prefix)

    def endswith(self, suffix: str) -> bool:
        """
        Like str.endswith, but also checks that the string ends with the given prefixes sequence of graphemes.

        str.endswith may return true for a suffix that is not visually represented as a suffix if a grapheme cluster
        is initiated before the suffix starts.

        ``` python
        >>> GraphemeString("🏳️‍🌈").endswith("🌈")
        False
        >>> "🏳️‍🌈".endswith("🌈")
        True
        ```
        """
        return grapheme.endswith(self.string, suffix)

    def __str__(self) -> str:
        return self.string

    def __repr__(self) -> str:
        return self.__str__()

    def __add__(self: GraphemeStringT, other: GraphemeStringT) -> GraphemeStringT:
        return self.__class__(self.string + str(other))

    def __key(self) -> str:
        return self.string

    def __eq__(self, other) -> bool:
        if isinstance(other, GraphemeString):
            return self.__key() == other.__key()
        return False

    def __hash__(self):
        return hash(self.__key())
