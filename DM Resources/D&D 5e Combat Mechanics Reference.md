# D&D 5th Edition Combat: How Attacking and Defending Work After Initiative

## TL;DR
- **Attacking is a single roll against a static number.** You roll d20 + ability modifier (Strength for melee, Dexterity for ranged/finesse) + proficiency bonus, and compare it to the target's Armor Class (AC). If you meet or beat the AC, you hit and roll damage; the defender does **not** roll to "defend."
- **Getting hit relies on more than Hit Points.** Your defense is a layered system: Armor Class (built from armor + Dexterity + shield + magic/class features) decides *whether* you're hit at all, and only after a hit does damage come off your Hit Points—optionally reduced by resistance, temporary HP, or reactions like the Shield spell.
- **Strength/Dexterity power your offense (to-hit and damage); Dexterity also powers defense (AC, Dex saves, initiative), while Strength mainly helps carrying/Athletics.** A second, parallel defensive system—saving throws vs. a Difficulty Class—handles spells and effects that don't use attack rolls.

## Key Findings

1. **The attack roll:** d20 + ability modifier + proficiency bonus (if proficient) vs. the target's AC. Equal-or-higher = hit. Per the SRD: "If the total of the roll plus modifiers equals or exceeds the target's Armor Class (AC), the attack hits."
2. **AC is not a roll.** It's a fixed number the attacker must beat, composed of armor base + Dexterity (capped by armor type) + shield + other bonuses. The target usually does nothing when attacked.
3. **On a hit you roll damage** (weapon die + the same ability modifier used to attack) and subtract it from Hit Points. Proficiency bonus is NOT added to damage.
4. **Resistance halves, vulnerability doubles, immunity zeroes** damage of a given type; none of them stack with themselves.
5. **Saving throws are the mirror image of attack rolls:** for effects without an attack roll, the *target* rolls d20 + ability mod (+ proficiency if proficient) against the attacker's DC.
6. **Advantage/disadvantage** (roll 2d20, take higher/lower) modify attack rolls from conditions like prone, unseen, restrained, etc.; multiple instances don't stack and any advantage + any disadvantage cancel to a normal roll.
7. **Natural 20 always hits and is a critical hit** (double the damage dice); **natural 1 always misses**.
8. **At 0 HP** you fall unconscious and make death saving throws; temporary HP act as a buffer that absorbs damage before real HP.

## Details

### 1. The Sequence After Initiative Is Rolled
Initiative is a Dexterity check (d20 + Dex modifier); combatants act in descending order, and that order repeats each round. On your turn you get, in any order: **movement** up to your speed, **one action** (Attack, Cast a Spell, Dash, Disengage, Dodge, Help, Hide, Ready, Search, Use an Object), possibly **one bonus action** (only if a feature grants one), and a free object interaction. You also have **one reaction per round** that you can use on anyone's turn when its trigger occurs (e.g., an opportunity attack, or the Shield spell).

The SRD structures a single attack as three steps: (1) **Choose a target** in range; (2) **Determine modifiers** (cover, advantage/disadvantage, other bonuses); (3) **Resolve the attack**—make the attack roll, and on a hit roll damage. "If there's ever any question whether something you're doing counts as an attack, the rule is simple: if you're making an attack roll, you're making an attack."

### 2. The Attack Roll (Offense)
**Attack roll = d20 + ability modifier + proficiency bonus (if proficient) + other bonuses.**

- **Ability modifier:** Strength for melee weapon attacks; Dexterity for ranged weapon attacks. Weapons with the **finesse** property (e.g., rapier, shortsword, dagger) let you choose Strength *or* Dexterity; **thrown** weapons use the weapon's normal ability. Spell attacks use the caster's spellcasting ability (Int/Wis/Cha depending on class).
- **Proficiency bonus:** added only if you're proficient with the weapon (or it's a spell attack). It scales with character level (+2 at levels 1–4, up to +6). It is added to the attack roll, never to the damage roll.
- **Comparison:** If the total meets or exceeds the target's AC, it hits.

Example: a 1st-level fighter with Strength 16 (+3) and a longsword attacks. Roll 10 on the d20, +3 Strength, +2 proficiency = 15. If the goblin's AC is 15 or lower, it hits.

