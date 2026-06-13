# craft-fit-rating

A discipline for rating your own work without quietly inflating the score, plus
a small parser that keeps a report's claimed number and its defensible number
the same number.

The write-up lives at
**https://kiwimaddog2020.github.io/craft-fit-rating/**.

- [`RUBRIC.md`](RUBRIC.md) is the method: two axes (craft and fit), a
  gap metric, the evidence requirement, the forbidden-phrase gate, the
  anti-inflation rules, and permission to park instead of faking a score.
- [`parse_polish_output.py`](parse_polish_output.py) reads a report written to
  that format and prints the aggregate craft and fit scores, the verdict, and
  the open-findings ledger as JSON. Pure stdlib.
- [`examples/`](examples/) has a complete report and the exact JSON the parser
  extracts from it.

## Run it

```bash
python3 parse_polish_output.py examples/POLISH_example.md   # prints the parsed JSON
python3 -m pytest tests -q                                  # 7 tests
```

The scores the parser prints are the scores the example claims; that is the
whole point.

## License

MIT (see LICENSE).
