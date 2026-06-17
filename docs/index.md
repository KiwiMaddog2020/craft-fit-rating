---
title: "Rating your own work without lying to yourself"
date: 2026-06-12
---

# Rating your own work without lying to yourself

<p class="dek">A two-axis scoring method, a short list of rules that can only subtract, and what came out when I turned it on the blog you are reading.</p>

<p class="meta">Kevin Madson · June 2026 · 5 min read</p>

> **If someone forwarded this to you:** I build software with AI agents, programs
> that write and change code on their own. Much of what they produce is subjective
> craft, the kind no second program can grade for me, so the grading falls to me.
> This note is about the rules that keep a self-assigned score honest, and the
> small tool that makes the score checkable by anyone who doubts it.

<p class="contact-card">
<a href="https://github.com/KiwiMaddog2020/craft-fit-rating">github.com/KiwiMaddog2020/craft-fit-rating</a>
<a href="mailto:kevinmadson@protonmail.com">kevinmadson@protonmail.com</a> <!-- pragma: allowlist -->
</p>

---

## The case a second grader can't cover

Anyone who has graded their own work knows the pull to round up. You finish the
resume, the paint job, the slide deck, and the part of you that did the work is
the same part that gets to decide it came out great. The judge is the defendant.

In a [companion note](https://kiwimaddog2020.github.io/trust-weighted-evals/) I
argued that an AI model should never grade its own output, and the fix was more
graders: work from one model gets judged by two others, none of which wrote it.
That works when the artifact is objective enough that disagreement carries
information. Two graders splitting on whether a function is correct tells you
something. Two graders splitting on whether a paragraph is beautiful tells you
they have different taste.

So it leaves the hard case wide open. A lot of what I make is subjective craft.
Is this layout good. Is this paragraph tight. Is this even the right thing to
build. You cannot bolt three graders onto "is this beautiful" and average your
way to truth, and most days the only person who knows what a project is actually
for is me. The uncomfortable question survives all of it: when you have to be your
own grader, what stops the number from drifting up?

## Two scores, never one

Rule one: every category carries two scores. Collapse them into a single number
and "well-built" quietly absorbs "good," and a beautiful thing aimed at the wrong
problem ends up scoring the same as the right one.

- **Craft** is workmanship in isolation. Would a senior practitioner in that
  specific field look at it and say yes, that is well made. Craft does not know or
  care what you were trying to do.
- **Fit** is service to the actual goal. A gorgeous house on the wrong lot is high
  craft, low fit. The carpentry is real. It is also beside the point.

A category at 9 craft and 4 fit is not a 6.5. The weaker score governs it, so the
method ranks every item by how far its weaker axis sits below ten. That 4-fit
item carries a six-point gap and goes straight to the top of the fix list, ahead
of things that average higher and hurt less. Splitting the axes is the one change
that earns its keep, because nearly all self-deception hides in the slash between
craft and fit.

## Evidence, or the grade is inflated

Every craft score has to point at something a stranger could check: a file and a
line number, a measured contrast ratio, a test count. No referent, no score. You
lower the number until you can name a fact that holds it up.

The tell is lexical. Before a report ships, it gets grepped for the phrases people
reach for when they have nothing concrete underneath:

```
seems reasonable | looks fine | could be better | appears solid | generally well-structured
```

Each one is a grade with the evidence filed off. If a single phrase survives the
search, that category drops until the phrase can be swapped for something
falsifiable.

## Rules that only ever subtract

A score you assign yourself climbs on its own, like a thermostat with a thumb on
it. Willpower does not fix that. So the method fixes it structurally, with rules
built so they can only push a number down:

- Ties break **down**. Caught between two scores, a category takes the lower.
- Reward only what exists. Not the effort, not the intent, not the plan you swear
  you will execute.
- Discount whatever you cannot verify. An unverifiable claim is not a 10, however
  much you believe it.
- Stopping short is legal. A category may sit at 7 and say so out loud. A scale
  that only travels upward is a scale that lies.

And when polish cannot close the remaining gap, the method is *required* to say
so. It parks, names the real decision, and refuses to manufacture the last few
points. That rule does the heaviest lifting, because any process that cannot admit
"I can't get there from here" will eventually report that it got there when it
flatly did not.

## What came out when I aimed it at this blog

The fairest test of a scoring method is to point it at the thing presenting it.
This blog, this note included, was graded and rebuilt under exactly this process.
It opened at an honest **68.3 out of 100**. A measured re-grade after the first
round of fixes returned **85.4**. Two rounds after that, it sat near **90**.

Here is where the method grades itself, because two of its own rules fired on this
run, and I am not going to bury either one.

The evidence rule first. That final figure near 90 is an **estimate, not a
measured re-grade**. The careful re-grade that produced the 85.4 ran six
independent grader programs concurrently, each driving its own headless browser,
and on my laptop that load hard-crashed the machine. Three times. So I scored the
final state by hand, under the same downward-only rules, rather than fake a clean
automated re-grade I could not actually execute. The label is "estimate." It stays
welded to the number.

Then the park rule. The target was 92. I could not reach it, and when I dug into
why, the gap was not polish. A single web page structurally caps a handful of
categories: one page only contains so many distinct kinds of component, and some
checks simply will not resolve until the site is live. Grinding on the prose would
not have moved them without gaming the score outright. So the process did its job.
It parked near 90 and named the real decision, which was this: the way past the
ceiling is a second note, not more sanding of the first.

This is that second note. The method, run on the blog, told me to write the exact
thing you are reading. I find that more convincing than the score it gave.

## The runnable part

A score is only honest if the number a report claims and the number it can defend
are identical. So the report format is machine-readable, and
[`parse_polish_output.py`](https://github.com/KiwiMaddog2020/craft-fit-rating)
reads a report and prints back the craft and fit scores, the verdict, and every
still-open issue, as plain structured data. It is roughly two hundred lines of
standard-library Python behind a 7-test suite, and the repo ships a full example
report alongside the exact data the parser extracts from it. Clone it, run the
parser on the example, and check for yourself that the scores it prints match the
scores the report claims. `RUBRIC.md` holds the full method.

None of this makes a self-given score objective. It makes it **honest**, which is
the smaller and far more reachable target: every grade drags its evidence along
behind it, the empty phrases are gone, the number is allowed to stop short, and
when it stops short it tells you why instead of pretending it didn't have to.

---

<p class="byline"><em>I build agentic systems across multiple coding LLMs. More of my research notes are <a href="/">here</a>.</em></p>
