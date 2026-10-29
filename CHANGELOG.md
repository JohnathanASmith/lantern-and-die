# Changelog

## 1.3.1

- Fixed: a DM update could replace a quest's whole description in your journal with just the latest change. Updates now add to what your hero already knows instead of wiping it, and the DM is asked for the full picture.
- Near-identical clues are no longer added twice.

## 1.3.0

One hero sleeping no longer fast-forwards everyone else.

- Long actions (sleeping, a long rest, reading through the night) put just that hero on hold until a set time. Everyone else in the place keeps playing at the current hour.
- Heroes still awake get a card: keep playing, rest until then too, or skip ahead. The clock jumps only when everyone there is resting or skipping, and then everyone wakes together with a short "morning" from the DM. Sleeping 6+ hours restores like a long rest.
- Sleepers don't hear normal talk. A shout, a fight or someone shaking them wakes them, and they can tap Wake up any time.

## 1.2.2

- Fixed: when an NPC answered a hero loudly enough for the whole room, the hero who spoke could end up outside the reply, seeing "talks with you out of earshot" with Listen in. The hero who triggers a reply now always hears it.

## 1.2.1

- Fixed a stray "null" under the talk box when there were no ideas showing.
- When a Claude call fails, the message now says why (declined, came back empty, too much to send, sign in again) instead of always "the DM got interrupted".

## 1.2.0

Talk now follows who can actually hear it.

- Earshot: each line is heard only by heroes and NPCs close enough. Choose Whisper, Talk or Shout when you speak, and Openly or Quietly when you act. Talking to someone across the room walks your hero over to them.
- Private spots: stepping aside (a vestry stair, a back room) puts you in a spot nobody outside can hear. The map lists who is in each spot.
- Out of earshot, other players see a short grey line instead ("Legrey talks with Brother Ilric on the vestry stair") with Listen in, which may take a Stealth roll.
- NPCs only know what they heard, so private conversations stay private in the story too.
- Ideas: tap for 4 suggestions built from what your hero knows and carries, marked with what each uses (a check, coins, a spell).
- Journals: your chronicle, quests, clues and people met show only what your hero knows. Tell another hero something from your journal to share it in character.
- Coin purse in gold, silver and copper, updated automatically when coins change hands.
- Revealed about you: new facts the DM adds about your hero's past appear on your sheet to keep or change, and the DM sticks to your version.
- Last time…: a short catch-up from your own journal when you come back after a while.

## 1.1.3

- Gender: a simple Male / Female / Other choice on the Story step (and in Edit story) replaces the pronouns box from 1.1.2. Generate, Surprise me, painted portraits, pixel heroes, the DM and NPCs all follow it. With no gender set, generated text uses the hero's name or they/them instead of guessing.
- Match story to name & gender: one tap rewrites the appearance, personality and backstory so they use the hero's current name and gender, leaving everything else as written.

## 1.1.1

- Ending a campaign now clears everything from it: talk, checks, turns, NPC memories, scenes and party chat, and private Ask the DM answers no longer show. Heroes keep their level and gear and unlock for editing.
- Tables ended on an older version are cleaned up the next time the host opens the page.
- Ending a campaign keeps the host's DM settings.
- The review step no longer says a hero is "already in the campaign" when no campaign is running.
- Generate for spells (class spells, Magic Initiate and Versatile Magic Initiate) now fills the field even when Claude answers in a different shape, and says so if it comes back empty.
- Surprise me fills spells for every class that casts at level 1, including Paladins, Rangers and Versatile Magic Initiate.

## 1.1.0

The table gets art.

- Scene maps are drawn with pixel-art tiles: stone, wood, grass, water, trees, doors, stairs, statues, altars, plus hand-drawn bars, tables, barrels, crates, beds, chests, hearths and torches.
- Light and dark: night falls over outdoor scenes, dungeons and crypts stay dark, and fires, torches and heroes cast light.
- NPCs appear as sprites (guards, priests, bandits, wolves, skeletons, dragons and more). The DM picks each look; tap anyone on the map to see who they are.
- The DM sets a theme for each place (tavern, temple, crypt, forest...) and furnishes maps with the new tiles.
- Illustrated world map: parchment, inked forests, mountains, fields and rivers, a title cartouche and compass rose; the unexplored drifts under cloud.
- Hero portraits, three ways: a pixel hero built from your species and class (change hair, outfit, cloak, headwear, weapons), a portrait painted by Claude, or your own uploaded art.
- Player card: a trading-card view of your hero with portrait, HP, AC and abilities, on the Character tab. Save it as an image.
- Portraits show up across the table: party list, Talk, your sheet, map tokens and world map markers.

Tile art from Dungeon Crawl Stone Soup (RLTiles), dedicated to the public domain (CC0).

## 1.0.1

- Character tab: once a hero is in play, story details are read-only until you tap Edit story.
- Character tab: the Ask the DM coach is hidden once a hero is in play (use Ask the DM in Talk instead).

## 1.0.0

First public version.

- Step-by-step 2024 hero builder with live hero card, Generate, Surprise me and Ask the DM.
- Live Talk with Say, Do and private Ask the DM; NPCs with memory and attitudes; DM-called checks with Heroic Inspiration rerolls.
- Scenes with their own clocks, split parties, catch-up arrivals and skip ahead.
- Fog-of-war world map with routes, journeys, travel pace, camping and turning back.
- Combat in initiative order, attack checks and death saves.
- 2024-style sheet with skills under abilities, attacks, features, spell slots.
- Party chat, hero export (current or fresh at level 1), import and retire.
- Host DM settings for model and effort.
