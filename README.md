# `בְּרֵאשִׁ֖ית == בְּרֵאשִׁית == בראשית`

[![Test](https://github.com/avi-perl/HebrewString/actions/workflows/test.yml/badge.svg)](https://github.com/avi-perl/HebrewString/actions/workflows/test.yml)

`HebrewString` assists in working with Hebrew text by providing methods to handle the text according to user-perceived
characteristics. Additionally, methods for common Hebrew text processing are provided.


```python
>>> from HebrewString import HebrewString
>>>
>>> v2 = HebrewString("וְהָאָ֗רֶץ הָיְתָ֥ה תֹ֙הוּ֙ וָבֹ֔הוּ וְחֹ֖שֶׁךְ עַל־פְּנֵ֣י תְה֑וֹם וְר֣וּחַ אֱלֹהִ֔ים מְרַחֶ֖פֶת עַל־פְּנֵ֥י הַמָּֽיִם׃")
>>>
>>> v2.no_punctuation()
וְהָאָרֶץ הָיְתָה תֹהוּ וָבֹהוּ וְחֹשֶׁךְ עַל־פְּנֵי תְהוֹם וְרוּחַ אֱלֹהִים מְרַחֶפֶת עַל־פְּנֵי הַמָּיִם׃
>>>
>>> v2.text_only()
והארץ היתה תהו ובהו וחשך על־פני תהום ורוח אלהים מרחפת על־פני המים
>>>
>>> v2.length
35
>>> v2.words(split_maqaf=True)
[וְהָאָ֗רֶץ, הָיְתָ֥ה, תֹ֙הוּ֙, וָבֹ֔הוּ, וְחֹ֖שֶׁךְ, עַל, פְּנֵ֣י, תְה֑וֹם, וְר֣וּחַ, אֱלֹהִ֔ים, מְרַחֶ֖פֶת, עַל, פְּנֵ֥י, הַמָּֽיִם׃]
```

## Grapheme Characters
Hebrew text comes in different forms, depending on the context. Hebrew text may appear with Niqqudot 
"a system of diacritical signs used to represent vowels or distinguish between alternative pronunciations of letters 
of the Hebrew alphabet". [^1] Additionally, Hebrew text may appear with extensive punctuation characters that connect 
words, separate them, and cantillation marks "used as a guide for chanting the text, either from the printed text or, 
in the case of the public reading of the Torah" [^2].   

Because of the above, from the perspective of a hebrew reader, the following 3 words are the same:
1. בְּרֵאשִׁ֖ית
2. בְּרֵאשִׁית
3. בראשית

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
The 2nd class `HebrewString` subclasses `GraphemeString` and adds methods for handling Hebrew text. This allows us to 
interact with the text like so:
```python
>>> from HebrewString import HebrewString
>>>
>>> v2 = HebrewString("וְהָאָ֗רֶץ הָיְתָ֥ה תֹ֙הוּ֙ וָבֹ֔הוּ וְחֹ֖שֶׁךְ עַל־פְּנֵ֣י תְה֑וֹם וְר֣וּחַ אֱלֹהִ֔ים מְרַחֶ֖פֶת עַל־פְּנֵ֥י הַמָּֽיִם׃")
>>>
>>> v2.no_punctuation()
וְהָאָרֶץ הָיְתָה תֹהוּ וָבֹהוּ וְחֹשֶׁךְ עַל־פְּנֵי תְהוֹם וְרוּחַ אֱלֹהִים מְרַחֶפֶת עַל־פְּנֵי הַמָּיִם׃
>>>
>>> v2.text_only()
והארץ היתה תהו ובהו וחשך על־פני תהום ורוח אלהים מרחפת על־פני המים
>>>
>>> v2.length
35
>>> v2.words(split_maqaf=True)
[וְהָאָ֗רֶץ, הָיְתָ֥ה, תֹ֙הוּ֙, וָבֹ֔הוּ, וְחֹ֖שֶׁךְ, עַל, פְּנֵ֣י, תְה֑וֹם, וְר֣וּחַ, אֱלֹהִ֔ים, מְרַחֶ֖פֶת, עַל, פְּנֵ֥י, הַמָּֽיִם׃]
```

The text in these examples and used in testing were sourced from [Sefaria](https://github.com/Sefaria/Sefaria-Export).

## Contributing 
Contributions in the form of pull requests are very welcome! I'm sure many more helpful methods related to hebrew text 
could be helpful.

[^1]: [https://en.wikipedia.org/wiki/Niqqud](https://en.wikipedia.org/wiki/Niqqud)
[^2]: [https://en.wikipedia.org/wiki/Hebrew_cantillation](https://en.wikipedia.org/wiki/Hebrew_cantillation)
[^3]: [https://en.wikipedia.org/wiki/Grapheme](https://en.wikipedia.org/wiki/Grapheme)