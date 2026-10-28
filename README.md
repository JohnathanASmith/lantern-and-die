# Lantern & Die

A shared Dungeons & Dragons (2024 rules) table that runs as a claude.ai artifact, with Claude as the Dungeon Master.

- **Step-by-step hero builder** with 2024 classes, backgrounds, species and origin feats, plus Generate, Surprise me and Ask the DM.
- **Live play**: say or do anything, NPCs answer right away, the DM calls for the checks that matter.
- **Scenes and split parties**, each with its own clock, so time away matters.
- **Fog-of-war world map** that grows as you explore, with routes and journeys.
- **Combat** in initiative order with death saves.
- **Party chat**, private Ask the DM, hero export and import.

## Install

This repo is a Claude plugin marketplace with one plugin, **lantern-and-die**. It works on paid Claude plans.

1. In Claude, open **Customize > Plugins**, click **Add**, choose **Add marketplace**, then **Add from a repository**, and enter `JohnathanASmith/lantern-and-die`.
2. Add the **lantern-and-die** plugin.
3. In a chat, say **"Start a new Lantern & Die table."** Claude publishes a table that you own; you're the host.
4. Share the table from its **Share** menu with each player as **Contributor**.

## What the plugin does

- **Table** (`/lantern-and-die:table`): starts new tables, updates them to the newest version, and can set up a weekly scheduled task that keeps them updated.
- **Host tools** (`/lantern-and-die:host-tools`): session recaps, campaign backup and restore, session prep, and fixes for a stuck table.

## Updates

New versions are published here. Updating a table replaces only the page; heroes, scenes, world map and conversations stay in the table's database. Your Claude checks for a newer version whenever you use the plugin, and the optional weekly task updates your tables for you.

To update by hand, say **"Update my Lantern & Die table."**

## Repo layout

- `.claude-plugin/marketplace.json`: the marketplace listing
- `plugins/lantern-and-die/`: the plugin
  - `skills/table/assets/lantern-and-die.html`: the game page (version in `VERSION` and a `lantern-and-die-version` meta tag)
  - `skills/table/assets/capabilities.json`: artifact capabilities and database rules the page needs

See [CHANGELOG.md](CHANGELOG.md) for what changed in each version.
