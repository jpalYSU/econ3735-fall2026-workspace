---
name: sales-brief
description: Turns a weekly Cosmic Crunch sales export (CSV or pasted table) into a short three-finding brief for the sales manager. Use when someone shares a weekly sales file, sales numbers, or a sales export and asks for a brief, summary, recap, or "what happened this week" for the sales manager. Not for one-off data questions, forecasts, or charts.
---

# Turn the weekly sales export into a three-finding brief for the sales manager.

## When to use this skill

Use it when a coworker shares a weekly sales export (a CSV, spreadsheet, or pasted table) and wants a summary for the sales manager. Typical requests: "write the brief for the sales manager," "summarize this week's sales," "what stood out in this export?"

Don't use it for one-off questions about the data ("how many units did we sell in Ohio?"), multi-month trend analysis, forecasts, or making charts. Answer those directly.
## Inputs

- One weekly sales export. Expected columns: date, product, region, units, revenue. Prior-week columns are a bonus if present.
- If no file is attached or pasted, ask for it. Don't invent numbers.
- If the file covers more or less than one week, say so and ask whether to continue.

## Steps

1. Open the file and list its columns, its row count, and its date range.
2. Look for data problems: blank cells, duplicate rows, mixed date formats, text in number columns, and rows outside the date range. Write down each one.
3. Exclude rows you can't use, and record how many you excluded and why. Don't guess at missing values.
4. Calculate total units and total revenue for the week.
5. Break the totals down by product and by region.
6. If prior-week data exists, calculate the week-over-week change for the totals and for each product.
7. Pick the three findings that matter most to a sales manager: big changes, top or bottom performers, and anything unusual.
8. Write the brief in the format below.
9. Run every check in "Checks before finishing" and fix anything that fails.
## Output

A Markdown brief of no more than 200 words, written in plain, direct language for a busy sales manager:

**Week of [start date] – [end date]**
**Headline:** one sentence with total revenue and units (plus the week-over-week change if available).

**Three findings**
1. **[Short title]:** what happened, with the number. *Why it matters:* one sentence.
2. ...
3. ...

**Data notes:** the rows excluded and the problems found, or "No data issues found."

## Checks before finishing

- Every number in the brief appears in the file or was calculated from it. Recalculate each one.
- Product totals and region totals each add up to the overall total.
- The date range in the brief matches the file.
- There are exactly three findings, and each one includes a number and a comparison, not just a raw figure.
- Every data problem from step 2 is listed under "Data notes." Nothing was fixed silently.
- The brief is 200 words or fewer.

## Example

**Input:** week1.csv, 42 rows, Oct 6–12. Total revenue $18,450. Galaxy Granola revenue up 30% from last week. The Midwest region is down 12%. Two rows have blank revenue.

**Output:**
**Week of Oct 6 – Oct 12**
**Headline:** Revenue was $18,450 on 3,210 units, up 4% from last week.
1. **Galaxy Granola surged:** revenue rose 30% to $5,100. *Why it matters:* it is now our top seller, so check that stock levels can keep up.
2. **Midwest slipped:** revenue fell 12% to $3,900. *Why it matters:* it's the only region that declined.
3. ...
**Data notes:** 2 rows with blank revenue were excluded (rows 17 and 31).
