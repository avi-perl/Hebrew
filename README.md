<h1 align="center" style="font-family:'Courier New'">Hebrew("בְּרֵאשִׁ֖ית")</h1>
<p align="center">
    <em>A python package with methods to handle the complexities of Hebrew text.</em>
</p>
<p align="center">
<a href="https://pypi.org/project/hebrew/" target="_blank">
    <img src="https://badge.fury.io/py/hebrew.svg" alt="PyPI version">
</a>
<a href="https://badge.fury.io/py/hebrew">
    <img src="https://img.shields.io/pypi/pyversions/hebrew" alt="Supported Python Versions">
</a>
<a href="https://github.com/avi-perl/hebrew/actions/workflows/test.yml" target="_blank">
    <img src="https://github.com/avi-perl/hebrew/actions/workflows/test.yml/badge.svg" alt="Test">
</a>
<a href="https://codecov.io/gh/avi-perl/hebrew" target="_blank">
  <img src="https://codecov.io/gh/avi-perl/Hebrew/branch/master/graph/badge.svg?token=0DA1R9IY6S"/>
</a>
󠀠󠀠
<a href="https://twitter.com/__aviperl__" target="_blank">
    <img src="https://badgen.net/badge/icon/twitter?icon=twitter&label=Chat%20with%20me" alt="Twitter">
</a>
</p>

---

