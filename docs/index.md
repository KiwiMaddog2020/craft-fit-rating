---
title: "Rating your own work without lying to yourself"
date: 2026-06-12
---

# Rating your own work without lying to yourself

<p class="dek">A two-axis craft and fit rubric, anti-inflation rules, and what happened when I pointed it at the blog you are reading.</p>

<p class="meta">Kevin Madson · June 2026 · 5 min read</p>

> **If someone forwarded this to you:** I build and operate agentic systems
> across multiple coding LLMs. This note is about the rubric I use to grade the
> output, especially the work no second model can grade for me, and the rules
> that keep a self-assigned score honest.

<p class="contact-card">
<a href="https://github.com/KiwiMaddog2020/craft-fit-rating">github.com/KiwiMaddog2020/craft-fit-rating</a>
<span class="sep">·</span>
<a href="mailto:kevinmadson@protonmail.com">kevinmadson@protonmail.com</a> <!-- pragma: allowlist -->
</p>

---

## The case a second rater can't cover

In a [companion note](https://kiwimaddog2020.github.io/trust-weighted-evals/) I
argued that an AI agent should never grade its own work, and the fix was more
raters: work from one model is judged by two others. That works when the thing
being judged is objective enough that disagreement means something.

It does not cover the harder case. Some of what I make is subjective craft. Is
this layout good? Is this paragraph tight? Is this the right abstraction? You
cannot add three raters to "is this beautiful" and average your way to the
truth, and a lot of the time the only person in the room who knows the project's
real goal is me. So the question becomes the uncomfortable one: when you have to
grade your own work, how do you keep the number honest?

## Two axes, not one

The first rule is that every category gets two scores, never one. Collapsing
them is how "well-built" quietly launders into "good", and how a beautiful
solution to the wrong problem scores the same as the right one.

- **Craft** is universal craftsmanship. Would a senior expert in that
  discipline nod and say "yes, that is well-built"? It does not care what you
  were trying to do.
- **Fit** is fit-to-purpose, scored against the project's own stated goals. Does
  this serve what you are actually building?

A category at 9 craft and 4 fit is not a 6.5. It is a 4-gap, because the weaker
axis is what holds the work back, and `gap = 10 - min(craft, fit)` is what the
plan sorts on. Splitting the axes is the single change that does the most work,
because most self-deception lives in the slash between them.

## Evidence, or the grade is too high

Every craft grade has to cite something: a file and line, a test count, a
measured contrast ratio, a benchmark, a commit. No evidence means the score is
inflated; you lower it until you can point at a fact.

The tell is in the language. Before a report ships it gets grepped for the
phrases people reach for when they have no evidence:

```
seems reasonable | looks fine | could be better | appears solid | generally well-structured
```

Each of those is a grade with the evidence filed off. If one survives the grep,
the category goes down until the phrase can be replaced with something checkable.

## Anti-inflation is structure, not willpower

A self-scored loop drifts upward on its own. You cannot fix that with resolve,
so the rubric fixes it with rules that only point one way:

- Ties break **down**. A category between two scores takes the lower.
- Reward only the realized artifact, never effort, intent, or the plan.
- Discount anything you cannot verify. An unverifiable claim is not a 10.
- Exiting is legitimate. It is fine for a category to sit at 7 and say so. A
  rubric that can only go up is a rubric that is lying.

And when polish alone cannot reach the target, the rubric is required to say so.
It parks and names the structural decision instead of faking the last points.
That rule is the same one the companion framework runs on, and it is the rule
that matters most, because a process that cannot say "I can't get there from
here" will eventually tell you it got there when it didn't.

## What happened when I pointed it at this blog

The fairest test of a rubric is to run it on the thing presenting it. This blog,
including the note you are reading, was graded and rebuilt under this exact
process. It started at an honest **68.3 out of 100**. A measured re-rate after
the first round of fixes put it at **85.4**. After two more rounds it sat near
**90**.

Here is where the rubric grades itself, because two of its own rules fired on
this run and I am not going to hide either one.

First, the disclosure rule. That final number near 90 is an **estimate, not a
measured re-rate**. The panel that produced the 85.4 ran six independent rater
agents at once, each driving a headless browser, and on my laptop that load
crashed the machine, three times. So I scored the final state inline, by hand,
under the same anti-inflation discipline, rather than fake a clean re-rate I
could not run. The honest label is "estimate", and it stays on the number.

Second, the park rule. The target was 92. I could not get there, and when I
looked at why, the gap was not polish. A single web page structurally caps a
handful of categories: a lone page has a finite component palette, and some
checks only resolve once the site is live. Grinding would not have moved them
without gaming the rubric. So the process did what it is built to do: it parked
at ~90 and named the structural decision. The decision it named was "the way
past this is a second note, not more polishing of the first."

This note is that second note. The rubric, run on the blog, told me to write
exactly the thing you are reading. I find that more convincing than any score.

## The runnable part

A rubric is only honest if the number a report claims and the number it can
defend are the same number. So the format is machine-readable, and
[`parse_polish_output.py`](https://github.com/KiwiMaddog2020/craft-fit-rating)
reads a report and returns the aggregate craft and fit scores, the verdict, and
the open-findings ledger as JSON. It is about two hundred lines of stdlib
Python with a 7-test suite, and the repo ships a complete example report plus
the exact JSON the parser extracts from it. Clone it, run the parser on the
example, and check that the scores it prints are the scores the report claims.
`RUBRIC.md` is the full discipline.

None of this makes a self-assigned score objective. It makes it **honest**,
which is a smaller and more achievable thing: every grade carries its evidence,
the forbidden phrases are gone, the score is allowed to stop short, and when it
stops short it says why instead of pretending.

---

<p class="byline"><em>I build agentic systems across multiple coding LLMs. More of my research notes are <a href="/">here</a>.</em></p>
