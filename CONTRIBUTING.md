# Contributing to `Hebrew`

This project welcomes contributions in the form of Pull Requests.
For clear bug-fixes / typos etc. just submit a PR.
For new features or if there is any doubt in how to fix a bug, you might want
to open an issue prior to starting work.

## Development Environment

Rich Tools uses [poetry](https://python-poetry.org/docs/) for packaging and
dependency management. To start developing with Rich Tools, install Poetry
using the [recommended method](https://python-poetry.org/docs/#installation) or run:
<!--pytest-codeblocks:skip-->
```bash
pip install poetry
```

Once Poetry is installed, install the dependencies with the following command:
<!--pytest-codeblocks:skip-->
```bash
poetry install
```

### Tests

Run tests with the following command:
<!--pytest-codeblocks:skip-->
```bash
poetry run pytest --codeblocks
```

_The `--codeblocks` flag runs tests on the python code blocks found in markdown files and is critical to testing!_

New code should ideally have tests and not break existing tests.

If you are not familiar with writing tests but still want to contribute to this package, 
please feel free to submit your pull request, and I will work on tests. 🙂

### Type Checking

Please add type annotations for all new code.

### Code Formatting

Rich Tools uses [`black`](https://github.com/psf/black) for code formatting.
I recommend setting up black in your editor to format on save.

To run black from the command line:
<!--pytest-codeblocks:skip-->
```bash
black <path-to-files-changed>
```