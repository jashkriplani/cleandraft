# CleanDraft

CleanDraft is a small, dependency-free command-line utility that tidies Markdown files locally.

## Features

- Removes trailing whitespace.
- Normalizes Windows and old-style line endings.
- Collapses repeated blank lines.
- Normalizes spacing in ATX headings.
- Adds a final newline.
- Supports preview mode and explicit write mode.

## Requirements

- Python 3.10 or newer
- No third-party dependencies

## Usage

Preview the cleaned output without changing the source file:

```bash
python3 cleandraft.py notes.md
```

Overwrite the file with the cleaned version:

```bash
python3 cleandraft.py notes.md --write
```

Run the test suite:

```bash
python3 -m unittest -v
```

## Project status

This is an early-stage utility. Review the output before using it on important documents, and keep backups of files you care about.

## Contributing

Bug reports, tests, and improvements are welcome. Please explain the problem and include a small example where possible.

## License

MIT. See [LICENSE](LICENSE).
