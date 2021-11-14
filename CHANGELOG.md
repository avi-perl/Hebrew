# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0] - 2021-11-14

### Added

- Added `hebrew.chars` with constants for Hebrew characters and classes to represent each letter.
- Moved constants out of `Hebrew` and into `hebrew.chars`.
- Constant values, previously strings, are now instances of a class with metadata for each letter.

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