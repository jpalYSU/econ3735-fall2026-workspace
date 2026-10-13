---
name: steering-log
description: Turn an AI work session into a steering log for ECON/BUS 3735. Use when a student says "steering log", "chat history for my assignment", "log this session", or asks to prepare an AI session for submission. Finds the moments where the student changed the outcome, quotes them verbatim, flags personal information, and writes two explain-this questions about the student's own session.
---

# Steering log

A steering log is a one-page record of how a student directed an AI session. It
goes in with the raw chat history on assignments that ask for it. The instructor
reads it to see what the student contributed. The student reads it to see the
same thing, which is the more useful half.

## What to read

Use whichever applies:

1. **The current conversation.** If the student asks for a steering log at the end
   of a chat or Cowork/Work session, the session is already in your context. Use it.
2. **A transcript file.** In a Codespace or any folder with Claude Code or Codex
   session files, run `scripts/export_transcript.py` to find the most recent
   session and convert it to `transcript.md`, then read that file. Pass `--list`
   to see recent sessions and `--session <path>` to pick one.
3. **A pasted or uploaded history.** Read it as given.

If more than one session went into the assignment, ask which ones to include and
log each one separately.

## Numbering turns

Number the messages the student typed, in order: S1, S2, S3, and so on. Do not
count text the tool inserted on its own (loaded skill instructions, system
notices), and do not count the message asking for this steering log. If you
skipped anything, say so in one line under "Student turns". Every reference to
the session uses these numbers, and every quote is exact, so the instructor can
find each moment in the raw history by searching for the quoted words.

## Finding steering moments

Read `references/steering-moves.md` before choosing moments. A steering moment is
a student message that changed what the AI produced in a way the AI would not have
reached on its own. List **up to five**, ordered by how much they changed the
result, not by when they happened.

Use one row per student turn. If a single message makes several moves, list
them together in the Move column (for example, "Redirect + Set the goal") and
quote the part that carries the most weight.

For each row record:

- the turn number,
- the student's words, **quoted exactly** (trim with "..." if long, never paraphrase),
- the move type or types from the reference file,
- one sentence on what changed, naming the AI reply where the change shows up
  ("AI reply to S4 drops the listicle format"). If you cannot point to a change
  in a later AI reply, the message does not qualify.

**Do not inflate.** If the session had little steering (the student accepted
the first draft, or repeated "make it better"), list only the moments that
qualify, even if that is one or none, and say so plainly in the verdict. A short,
honest log is a correct result. Never upgrade a vague request into a
specific one by describing it more favorably than the quote supports.

## Steering verdict

One of the following, with one sentence of justification that cites turn numbers:

- **Strong**: the student set the direction, caught at least one specific error
  (naming what was wrong, not only expressing dissatisfaction), and the final
  product reflects choices the AI did not propose.
- **Moderate**: some real direction or correction, but the AI made most of the
  decisions.
- **Light**: the student mostly accepted or re-requested output.

## Privacy check

Scan the whole session for: names of people other than the student and public
figures, email addresses, phone numbers, street addresses, account or ID numbers,
passwords or API keys, and health or financial details about anyone. List each
with its turn number and a suggested redaction. Do not repeat the sensitive value
itself in the log; describe it ("a classmate's full name at S4"). If nothing is
found, say "No personal information found." If parts of the session were not
visible to you (attached files, tool output shown only as a summary), add one
line saying what you could not scan, so the student checks those parts by hand.

## Explain-this questions

Write **two** questions the student should be able to answer without AI if they
understood their own session. Each question must:

- point to a specific turn or decision in this session,
- ask *why* or *what would happen if*, not *what*,
- be answerable in under 150 words.

Good: "At S6 the agent switched from monthly to weekly totals. Why did it do that,
and which one is right for the question you asked?"
Weak: "What did you learn from this session?"

Prefer questions about places where the AI made a decision the student did not
explicitly ask for, since those are the parts a student is most likely to accept
without understanding.

## Output

Write the log to `steering-log.md` (in the working folder if there is one, or as
a file the student can download). Use exactly this structure:

```
# Steering log

Assignment: <ask the student if unknown>
Tool: <Claude / ChatGPT / Codex / other> · Session date: <date>
Student turns: <count>

## What the session did
<3 to 5 sentences: the goal, what was produced, how many rounds it took.>

## Steering moments
| Turn | Student's words (verbatim) | Move | What changed |
|---|---|---|---|

## Steering verdict
<Strong / Moderate / Light>: <one sentence citing turns>

## Privacy check
<list, or "No personal information found.">

## Explain-this questions
1. <question>
2. <question>

## My answers (written by me, without AI)
1.
2.
```

Leave the answers section empty. For the Term Project Final Project, tell the student to leave it blank because the video replaces written explain-this answers. For other assignments, tell the student, in one line after the file
is written, that the answers must be their own words and that the instructor
may ask about any turn in the log.

## Things not to do

- Do not grade the work itself or comment on its quality beyond the steering.
- Do not answer the explain-this questions, even if asked. Offer instead to
  walk through the relevant part of the session so the student can understand it
  and write the answer themselves.
- Do not edit or summarize the raw history the student submits alongside the log.
- Do not count text copied from the assignment instructions as steering. If you
  do not have the assignment text, ask the student which parts of their first
  message came from the instructions.
