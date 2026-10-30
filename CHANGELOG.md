# Changelog

## 1.14.2
- A progress bar above Say/Do counts down to the next DM-played turn (who and how many seconds), shows when the DM is answering, and says when DM play is waiting on a roll or paused.
- Pictures and system notes no longer reset the quiet timer; DM-play checks every 5 seconds.

## 1.14.1
- DM-played heroes now take their own turns: when a scene has been quiet for 40 seconds and someone in it is at the table, the DM plays the next move for a DM-played hero (round robin), and the world answers. It pauses after 8 such turns in a row until a player acts or presses Keep going. Runs on the page keeping the world, never when nobody in the scene is at the table.
- The DM's reply logic can act for a hero other than the page's own (coins, private lines and rests go to the right hero).

## 1.14.0
- "DM plays for me" checkbox next to Send. It turns on by itself when a player has been away for 3 minutes and stays on after they return, until they untick it or press Take over. Players can tick it themselves while at the table. While it's on the DM voices that hero between their own lines and rolls for them; they can still say or do things.
- Earshot preview: the To list shows whether each person hears you (or sees it, for Do), is too far, in another room or asleep, and a line under the input lists who will and won't. It follows Say/Do, Talk/Whisper/Shout, quiet actions and walking over to someone. Hidden listeners are never shown.

## 1.13.1
- Character sheet and player card show the new figure when there's no portrait.
- The Pixel hero tab is now an editor for the new figure: body, skin, hair colour, head, ears, hair, beard, shirt, dress, armour or coat, belt, cloak, legs, feet, headwear, weapon, shield, with colours. Choices sit on top of what your description gives; Match my description again clears them.
- Humanoid monsters (goblins, hobgoblins, orcs, gnolls, kobolds, lizardfolk, minotaurs, trolls, ogres) use the new figures; beasts keep their tiles.
- Goliaths and big folk in armour keep a normal body (so armour shows) and are drawn a little taller.

## 1.13.0
- Real character sprites: heroes and NPCs are now built from the Liberated Pixel Cup (LPC) layered art: body type, skin, head (human, elderly, orc, lizard for dragonborn, and more), ears, hair style and colour, beard, shirt, armour, coat, apron, robe or dress, trousers or skirt, boots, cloak, hood or helmet, weapon and shield, all read from descriptions, class and inventory. Used on the map, in the chat and in the who's-here list; painted portraits still win where they exist.
- The art ships as three files next to the page (lpc.png, lpc.json, lpc-credits.json). Art credits are listed at the bottom of the page.
- tools/lpc has the scripts that build the art sheet from the LPC repository.

## 1.12.0
- Painted NPC portraits: once an NPC has a description, the page keeping the world paints them (one at a time) and keeps it. Tap any NPC face to see it large, with Repaint.
- NPC figures on the map are now built from the same parts as hero figures, using their description (species, gender, hair, beard, role clothing); monsters keep their tiles.
- Faces in the chat: NPC lines show their portrait or figure.
- Scene pictures: a painting when the heroes arrive somewhere new, and for striking moments the DM picks (at most one per scene every 15 minutes, never intimate scenes). They appear in the chat and above the scene map, with earlier ones browsable.
- New `art` collection (players can write).

## 1.11.1
- NPCs can become pregnant too: after an intimate scene with a hero, if the DM judges she could conceive and wouldn't have taken her own precautions, the page rolls a secret d20 (18+). The DM keeps it hidden from players, she learns of it after a few weeks, and decides in character whether and when to tell.
- NPC memory rewrites keep this.

## 1.11.0
- Pregnancy as a player's choice: after an intimate scene with no precautions in the story, the player of a female hero (who isn't already pregnant) privately picks No chance or Chance. Chance rolls a d20, 18+ means pregnant. Only she sees the card and result.
- The DM knows quietly: signs show gradually after a few weeks of game time, and the telling is left to her player.
- Saving a character sheet keeps these fields.

## 1.10.4
- Rolls are required: while you owe a roll, Say/Do is locked until you roll. The skip option is gone.
- The host can cancel a roll the DM asked for by mistake, from the host bar.
- While a roll is waiting, the DM is told not to resolve that attempt or move the scene past it; others can still talk.
- If a player leaves (away for over a minute after the 3-minute grace) while owing a roll, the game rolls for them.

## 1.10.3
- NPCs now have a remembered look (under 250 characters), set when they first appear and updated when it changes (mud, blood, new clothes). It follows them between scenes and is sent with every conversation and world update, so NPCs stay consistent and notice each other's looks.