### 3. Armor Class (Defense) — How It's Built
AC is a **static number**, set at character creation (and adjusted by gear/spells), that the attacker must beat. You pick exactly ONE base formula—you never stack multiple base-AC methods:

- **Unarmored:** 10 + full Dex modifier.
- **Light armor** (padded/leather 11, studded leather 12): base + **full** Dex modifier.
- **Medium armor** (hide 12, chain shirt 13, scale mail/breastplate 14, half plate 15): base + Dex modifier **capped at +2**.
- **Heavy armor** (ring mail 14, chain mail 16, splint 17, plate 18): fixed base, **Dex does not apply at all**. (Heavy armor also has Strength-score requirements or you move slower.)
- **Shield:** +2 AC, added on top of any of the above, while wielded (requires proficiency and a free hand).

**AC-boosting class features, spells, and items** (these replace or add, per their wording):
- **Barbarian Unarmored Defense:** 10 + Dex modifier + **Constitution** modifier (may use a shield).
- **Monk Unarmored Defense:** 10 + Dex modifier + **Wisdom** modifier (no shield).
- **Mage Armor** (spell, 1st level, 8-hour duration): "The target's base AC becomes 13 + its Dexterity modifier. The spell ends if the target dons armor or if you dismiss the spell as an action." Because it sets a *base* AC, it does not stack with Unarmored Defense—use whichever is higher.
- **Shield** (spell, cast as a reaction): "1 reaction, which you take when you are hit by an attack or targeted by the magic missile spell… Until the start of your next turn, you have a +5 bonus to AC, including against the triggering attack, and you take no damage from magic missile." This is one of the few times a defender actively responds to an incoming attack—and it can retroactively turn a hit into a miss.
- **Cover** (situational): half cover +2 AC and Dex saves; three-quarters cover +5 AC and Dex saves; total cover can't be targeted. Only the most protective source applies; they don't add together. Note that a creature (ally OR enemy) between attacker and target grants half cover.
- **Magic items** (e.g., +1 armor/shield, Bracers of Defense +2 while unarmored), **Fighter's Defense fighting style** (+1 while armored), etc.

**Key point:** Nothing about a normal attack requires the *target* to roll. AC is passive. The defender's Strength, weapon, and most abilities are irrelevant to being hit; what matters is the AC number and any reaction they choose to spend.

### 4. On a Hit: Damage and Hit Points
On a hit, the attacker rolls the weapon's damage die/dice and adds the **same ability modifier used for the attack** (SRD: "When attacking with a weapon, you add your ability modifier—the same modifier used for the attack roll—to the damage"). Proficiency is *not* added. Some effects add extra dice (e.g., Rogue Sneak Attack, Divine Smite). Two-weapon fighting's bonus-action attack does *not* add the ability modifier to its damage (unless the modifier is negative).

The damage is subtracted from the target's current Hit Points. There's no separate "defense roll" and no armor-based damage reduction in default 5e—armor affects *whether* you're hit, not *how much* damage you take once hit. HP is an abstraction of stamina, luck, and durability, not just physical wounds. One reaction-based exception is the Rogue's **Uncanny Dodge** (level 5): "when an attacker that you can see hits you with an attack, you can use your reaction to halve the attack's damage against you."

### 5. Resistance, Vulnerability, Immunity
Each successful hit deals a **damage type** (slashing, fire, cold, etc.). Then:
- **Resistance:** damage of that type is **halved** (round down).
- **Vulnerability:** damage of that type is **doubled**.
- **Immunity:** damage of that type is **reduced to zero**.

