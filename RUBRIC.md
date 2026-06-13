# The two-axis rubric: craft x fit

A discipline for rating your own work without quietly inflating the score. It
rates any creative artifact on two independent axes, demands evidence for every
grade, forbids the phrases people reach for when they have none, and gives the
process explicit permission to fail rather than fake a number.

`parse_polish_output.py` reads a report written to this format and returns the
scores, the verdict, and the open-findings ledger as JSON, so the number a
report claims and the number it can defend are the same number.

## The two axes

Every category gets two scores, not one. Conflating them is how "well-built"
launders into "good", and how a beautiful solution to the wrong problem scores
the same as the right one.

- **CRAFT (1-10)** is universal craftsmanship. Would a senior expert in that
  discipline nod and say "yes, that is well-built"? It does not care what you
  were trying to do.
- **FIT (1-10)** is fit-to-purpose, scored against the project's own stated
  objectives. Does this category serve what you are actually trying to build?

For each category, record the **gap = 10 - min(craft, fit)**. A category at 9
craft / 4 fit is not a 6.5; it is a 4-gap, because the weaker axis is what
holds the work back.

## Themes

Group categories into themes. A whole codebase wants 50+ categories across ~10
themes (engineering, visual design, UX, brand, architecture, security,
operations, performance, documentation, customer-facing readiness). A single
page or feature wants 20-30 across 5-7 themes. Name the themes honestly; do not
pad the count.

## The evidence requirement (non-negotiable)

Every CRAFT grade cites at least one specific piece of evidence: a file path
and line, a test count, a benchmark number, a commit hash, a measured ratio, a
log line. No evidence means the grade is too high; lower it until you can cite.

**Forbidden phrases.** Grep the report before you publish it:

```
seems reasonable | looks fine | could be better | appears to be solid | generally well-structured
```

Each of those is a grade with the evidence filed off. If one survives,
downgrade the category until you can replace the phrase with a fact.

## Anti-inflation

A self-scored loop drifts upward unless the framing pushes back. The rules:

- **Ties break down.** A category between two scores takes the lower one.
- **Reward only the realized artifact**, never effort, intent, or plan.
- **Discount the unverifiable.** A claim you cannot check is not a 10.
- **Exit is legitimate.** It is fine for a category to sit at 7 and say so. A
  rubric that can only go up is a rubric that is lying.

## Permission to fail

When polish alone cannot reach the target, the report must say so. It parks and
names the structural decision: "we are at 8.6 against your 9.0, and closing the
gap needs choice A or choice B." It is not allowed to fake the score, and it is
not allowed to finish by lowering the bar.

## The report format (what the scorer parses)

A report is Markdown. To be machine-readable, it includes:

- An aggregate line: `Plan quality: craft X / fit Y.` (or `Code quality: ...`),
  or a Markdown table row whose first cell is `weighted average` followed by
  the two numbers.
- A labeled verdict line: `Verdict: GO` (or `GATED-GO | NO-GO | CONVERGED |
  PLATEAU | DID-NOT-CONVERGE`).
- A `## Canonical accounting` section carrying `New findings this pass: N` and
  `Open findings after this pass: N`.
- A `## Open findings after this pass` section, one finding per line,
  pipe-delimited: `- SEVERITY | location | summary | N | author` where N is the
  pass the finding was introduced on.

`examples/` has a complete report and the JSON the scorer extracts from it.