## 1.10.2
- The DM now sees each hero's appearance, gender and alignment in conversation and world updates, so NPCs react to how heroes look.
- Conversation also gets level, HP, conditions, exhaustion, Heroic Inspiration, languages, known spells with slots left, class features, expertise and a short backstory.

## 1.10.1
- The DM's bookkeeping (moving heroes to new places, HP, items, quests) no longer waits for the host's screen: when the host is away, a player at the table runs it. Requires game, scenes, characters and actions to be writable by players (interact).
- Sending a new line while you still owe a roll now asks you to roll it first or skip it, so the story can't leave rolls behind.

## 1.10.0
- Dice overhaul: a host Dice setting (Light, Standard, Crunchy; Standard by default). On Standard the DM calls for checks whenever there is resistance or risk, not just big moments.
- Contested rolls: when an NPC opposes a hero, the page rolls for the NPC and that total is the number to beat (shown as "vs Ring-man's 14").
- Passive Perception is sent to the DM so noticing things can happen without a roll.
- Heroes whose player is away still roll: the page rolls for them and the story carries on.

## 1.9.1
- An old "on the way" status can no longer lock someone's Talk box: it only counts when the destination is actually expecting them.
- Undo never brings back an old travel status.

## 1.9.0
- Host "Undo last turn": rewinds the scene you're viewing to just before the last thing a player said, did, rolled or set off on. It removes the lines, rolls and notes since then, and restores the scene, positions, clock, errands, the heroes' sheets (HP, coins, items), quests and the chronicle. One step back per scene.

## 1.8.4
- A quiet action that names another hero ("I quietly tell Elara…") now includes that hero, so they see what you told them and the DM's reply.

## 1.8.3
- If the DM voices an NPC by the name a hero learned (Tamsin) instead of the listed name, the line is filed under the same person, so one NPC never splits into two.

## 1.8.2
- A hero who moves on to another scene no longer keeps a stale "on the way" status that could lock their Talk box.

## 1.8.1
- While you're on your way to another scene, you can't keep acting (or Waiting) in the place you left, which used to play out a second copy of where you were heading.
- New "Join them now" button: step into the scene you're heading to right away, at their time.
- Short hops (up to an hour ahead of the people there) arrive straight away instead of waiting for their clock.

## 1.8.0
- Errands between scenes: an NPC sent from one scene to another (to fetch someone where the other hero is) is known to be there. While they're busy there, the scene they left knows not to bring them back yet, and Wait doesn't skip ahead for them.
- The DM in the scene they visit knows they're on an errand and sends them back when their business is done (or when someone sends them back). They leave that scene, and the scene they came from gets them back a few minutes later.

## 1.7.13
- If you hit Send (or Wait) while the DM is answering someone else, your line is held, not posted. When it's your turn and something new happened in the meantime, you see what happened and choose: Send it, Change it, or Drop it. If nothing changed, it just goes.

## 1.7.12
- World updates and journey legs take the same one-at-a-time turn as talk, so a scene update can't contradict an NPC reply happening at the same moment.
- Wait moves the clock only when its turn comes, so two Waits don't stack up time before either is answered.
- The DM is told to stay consistent with answers other heroes got moments earlier.

## 1.7.11
- One DM reply at a time per scene across all players: if two people act at the same moment, the second waits a few seconds and the DM answers with the first result in view, so the story can't split into two versions.

## 1.7.10
- NPCs answer at the hero's own volume: a reply to a whisper or a quiet action is whispered back, so people nearby (and other heroes) no longer overhear one side of a sneaky exchange.

## 1.7.9
- Walls and shut doors stop voices: people inside a building on the map can't hear (or see) what's said and done outside it, and the reverse. Shouts still carry.
- The DM is reminded to move heroes on the map when they go into a building, up a stair or onto a landing.

## 1.7.8
- Talking to a friend's hero no longer silences the world: NPCs in earshot can still react (a goodbye when someone leaves, a reply to a plan that involves them), while the DM never answers for the friend.
- Someone a hero was just talking with may react when that hero says they're leaving.

## 1.7.7
- When an NPC answers a hero privately, anyone who could hear the hero's own words (an eavesdropper close by) hears the answer too, instead of only one side of the conversation. Private narration (what a hero alone notices) stays private.

## 1.7.6
- Quiet actions (and anything done while hidden) are secret: other heroes don't see them, or the rolls that come with them, just because they're standing close. Only the person the action is aimed at is in on it, and the DM decides if anyone notices.