These do **not stack**: multiple sources of resistance to the same type still only halve once. **Order of application** (per Xanathar's Guide / 2024 PHB): (1) any immunity, (2) flat additions/subtractions/multipliers, (3) resistance, (4) vulnerability. Example: 28 fire damage, with a −5 damage aura, resistance, and vulnerability → 28 − 5 = 23 → halved to 11 (round down) → doubled to 22.

### 6. Saving Throws — The Other Half of Defense
Many spells and abilities don't make an attack roll against your AC; instead they force **you** to make a saving throw against the source's **Difficulty Class (DC)**. This flips who rolls:
- **Attack roll:** the *attacker* rolls vs. your (static) AC.
- **Saving throw:** the *defender/target* rolls d20 + ability modifier + proficiency bonus (if proficient in that save) vs. the source's (static) DC.

**Spell save DC = 8 + proficiency bonus + spellcasting ability modifier.** Each class is proficient in exactly two of the six saves (Str, Dex, Con, Int, Wis, Cha); the other four use the raw ability modifier only. Fireball, dragon breath, and traps typically call for **Dexterity saves**; poison/concentration use **Constitution**; charm/fear use **Wisdom**. On a successful save, damage effects are usually **halved** ("save for half"); many condition effects are negated entirely. (The Rogue's Evasion turns a successful Dex save into *no* damage and a failure into half.) Note: the caster does not roll—their DC is fixed.

### 7. Advantage and Disadvantage
When you have **advantage**, roll 2d20 and take the higher; with **disadvantage**, take the lower. They do not stack (any number of advantage sources = roll twice), and if you have at least one of each, they cancel and you roll one d20 normally.

Common combat sources of **advantage** on attacks: attacking a target that can't see you (unseen attacker); attacking a prone target **from within 5 feet**; target is restrained, paralyzed, stunned, unconscious, or blinded; the Help action; Barbarian's Reckless Attack; the optional Flanking rule.
Common **disadvantage**: attacking a target you can't see; attacking a prone target **from more than 5 feet** (i.e., ranged attacks vs. prone); attacker is prone, poisoned, restrained, or blinded; ranged attack at long range or within 5 feet of a hostile creature; using a weapon/armor you're not proficient with.

**Reckless Attack** (Barbarian, level 2) is the clearest offense-for-defense trade: "you can decide to attack recklessly. Doing so gives you advantage on melee weapon attack rolls using Strength during this turn, but attack rolls against you have advantage until your next turn."

**Flanking** is an *optional* rule (Dungeon Master's Guide p. 251), not the default: when two allies are on opposite sides of an enemy, each has advantage on melee attacks against it. Many DMs decline it because advantage is a large, easily obtained bonus. Statistically, advantage is worth about **+3.3 on average** (the higher of two d20s averages ~13.8 vs. 10.5 for a single d20) and peaks at roughly **+25 percentage points** to your hit chance on a coin-flip roll (turning a 50% chance into ~75%). Combined with 5e's free movement, flanking is easy to set up, so it can make AC feel irrelevant. New DMs should treat it as optional.

### 8. Critical Hits and Critical Misses
- **Natural 20:** the attack **automatically hits regardless of AC or modifiers**, and is a **critical hit**. On a crit, "roll all of the attack's damage dice twice and add them together," then add modifiers once. Only *dice* double (weapon dice, Sneak Attack dice, smite dice, magic-weapon dice); flat modifiers (ability modifier, magic bonuses like +1) are **not** doubled. Example: a crit with a dagger and +3 Dex = 2d4 + 3, not 2d4 + 6.
- **Natural 1:** the attack **automatically misses regardless of modifiers or AC.**
- Note: the auto-hit/auto-miss rule applies only to **attack rolls**, not to ability checks or saving throws. There is no default "critical fumble" table (dropping your weapon, etc.)—that's a house rule. Some features expand the crit range (e.g., Champion Fighter crits on 19–20).

### 9. Zero HP, Death Saving Throws, and Temporary HP
When damage drops you to **0 HP**, you fall unconscious (drop what you're holding, can't act). You don't go negative—excess damage is normally ignored, *unless* it's **instant death**: if the leftover damage after hitting 0 equals or exceeds your HP maximum, you die outright.

**Death saving throws:** at the start of each of your turns at 0 HP, roll a plain d20 (no ability modifier, no proficiency). 10+ = success, 9 or lower = failure. Three successes = **stable** (unconscious at 0 HP, no more saves); three failures = **dead**. A **natural 1 counts as two failures**; a **natural 20 restores 1 HP** (you wake up). Successes/failures needn't be consecutive and reset when you regain any HP or stabilize.

**Damage while at 0 HP** causes one automatic death-save **failure**; if it's from a **critical hit**, two failures. Note that any melee attack that hits an unconscious creature from within 5 feet is automatically a critical hit (attacks against an unconscious target within 5 feet have advantage and auto-crit), so a foe finishing off a downed character typically inflicts two failures at once. You can also **stabilize** a dying creature with a DC 10 Wisdom (Medicine) check as an action, or any healing brings them back to consciousness.

**Temporary Hit Points (temp HP):** a buffer sitting on top of your real HP. Damage depletes temp HP first; they're "not hit points" and aren't healing—they don't stack (take the higher of two sources), don't restore consciousness, and (unless a feature says otherwise) last until depleted or you finish a long rest. While at 0 HP, temp HP can still absorb an incoming attack's damage—and if they absorb *all* of it, you avoid the death-save failure that damage would have caused. Effects that check your HP total (like Power Word Kill) ignore temp HP.

## Recommendations
For a new DM running combat, use this turn-by-turn checklist:

1. **Roll initiative** (d20 + Dex) once; keep the order all fight.
2. **On an attacker's turn**, resolve each attack as: pick target → check cover/advantage/disadvantage → roll d20 + ability mod + proficiency vs. the target's AC.
3. **If it's a natural 20**, it hits and crits (double the dice). **Natural 1** always misses. Otherwise, hit only if the total ≥ AC.
4. **On a hit**, roll weapon dice + ability modifier (no proficiency), apply resistance/vulnerability/immunity if relevant, subtract from HP (temp HP first).
5. **For spells/effects that say "make a saving throw,"** don't roll an attack—set your DC (8 + prof + casting mod) and have the *target* roll their save; apply half damage on a successful "save for half" effect.
6. **At 0 HP**, start death saves; watch for instant death (leftover damage ≥ HP max) and the auto-two-failures from adjacent crits.

**Thresholds that should change your approach:**
- If your players are constantly obtaining advantage cheaply (Flanking + free movement), consider dropping the optional Flanking rule or replacing it with a flat +2 to keep AC meaningful.
- If a monster has resistance/immunity your party can't bypass, signal it after the first hit so players switch damage types or use magical weapons.
- Learn the two "who rolls?" cases cold: **AC = attacker rolls; DC = defender rolls.** This is the single most common point of confusion for new tables.

**Version note:** This reference reflects the 2014 5e rules (SRD 5.1 / original Player's Handbook), which is what most learning material and virtual tabletops still use. The 2024 revision ("5.5e") keeps the same core math (attack vs. AC, save vs. DC, crits double dice) but tweaks some edge cases (e.g., how surprise interacts with initiative, and it dropped the optional Flanking rule entirely). Confirm which version your table uses.

## Caveats
- **Sources:** Core mechanics here are drawn from the official System Reference Document (SRD 5.1, Wizards of the Coast, Creative Commons) as mirrored at 5thsrd.org and 5e.d20srd.org, plus D&D Beyond forum rulings and the Sage Advice Compendium for edge cases. Spell/feature quotes (Shield, Mage Armor, Uncanny Dodge, Damage Rolls) were verified verbatim across multiple independent SRD mirrors. Community discussion (D&D Beyond forums, EN World, r/dndnext) was used only to illustrate common confusions, not to establish rules.
- **Instant-death and massive-damage nuance:** the "leftover damage ≥ HP max" instant-death rule is default; there's also a separate *optional* "massive damage" rule (System Shock table) in the DMG that most tables ignore.
- **House rules vs. RAW:** Flanking, critical-fumble tables, and "max damage on a crit" are all optional/house rules, explicitly not part of default play. This guide prioritizes rules-as-written.
- **Monsters vs. PCs:** DMs typically have monsters die instantly at 0 HP rather than roll death saves (major villains excepted). Monsters use the flat attack/save modifiers printed in their stat blocks rather than recalculating from ability scores.
- **Unarmed strikes:** deal 1 + Strength modifier bludgeoning damage by default (a flat number, not a die), and you're always proficient with them.
- **The advantage value figure** (~+3.3 average, ~+25 percentage points at 50/50) is a community-computed statistical estimate; the exact benefit varies with the target number you need to roll.