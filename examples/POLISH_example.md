# Polish: example subject

A worked example of a report in the two-axis format, here so the parser has a
real document to read and the test has something to assert. The numbers are
illustrative.

## Aggregate

Plan quality: craft 8.6 / fit 9.0.

Verdict: GATED-GO

| theme | craft | fit |
| --- | --- | --- |
| Engineering | 9 | 9 |
| Visual design | 8 | 9 |
| weighted average | 8.6 | 9.0 |

## Canonical accounting

New findings this pass: 3
Open findings after this pass: 2

## Open findings after this pass

- HIGH | parser.py:88 | control characters survive destination validation | 2 | claude
- MEDIUM | index.md:12 | the notes list is not keyed for screen readers | 1 | human