## 1.7.5
- Talk history is never pruned anymore (it used to keep only the newest 300 lines across the whole campaign).
- Reading back an earlier scene loads up to 1,000 lines.

## 1.7.4
- Learned names: when an NPC tells a hero their name, that hero sees it everywhere (Talk feed, To list, map, who's here). Heroes who weren't there keep seeing the description until they learn it too.

## 1.7.3
- Appearance and personality now hold up to 800 characters (were 400, which cut generated text off mid-word), with taller boxes.
- Generated appearance and personality are asked to stay short and finish every sentence.
- Item notes keep up to 200 characters instead of 60.

## 1.7.2
- Other heroes in the scene appear in the Say/Do "To" list, marked "(away)" when their player isn't at the table.
- Saying something to a friend who is present and playing goes straight to them; the DM doesn't answer for them.

## 1.7.1
- The DM only speaks or acts for a hero when that hero's player is away from the table, and then plays them true to their personality and how their player has been playing them, keeping big choices for the player.
- Away heroes follow the party like a real party member, including on journeys.
- Lines the DM plays for an away hero are labeled "played by the DM".

## 1.7.0
- The scene clock moves with play: each exchange takes in-world minutes (a quick line, a search, a ritual).
- NPC errands: when someone leaves the heroes for a while, the DM records what they're doing and when they'll be back, and brings them back once the clock gets there.
- New Wait button next to Ideas: lets time pass until the next errand is due (or 15 minutes).

## 1.6.4
- Repeating an action before rolling no longer stacks a second copy of the same check.

## 1.6.3
- Fixed journeys resetting to 0%: pushing on while already on the road continues the same journey instead of starting a new one over the top of it.
- The DM knows how far along the road the party is and no longer narrates covering the distance outside the journey controls.

## 1.6.2
- Companions: NPCs who travel with the party (an escort, guide or employer) now go along on journeys and arrive with the heroes instead of staying behind.

## 1.6.1
- Talk can read back earlier scenes: pick "Earlier: <scene>" above the feed to scroll what your hero saw and heard there, then "Now" to return.
- Fixed a stray "null" under the map legend.

## 1.6.0
- New campaign tone: Bawdy & cheeky, a raunchy, playful adult comedy that stays suggestive, never explicit.
- The chosen tone is now saved and guides every DM call for the whole campaign, not just the opening.
- The host can change the tone mid-campaign from the host bar.

## 1.5.1
- Romance scenes: the DM plays the lead-up in more detail and closes intimate scenes inside the story instead of breaking character to say it is fading to black.

## 1.5.0

Maps that stay consistent, with exits you discover.

- Maps you've seen don't get redrawn. The DM can only change single squares, each with a reason from the story (a table knocked over, a hatch found).
- Every room records where it's entered from on the main map, and a door is always drawn there, so two maps can't disagree about the way in.
- Every door and stair has a destination the DM knows. If one has none, the DM is asked to explain it or remove it.
- Destinations stay secret until discovered: you see "Narrow door", not where it goes, until your hero goes through, looks, sees someone use it or is told. Obvious exits (the front door, the door you came in by) show where they lead.

## 1.4.1

- Tap anything on the map to see what it is: the DM names and describes notable things (the hearth, the bar, a locked chest), and everything else gets a plain name (barrel, door, stairs).
- Things in your room come with Look closer and Go to it, and people with Talk to and Look at. They fill in your talk box so you can edit before sending.
- The DM only draws furniture the story has established or that plainly belongs, since whatever is on the map becomes real.

## 1.4.0

Maps follow where your hero is and what they've seen.

- Perches: high or tucked-away places inside a room (rafters, a balcony, behind the bar) are drawn on the map with a raised token and a gold marker. Hidden heroes show faded to themselves and not at all to others.
- Separate rooms (a vestry, a back room, a cellar) get their own tab above the map with their own small map.
- Your room is live. Rooms you've been in show as you last saw them, greyed, with the time, and people stay where you last saw them. Rooms you haven't entered show a shut door.
- The DM draws a small map whenever someone enters a new room, and tells perches and rooms apart.

## 1.3.3

- Catch-ups after a long time away now keep the start of what happened as well as the end, so early events (like the result of something you started just before leaving) aren't dropped.

## 1.3.2

Better "Last time…" catch-ups.

- Built from the talk your hero actually saw and heard, plus your chronicle, quests and clues, written by the stronger DM model.
- Three parts: the story so far, what happened near you while you were away, and where you are right now (who's around and what's waiting on you).
- A Catch me up button on the Scene panel brings one up any time.

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
