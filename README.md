# ECON/BUS 3735 workspace

This is your workspace for Modules 3 to 7. It runs in a GitHub Codespace, a temporary computer in the
cloud that you use through your browser.

**Your Codespace is temporary. Download everything you want to keep.** GitHub can automatically
delete an inactive Codespace, including files and changes you haven't pushed to GitHub. The default
retention period is 30 days of inactivity, but settings can shorten it. Saving a file or stopping
the Codespace does not create a backup. Download your coursework after each assignment and make a
complete backup before the course ends on December 6. Do not leave your only copy in Codespaces.
See [GitHub's automatic deletion policy](https://docs.github.com/en/codespaces/setting-your-user-preferences/configuring-automatic-deletion-of-your-codespaces).

## First time (Module 3)

1. Open the [course template](https://github.com/jpalYSU/econ3735-fall2026-workspace). Choose **Use this template → Create a new repository**.
   Make your copy **private** and name it `econ3735-yourlastname`.
2. In your private copy, choose **Code → Codespaces → Create codespace on main**. Wait for the
   container to finish building; it installs Claude Code and the spreadsheet tools.
3. In the terminal, type `claude` and press Enter. Choose your Claude account login and follow the
   browser prompt. Use your Claude Pro subscription rather than an API billing account.
4. Ask Claude: `What skills do you have available?` It should list **steering-log**.
5. Confirm `data/`, `templates/`, and `.claude/skills/steering-log/` are present, then commit and push
   any coursework changes to your private repository.

If the template is unavailable, Blackboard's Codespaces Setup page includes the same workspace as
a ZIP, with browser-only setup steps. If you're reading this inside your Codespace, start at step 3.

## Every session

- Open your repository on GitHub, then **Code → Codespaces** and pick your existing codespace.
  Don't create a new one each time.
- Start Claude Code with `claude` in the terminal.
- Save your work to GitHub before you stop: ask Claude to commit and push, or use the Source Control
  panel on the left. Confirm the latest files appear on your repository's GitHub page.
- Export the assignment's chat history and download your files and steering log. Use different
  filenames for each assignment so a new export doesn't overwrite an earlier one.
- Stop your Codespace when you finish so it doesn't use hours while idle. Stopping it does not
  prevent later automatic deletion.

## Download a complete backup

1. Save all open files. In Claude Code, use `/export assignment-chat.txt` to save the current
   conversation in your course folder; replace the filename with one that identifies the assignment.
   Export each conversation you need to keep, and save its steering log too. Chat histories stored
   elsewhere in the Codespace are not automatically included in your repository.
2. Ask Claude to create a dated ZIP of **all your coursework**: skills, plugins, scripts, datasets,
   reports, spreadsheets, images, decks, web pages, recordings, test results, exported chat histories,
   and steering logs. Include coursework that hasn't been committed or is ignored by Git. Exclude
   passwords, API keys, installed software, and older backup ZIPs. Keep the backup private.
3. Find the ZIP in the Codespace's **Explorer**, right-click it, and choose **Download**. Save it on
   your own computer and keep another copy in OneDrive or another location you control.
4. Unzip the downloaded copy and open several files, including a plugin or skill, a spreadsheet or
   report, and a chat export. Check that the files are present and readable before relying on it.

**GitHub's Code → Download ZIP contains only the files committed on the selected branch.** It can
leave out generated files, uncommitted work, and chat histories. Commit and push regularly, and also
download the complete coursework backup above.

## What's here

| Folder | What it's for |
|---|---|
| `.claude/skills/steering-log/` | The course steering log skill. Ask for a steering log at the end of a session. |
| `templates/skill-template/` | A starting point for your First Skill (Module 3). Copy it into `.claude/skills/`. |
| `templates/plugin-template/` | A starting point for your Plugin Build (Module 4). |
| `data/` | Cosmic Crunch data files used in assignments. |

## Free hours

Verified students get extra free Codespaces hours through the GitHub Student Developer Pack. Stop
your codespace when you finish (Code → Codespaces → ... → Stop) so it doesn't use hours idling.
