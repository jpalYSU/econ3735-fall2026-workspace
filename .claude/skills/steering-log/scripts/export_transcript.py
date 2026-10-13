#!/usr/bin/env python3
"""Convert a Claude Code or Codex session file into a readable transcript.md.

Claude Code keeps sessions in ~/.claude/projects/<folder>/<id>.jsonl.
Codex keeps them in ~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl.

Usage:
    python export_transcript.py                 # newest session from either tool
    python export_transcript.py --list          # show the 10 newest sessions
    python export_transcript.py --session PATH  # convert a specific file
    python export_transcript.py --out FILE      # default: transcript.md

Student messages are numbered S1, S2, ... in the output. Tool calls and tool
output are summarized on one line each so the transcript stays readable.
"""
import argparse, glob, json, os, sys

HOME = os.path.expanduser("~")
PATTERNS = {
    "Claude Code": os.path.join(HOME, ".claude", "projects", "*", "*.jsonl"),
    "Codex": os.path.join(HOME, ".codex", "sessions", "**", "*.jsonl"),
}
# Messages the tools inject that the student did not type.
SYSTEM_PREFIXES = ("<environment_context>", "<user_instructions>", "<command-",
                   "<local-command", "<system-reminder>", "Caveat:", "# AGENTS.md",
                   "Base directory for this skill", "<task-notification>")


def sessions():
    found = []
    for tool, pat in PATTERNS.items():
        for p in glob.glob(pat, recursive=True):
            try:
                found.append((os.path.getmtime(p), tool, p))
            except OSError:
                pass
    return sorted(found, reverse=True)


def text_of(content):
    """Return (text, tool_note) from a string or a list of content blocks."""
    if isinstance(content, str):
        return content, ""
    texts, tools = [], []
    for b in content or []:
        if not isinstance(b, dict):
            continue
        t = b.get("type", "")
        if t in ("text", "input_text", "output_text"):
            texts.append(b.get("text", ""))
        elif t in ("tool_use", "function_call"):
            tools.append("[tool call: %s]" % (b.get("name") or "tool"))
        elif t in ("tool_result", "function_call_output"):
            tools.append("[tool output]")
    return "\n".join(x for x in texts if x), " ".join(tools)


def parse(path):
    """Yield (role, text, note) in order, tolerating both tools' formats."""
    with open(path, encoding="utf8", errors="replace") as fh:
        for line in fh:
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if d.get("isMeta") or d.get("isSidechain"):
                continue  # text the tool inserted, or a subagent's side conversation
            ts = d.get("timestamp")
            if isinstance(ts, str) and len(ts) >= 10:
                yield "time", ts[:10], ""
            # Claude Code: {"type": "user"|"assistant", "message": {...}}
            msg = d.get("message") if isinstance(d.get("message"), dict) else None
            # Codex: {"type": "response_item", "payload": {"type": "message", ...}}
            pl = d.get("payload") if isinstance(d.get("payload"), dict) else None
            if msg and d.get("type") in ("user", "assistant"):
                role, content = msg.get("role", d["type"]), msg.get("content")
            elif pl and pl.get("type") == "message":
                role, content = pl.get("role"), pl.get("content")
            elif pl and pl.get("type") in ("function_call", "function_call_output"):
                yield "tool", "", "[tool call: %s]" % pl.get("name", "tool") \
                    if pl["type"] == "function_call" else "[tool output]"
                continue
            elif d.get("type") == "message" and d.get("role"):
                role, content = d.get("role"), d.get("content")
            else:
                continue
            text, note = text_of(content)
            if role == "user" and not text.strip():
                if note:  # tool results arrive as user messages in Claude Code
                    yield "tool", "", note
                continue
            if role == "user" and text.lstrip().startswith(SYSTEM_PREFIXES):
                continue
            if role in ("system", "developer"):
                continue
            yield role, text, note


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--session")
    ap.add_argument("--out", default="transcript.md")
    a = ap.parse_args()

    found = sessions()
    if a.list:
        import datetime
        for mt, tool, p in found[:10]:
            print("%s  %-11s %s" % (datetime.datetime.fromtimestamp(mt)
                                    .strftime("%Y-%m-%d %H:%M"), tool, p))
        return
    if a.session:
        path = a.session
        tool = "Codex" if ".codex" in path else "Claude Code"
    elif found:
        _, tool, path = found[0]
    else:
        sys.exit("No Claude Code or Codex session files found in this workspace.")

    out, n, pending_tools, dates = [], 0, 0, []
    for role, text, note in parse(path):
        if role == "time":
            dates.append(text)
            continue
        if role == "tool":
            pending_tools += 1
            continue
        if pending_tools:
            out.append("*(%d tool step%s)*\n" % (pending_tools, "" if pending_tools == 1 else "s"))
            pending_tools = 0
        if role == "user":
            n += 1
            out.append("### S%d (student)\n\n%s\n" % (n, text.strip()))
        else:
            if text.strip():
                out.append("**AI:**\n\n%s\n" % text.strip())
            if note:
                out.append("*%s*\n" % note)
    when = (min(dates) if dates and min(dates) == max(dates)
            else "%s to %s" % (min(dates), max(dates)) if dates else "unknown")
    head = ("# Transcript\n\nTool: %s\nSession date: %s\nSource: %s\nStudent turns: %d\n\n"
            % (tool, when, path, n))
    with open(a.out, "w", encoding="utf8") as fh:
        fh.write(head + "\n".join(out))
    print("wrote %s (%d student turns) from %s" % (a.out, n, path))


if __name__ == "__main__":
    main()