**Documentation**: [https://avi-perl.github.io/Hebrew/](https://avi-perl.github.io/Hebrew/)

---

# Installation
```bash
$ pip install hebrew
```

# Example

`Hebrew` assists in working with Hebrew text by providing methods to handle the text according to user-perceived
characteristics. Additionally, methods for common Hebrew text processing are provided.

```python
>>> from hebrew import Hebrew
>>> from hebrew.chars import HebrewChar, ALEPH

>>> hs = Hebrew('בְּרֵאשִׁ֖ית')
>>> list(hs.graphemes)
['בְּ', 'רֵ', 'א', 'שִׁ֖', 'י', 'ת']
>>> hs.text_only()
בראשית

>>> ALEPH
HebrewChar(char='א', name='Aleph', hebrew_name='אָלֶף', name_alts=['Alef'], hebrew_name_alts=None, final_letter=False)

>>> HebrewChar.search('bet')
HebrewChar(char='בּ', name='Bet', hebrew_name='בֵּית', name_alts=None, hebrew_name_alts=None, final_letter=False)
```

## Grapheme Characters
Hebrew text comes in different forms, depending on the context. Hebrew text may appear with Niqqudot 
"a system of diacritical signs used to represent vowels or distinguish between alternative pronunciations of letters 
of the Hebrew alphabet". [^1] Additionally, Hebrew text may appear with extensive punctuation characters that connect 
words, separate them, and cantillation marks "used as a guide for chanting the text, either from the printed text or, 
in the case of the public reading of the Torah" [^2].   

Because of the above, from the perspective of a hebrew reader, the following 3 words are the same:
1. **בְּרֵאשִׁ֖ית**
2. **בְּרֵאשִׁית**
3. **בראשית**

However, as a unicode string, they are entirely different because of the additional characters.
```python
>>> len("בְּרֵאשִׁ֖ית")  # 1
12
>>> len("בְּרֵאשִׁית")  # 2
11
>>> len("בראשית")  # 3
6  
```
This impacts the user is a number of other ways. For example, if I want to get the root of this hebrew word using a slice:
_Expected: `רֵאשִׁ֖ית`_
```python
>>> he = "בְּרֵאשִׁ֖ית"
>>> he[-5:]
'ִׁ֖ית'
```
The solution to this is to handle the unicode string as a list of grapheme[^3] characters, where each letter and its 
accompanying characters are treated as a single unit. 

### Working with Grapheme Characters
Using the [grapheme](https://github.com/alvinlindstam/grapheme) library for python, we can work with the grapheme 
characters as units. This allows us to get the right number of characters, slice the string correctly, and more.
```python
>>> import grapheme
>>> grapheme.length("בְּרֵאשִׁ֖ית")
6
>>> grapheme.slice("בְּרֵאשִׁ֖ית", start=1, end=6)
'רֵאשִׁ֖ית'
```
This library includes 2 classes. `GraphemeString` is a class that supports all the functions made available by `grapheme`.
The 2nd class `Hebrew` subclasses `GraphemeString` and adds methods for handling Hebrew text. This allows us to 
interact with the text like so:
```python
>>> from hebrew import Hebrew

>>> v2 = Hebrew("וְהָאָ֗רֶץ הָיְתָ֥ה תֹ֙הוּ֙ וָבֹ֔הוּ וְחֹ֖שֶׁךְ עַל־פְּנֵ֣י תְה֑וֹם וְר֣וּחַ אֱלֹהִ֔ים מְרַחֶ֖פֶת עַל־פְּנֵ֥י הַמָּֽיִם׃")
>>> v2.no_punctuation()
וְהָאָרֶץ הָיְתָה תֹהוּ וָבֹהוּ וְחֹשֶׁךְ עַל־פְּנֵי תְהוֹם וְרוּחַ אֱלֹהִים מְרַחֶפֶת עַל־פְּנֵי הַמָּיִם׃

>>> v2.text_only()
והארץ היתה תהו ובהו וחשך על־פני תהום ורוח אלהים מרחפת על־פני המים

>>> v2.length
35
>>> v2.words(split_maqaf=True)
[וְהָאָ֗רֶץ, הָיְתָ֥ה, תֹ֙הוּ֙, וָבֹ֔הוּ, וְחֹ֖שֶׁךְ, עַל, פְּנֵ֣י, תְה֑וֹם, וְר֣וּחַ, אֱלֹהִ֔ים, מְרַחֶ֖פֶת, עַל, פְּנֵ֥י, הַמָּֽיִם׃]
```

The text in these examples and used in testing were sourced from [Sefaria](https://github.com/Sefaria/Sefaria-Export).

## `hebrew.chars` and Character Constants
`hebrew.Chars` contains constants for every letter as well as lists by character category's.
Each value is an instance of a class that represents a character in the Hebrew character set with relevant properties. 
Since this library seeks to support the use of the Hebrew language in the way it is used, characters such as "בּ" can be
located (`BET`) even though, strictly speaking, "בּ" is not part of the hebrew alphabet; it is a Hebrew letter plus a dot.
```python
>>> from hebrew.chars import FINAL_LETTERS, YIDDISH_CHARS, TSADI

>>> TSADI
HebrewChar(char='צ', name='Tsadi', hebrew_name='צַדִי', name_alts=['Tzadik'], hebrew_name_alts=['צדיק'], final_letter=False)

>>> {c.name: c.char for c in FINAL_LETTERS}
{'Chaf Sofit': 'ך', 'Mem Sofit': 'ם', 'Nun Sofit': 'ן', 'Fe Sofit': 'ף', 'Tsadi Sofit': 'ץ'}

>>> [c.char for c in YIDDISH_CHARS]
['ײ', 'װ', 'ױ']
```
A letter can be retrieved using the `CHARS` dict; A dict of all instances of all supported Char types where the key is 
the char and the value is an instance of BaseHebrewChar. 
```python
>>> from hebrew.chars import CHARS

>>> CHARS.get('בּ')
HebrewChar(char='בּ', name='Bet', hebrew_name='בֵּית', name_alts=None, hebrew_name_alts=None, final_letter=False)
```
Search is also supported so that letters can be retrieved by their name.
```python
>>> from hebrew.chars import HebrewChar

>>> HebrewChar.search('bet')
HebrewChar(char='בּ', name='Bet', hebrew_name='בֵּית', name_alts=None, hebrew_name_alts=None, final_letter=False)
```

## Contributing 
Contributions in the form of pull requests are very welcome! I'm sure many more helpful methods related to hebrew text 
could be helpful. More information and instructions for contributing can be found [here](CONTRIBUTING).

[^1]: [https://en.wikipedia.org/wiki/Niqqud](https://en.wikipedia.org/wiki/Niqqud)
[^2]: [https://en.wikipedia.org/wiki/Hebrew_cantillation](https://en.wikipedia.org/wiki/Hebrew_cantillation)
[^3]: [https://en.wikipedia.org/wiki/Grapheme](https://en.wikipedia.org/wiki/Grapheme)