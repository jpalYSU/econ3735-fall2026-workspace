# Steering moves

A message counts as steering when it changes the output in a direction the AI
would not have taken on its own. Use these labels in the log.

| Move | What it looks like | Example |
|---|---|---|
| **Set the goal** | Defines audience, purpose, constraints, or what "done" means before work starts | "This is for first-year students who have never cooked. Every recipe under 30 minutes, under $10." |
| **Supply context** | Adds facts, files, or knowledge the AI did not have | "Our bank charges a $15 fee on the 1st of each month; that explains the gap." |
| **Catch an error** | Points out something wrong and says what | "The total in row 12 double-counts the March deposit." |
| **Redirect** | Rejects an approach and names a different one | "Drop the listicle format. Write it as one story told across the week." |
| **Ask a probing question** | Questions a choice, assumption, or source, and the answer changes the work | "Why weekly instead of monthly? Which one matches the bank statement?" |
| **Set a quality bar** | Gives a concrete standard to revise against | "A stranger should be able to follow each step without asking a question. Check every step against that." |
| **Decompose** | Splits the task into steps or assigns order | "First reconcile the deposits only. Show me before you touch withdrawals." |
| **Choose** | Picks among options the AI offered, with a stated reason | "Option B, because the audience is investors, not customers." |

## What does not count

- Requests with no direction: "make it better", "try again", "more", "continue".
- Formatting-only changes that do not affect substance: "use bullets", "make it shorter" (unless the length limit is a real constraint the student introduced with a reason).
- Accepting a suggestion the AI made: "yes, do that". The AI did the steering there.
- Instructions copied from the assignment prompt. Pasting the assignment is a starting point, not steering. Count it only where the student added something to it.
- Thanks, greetings, and status checks.

## Borderline cases

- A vague complaint that the AI turned into a real fix ("this feels off") counts only if the student's next message chose among the fixes or confirmed a specific one with a reason. Log the later message.
- A probing question counts only if the answer changed the work. If the AI answered and nothing changed, do not count it, though it may make a good explain-this question.
