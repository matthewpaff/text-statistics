# Text Counter Lab

Count Unicode characters, lines, whitespace-separated words, unique casefolded tokens, and common words.

This original small project uses **Python 3.10+ and only its standard library**.
No packages, virtual environment, service, or network access are required.

## Run

From this repository directory:

```console
python text_counter.py --help
python text_counter.py examples/sample.txt
python text_counter.py --check-fixtures fixtures/cases.jsonl
python -m unittest discover -s tests -v
```

Words are separated only by whitespace; punctuation remains part of a token. Counts use Unicode casefolding for uniqueness and ranking. Lines follow Python splitlines semantics: empty input has zero lines and a trailing newline does not create an extra line. Character counts include whitespace. Frequency ties sort lexicographically. This is not natural-language tokenization.

Output is JSON (or a fixture-check summary). Exit codes are 0 for success,
1 for file failures, and 2 for invalid input. Errors go to stderr.
For file-based tools, `-` reads stdin. Use UTF-8 input files.

## Structure and branches

- `text_counter_lab/core.py`: pure parsing or analysis logic.
- `text_counter_lab/cli.py`: command arguments and file input/output.
- `text_counter_lab/generate_fixtures.py`: deterministic original sample cases.
- `text_counter_lab/fixture_check.py`: expected-result/error validation.
- `fixtures/cases.jsonl`: 367 synthetic cases, one added per artificial dated commit.
- `tests/`: independently chosen boundary cases plus corpus validation.

`feature/core` and `feature/cli` retain the corresponding development snapshots.
`data/synthetic-fixtures` marks the completed corpus; `docs/usage` and `main` contain
the final documentation and tests. There are no copied upstream commits.

## Generate examples

```console
python generate_fixtures.py --count 20
```

This prints reproducible JSONL and **does not create or date Git commits**. The
historical-looking Git timeline is a separate, documented simulation. Many cases
vary generated values; they do not imply separate design decisions or features.

Keep contributions focused, add a regression test for changed behavior, and run
the standard-library tests. Never add real private data or credentials. Record
actual dates for new work. Licensed under [MIT](LICENSE).

[History and provenance](HISTORY.md).
