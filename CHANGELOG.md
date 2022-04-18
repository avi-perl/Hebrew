# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.8] - 2022-04-18

### Added

- Added Gematria methods `MISPAR_MUSAFI`. This is the first of the complex Gematria types that goes deeper than just 
adding up values assigned to each letter, necessitating internal changes to the `Hebrew` class.

## [0.5.7] - 2022-04-18

### Added

- Added Gematria methods `MISPAR_KATAN`, `MISPAR_PERATI`, `ATBASH`, `ALBAM`, `MISPAR_MESHULASH`.

## [0.5.6] - 2022-04-18

### Added

- Added a new gematria method, `MISPAR_SIDURI`.

## [0.5.5] - 2021-11-22

### Added

- Added a new gematria method, `MISPAR_GADOL`. A contribution by [Taber Andrew Bain](https://github.com/taber)

## [0.5.4] - 2021-11-21

### Fixed

- Fixed an issue where `Hebrew.gematria` would through an error if the input string had no hebrew characters.
  In this case, we now return a value of 0.

## [0.5.3] - 2021-11-15

### Changed

- Split the `PunctuationChar` type chars into `TaamimChar` and `OtherChar` types in `hebrew.char`.
- Renamed the `no_punctuation` method of `Hebrew` to `no_taamim`.

## [0.5.0] - 2021-11-14

### Added

- Added the method `Hebrew.gematria` method for calculating the gematria of a string.
- Added `mispar_hechrachi` as a supported gematria type.

``` python
>>> from hebrew import Hebrew
>>> from hebrew.gematria import GematriaTypes

>>> Hebrew("בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָרֶץ׃").gematria(GematriaTypes.MISPAR_HECHRACHI)
2701
```

## [0.4.0] - 2021-11-14

### Added

- Added `hebrew.chars` with constants for Hebrew characters and classes to represent each letter.
- Moved constants out of `Hebrew` and into `hebrew.chars`.
- Constant values, previously strings, are now instances of a class with metadata for each letter.

### Removed

- Support for Python 3.6 was removed because we are now using `@dataclasse`. It is possible to make this work with
  3.6 but I am choosing not to at this time. If this is a problem for you, feel free to open an issue.

## [0.3.0] - 2021-11-08

### Changed

- Renamed the python package from `hebrewstring` to `hebrew`.

## [0.2.0] - 2021-11-07

### Added

- Added the `__eq__` method to the `GraphemeString` object.

  This is to support the `==` operator when comparing two `GraphemeString` objects.

- Added the `__add__` method to the `GraphemeString` object.

  This is to support the `+` operator when adding two `GraphemeString` objects together.

- Added the `__hash__` method to the `GraphemeString` object.

  This is to support the `hash()` function for a `GraphemeString` instance and allows it (as an example) to be used as
  a `dict` key.

## [0.1.2] - 2021-11-07

### Added

- Added base code, tests, and examples for the first release.