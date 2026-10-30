---
name: table
description: Starts, updates or checks a Lantern & Die table, the shared D&D 2024 game page where Claude is the Dungeon Master. Use when the user asks to start a new Lantern & Die table or campaign, make a fresh table, update their table, check for a new Lantern & Die version, or set up automatic updates.
---

# Lantern & Die tables

Lantern & Die is a shared D&D (2024 rules) table that runs as a claude.ai artifact. Players build heroes, talk live with NPCs, travel a fog-of-war world map and fight in initiative order, with Claude as the Dungeon Master. Each table is owned by the person who creates it; that person is the host. All campaign data lives in the table's own database, so republishing the page never loses heroes or progress.

## The page

The page ships inside this skill:

- `assets/lantern-and-die.html`: the game page, with `<meta name="lantern-and-die-version" content="X">`
- `assets/capabilities.json`: the artifact capabilities and database rules it needs
- `assets/VERSION`: the bundled version
- `assets/lpc.png`, `assets/lpc.json`, `assets/lpc-credits.json`: the character art sheet, its index and its credits, published next to the page

The newest version is also published in the public GitHub repo `https://github.com/JohnathanASmith/lantern-and-die` (changelog in `CHANGELOG.md` at its root).

Get the newest page like this:

1. Copy the bundled files into a fresh folder in the working directory.
2. Fetch the repo with git, which works where plain web downloads are blocked:
   ```bash
   git clone -q --depth 1 https://github.com/JohnathanASmith/lantern-and-die lad-latest
   ```
   If that fails, try `curl -fsSL -o <file> https://raw.githubusercontent.com/JohnathanASmith/lantern-and-die/main/plugins/lantern-and-die/skills/table/assets/<file>` for `VERSION`, `lantern-and-die.html`, `capabilities.json`, `lpc.png`, `lpc.json` and `lpc-credits.json`.
3. If GitHub's `plugins/lantern-and-die/skills/table/assets/VERSION` is newer than the bundled `VERSION`, use GitHub's page, `capabilities.json` and `lpc.*` files instead of the bundled ones. If GitHub can't be reached, use the bundled files and say so in one line.
4. Check the HTML's `lantern-and-die-version` meta matches the version you're publishing. Never rebuild or edit the page by hand.

## Every time: check the user's tables

1. Find the user's tables: Artifact `action: "list"`, keeping the ones titled "Lantern & Die".
2. For each, Artifact `action: "read"` and read its `lantern-and-die-version` meta (missing means 0).
3. If any table is behind the newest version, say so in one line with the changelog highlights and offer to update. Update straight away if that's what the user asked for.

## Start a new table

1. Get the newest page.
2. Publish a NEW artifact (no `url`): `file_path` = the page, `files` = {"lpc.png", "lpc.json", "lpc-credits.json"} from the same folder, `capabilities` = the parsed `capabilities.json`, `icon: "dice"`, description "A shared D&D 2024 table where Claude is the Dungeon Master."
3. Tell the user briefly:
   - Build a hero on the Character tab, then start the campaign from the Table tab. Only the table's owner can host.
   - Share the table from its Share menu with each player as **Contributor** (Viewers can't play).
   - Everyone allows Claude when the page first asks. The host's Claude runs the DM; each player's Claude runs their own talk and character help.
4. Offer automatic updates (below).

## Update a table

1. Get the newest page.
2. Read the table (Artifact `action: "read"` with its `url`), then publish the page to that same `url` with `capabilities` from `capabilities.json` and `files` = the three `lpc.*` files.
3. Confirm in one line: "Updated your table from X to Y," plus the top changes.

Never delete a table, its data or its sharing while updating.

## Automatic updates

Offer once, after starting or updating a table. If the user agrees and scheduled tasks are available (search for the scheduling tools with ToolSearch), create a weekly scheduled task:

- Name: "Lantern & Die updates"
- Schedule: weekly, early morning in the user's time zone
- Prompt: "Use the Lantern & Die table skill to check my Lantern & Die tables against the newest version on GitHub. Update any table that is behind, then tell me which tables changed and the main changes. If none are behind, say so in one line."

Say which approval setting the task got; if its runs will ask before publishing, mention the user can switch it to automatic approval in the task's settings. If there's no scheduling tool, say tables are checked whenever they use this skill.
