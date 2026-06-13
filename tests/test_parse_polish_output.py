"""Tests for the two-axis report parser."""

from __future__ import annotations

import importlib.util
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("pp", REPO / "parse_polish_output.py")
pp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pp)

EXAMPLE = (REPO / "examples" / "POLISH_example.md").read_text(encoding="utf-8")


def test_example_parses_end_to_end():
    assert pp.extract_scores(EXAMPLE) == (8.6, 9.0)
    assert pp.extract_verdict(EXAMPLE) == "GATED-GO"
    assert pp.extract_new_findings_count(EXAMPLE) == 3
    assert pp.extract_open_findings_count(EXAMPLE) == 2
    findings = pp.extract_open_findings(EXAMPLE)
    assert len(findings) == 2
    assert findings[0] == {
        "severity": "HIGH",
        "location": "parser.py:88",
        "summary": "control characters survive destination validation",
        "introduced_on_pass": 2,
        "introduced_by": "claude",
    }
    # author is generalized, not hardcoded to a model name
    assert findings[1]["introduced_by"] == "human"


def test_aggregate_line_beats_table_and_prose():
    # The canonical aggregate line wins even when a table and prose also match.
    text = "craft 1 / fit 1\nCode quality: craft 7.5 / fit 8.\n| weighted average | 9 | 9 |"
    assert pp.extract_scores(text) == (7.5, 8.0)


def test_table_fallback_when_no_aggregate_line():
    text = "intro\n| weighted average | 6.2 | 7.1 |\n"
    assert pp.extract_scores(text) == (6.2, 7.1)


def test_missing_scores_return_none():
    assert pp.extract_scores("a report with no scores at all") == (None, None)


def test_labeled_verdict_beats_stray_tokens():
    # A stray GO in prose must not override the labeled NO-GO verdict.
    text = "we could GO further, but\nVerdict: NO-GO\n"
    assert pp.extract_verdict(text) == "NO-GO"


def test_open_findings_are_section_scoped():
    # A finding-shaped line OUTSIDE the open-findings section (e.g. in a code
    # fence) must not be counted. Only the real section is parsed.
    text = (
        "## The fix\n"
        "Example of the format: `- HIGH | x.py:1 | not a real finding | 1 | claude`\n\n"
        "## Open findings after this pass\n"
        "- LOW | y.py:2 | the one real open finding | 3 | codex\n"
    )
    findings = pp.extract_open_findings(text)
    assert len(findings) == 1
    assert findings[0]["location"] == "y.py:2"


def test_counts_come_only_from_the_accounting_section():
    text = (
        "Prose mentioning new findings this pass: 99 should be ignored.\n\n"
        "## Canonical accounting\n"
        "New findings this pass: 4\n"
        "Open findings after this pass: 1\n"
    )
    assert pp.extract_new_findings_count(text) == 4
    assert pp.extract_open_findings_count(text) == 1
