---
title: "Rating your own work without lying to yourself"
date: 2026-06-12
---

# Rating your own work without lying to yourself

<p class="dek">A scoring method with two axes, a few rules that only point downward, and what happened when I aimed it at the blog you are reading.</p>

<p class="meta">Kevin Madson · June 2026 · 5 min read</p>

> **If someone forwarded this to you:** I build software with AI agents, programs
> that write and change code on their own. A lot of that work is subjective craft
> that no second program can grade for me, so I have to grade it myself. This note
> is about the rules that keep a self-assigned score honest, and the small tool
> that makes the score checkable.

<p class="contact-card">
<a href="https://github.com/KiwiMaddog2020/craft-fit-rating">github.com/KiwiMaddog2020/craft-fit-rating</a>
<span class="sep">·</span>
<a href="mailto:kevinmadson@protonmail.com">kevinmadson@protonmail.com</a> <!-- pragma: allowlist -->
</p>

---

## The case a second opinion can't cover

Anyone who has graded their own work knows the pull to round up. You finish the
resume, the paint job, the slide deck, and the part of you that did the work is
the same part deciding it came out great.

In a [companion note](https://kiwimaddog2020.github.io/trust-weighted-evals/) I
argued that an AI should never grade its own output, and the fix was more graders:
work from one model gets judged by two others. That works when the thing being
judged is objective enough that disagreement means something.

It does not cover the harder case. A lot of what I make is subjective craft. Is
this layout good? Is this paragraph tight? Is this the right way to build the
thing? You cannot add three graders to "is this beautiful" and average your way to
the truth, and often the only person who knows what the project is actually for is
me. So the uncomfortable question stands: when you have to grade your own work,
how do you keep the number honest?

## Two scores, not one

The first rule is that every category gets two scores, never one. Collapsing them
into a single number is how "well-built" quietly becomes "good," and how a
beautiful thing that solves the wrong problem scores the same as the right one.

- **Craft** is plain craftsmanship. Would a senior expert in that field nod and
  say "yes, that is well made"? It does not care what you were trying to do.
- **Fit** is whether it serves the actual goal. A gorgeous house built on the
  wrong lot is high craft and low fit.

A category at 9 craft and 4 fit is not a 6.5. It is held back by its weaker score,
so the method ranks work by how far the weaker of the two sits from a perfect ten:
a 4-fit item has a six-point gap and rises to the top of the fix list. Splitting
the two scores is the single change that does the most work, because most
self-deception hides in the slash between them.

## Evidence, or the grade is too high

Every craft score has to point at something real: a file and line, a number, a
measured contrast ratio, a test count. No evidence means the score is inflated,
and you lower it until you can name a fact.

The tell is in the words. Before a report ships it gets searched for the phrases
people reach for when they have nothing concrete:

```
seems reasonable | looks fine | could be better | appears solid | generally well-structured
```

Each of those is a grade with the evidence filed off. If one survives the search,
that category goes down until the phrase can be replaced with something you could
actually check.

## The rules only point one way

A score you give yourself drifts upward on its own. You cannot fix that with
willpower, so the method fixes it with rules that can only ever lower a number:

- Ties break **down**. A category between two scores takes the lower one.
- Reward only the thing that actually exists, never the effort, the intent, or the
  plan.
- Discount anything you cannot verify. An unverifiable claim is not a 10.
- Stopping short is allowed. It is fine for a category to sit at 7 and say so. A
  scale that can only go up is a scale that is lying.

And when polish alone cannot reach the target, the method is required to say so.
It parks and names the real decision instead of faking the last few points. That
rule matters most, because a process that cannot say "I can't get there from here"
will eventually tell you it got there when it didn't.

## What happened when I aimed it at this blog

The fairest test of a scoring method is to run it on the thing presenting it. This
blog, including the note you are reading, was graded and rebuilt under exactly this
process. It started at an honest **68.3 out of 100**. A measured re-grade after the
first round of fixes put it at **85.4**. After two more rounds it sat near **90**.

Here is where the method grades itself, because two of its own rules fired on this
run and I am not going to hide either one.

First, the evidence rule. That final number near 90 is an **estimate, not a
measured re-grade**. The careful re-grade that produced the 85.4 ran six
independent grader programs at once, each driving its own browser, and on my
laptop that load crashed the machine three times. So I scored the final state by
hand, under the same downward-only rules, rather than fake a clean re-grade I could
not run. The honest label is "estimate," and it stays on the number.

Second, the park rule. The target was 92. I could not get there, and when I looked
at why, the gap was not polish. A single web page structurally caps a handful of
categories: one page has only so many kinds of component, and some checks only
resolve once the site is live. Grinding would not have moved them without gaming
the score. So the process did what it is built to do: it parked at about 90 and
named the real decision, which was "the way past this is a second note, not more
polishing of the first."

This note is that second note. The method, run on the blog, told me to write
exactly the thing you are reading. I find that more convincing than any score.

## The runnable part

A score is only honest if the number a report claims and the number it can defend
are the same number. So the report format is machine-readable, and
[`parse_polish_output.py`](https://github.com/KiwiMaddog2020/craft-fit-rating)
reads a report and prints back the craft and fit scores, the verdict, and the list
of still-open issues, as plain data. It is about two hundred lines of standard
Python with a 7-test suite, and the repo ships a complete example report plus the
exact data the parser pulls out of it. Clone it, run the parser on the example,
and check that the scores it prints are the scores the report claims.
`RUBRIC.md` is the full method.

None of this makes a self-given score objective. It makes it **honest**, which is a
smaller and more reachable thing: every grade carries its evidence, the empty
phrases are gone, the score is allowed to stop short, and when it stops short it
says why instead of pretending.

---

<p class="byline"><em>I build agentic systems across multiple coding LLMs. More of my research notes are <a href="/">here</a>.</em></p>
