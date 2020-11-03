# Combat Scenario

In the Simply Roleplaying system, combat is designed to be fairly simple while also allowing for a variety of different weapons and combat styles, as well as offering a variety of different techniques that can be performed in combat. When combat starts, every participant rolls a flat [Intuition](/character/attributes/) check unmodified by bonuses provided by any skill. This check determines how quickly each of the characters reacts to the combat scenario. In the event of an ambush, the ambushers may roll their Intuition twice, and use the combined value. Each combatant marks this value as their **initiative** for this combat. Then, starting with the character with the highest roll and continuing in descending order, each character takes a turn. This ordering is referred to as the **turn order**, and a full rotation of the turn order is considered a combat **round**. Each round takes approximately 10 seconds of game time, with all actions happening in the round occurring roughly sequentially.

## Actions and Reactions
<!-- TODO: This should be updated to indicate that a player may have more than one action per turn. Also get rid of minor actions. -->
Each turn a character may perform up to one major action and one minor action, though not necessarily in that order. A **minor action** can be used to perform a quick task or do something that does not require an undue amount of focus. Some examples of minor actions are running a short distance, jumping a gap, climb a ladder, hide behind a pillar, draw a weapon, or trigger a simple mechanism. Major actions are for more technical actions that a character might want to take, or an action that takes more time or effort. A **major action** is often something like attacking with a weapon, casting a spell, repairing broken machinery, deciphering a complicated message, hacking a computer terminal, or picking a lock. Additionally, a player may perform any minor action as a major action - since minor actions are just less complicated actions. This is to simulate a character sprinting flat out, running and jumping across a ledge, or any other substantially more complicated combination of actions that are together both simple tasks, but do not allow the time for more technical actions.

In addition to their actions that they can perform on their turn, characters can react to actions being performed against them. However, there is only so much time available in a round, so only one such reaction can be performed by any character before the beginning of the character's next turn. **Reactions** (as these responsive actions are called) are similar in scope to minor actions, but must be actions that are nearly instantaneous to perform. Some examples of reactions are ducking behind cover, dodging away from a fatal blow, closing a door, or activating a simple mechanism.

Sometimes a character will wish to perform their actions at a later time. Perhaps the room has filled with smoke and they're waiting for a clear shot, or the enemy mage is about to cast a spell and they want to wait out the attack. In either case, the character may choose to either delay their turn or hold their action. If a character **holds their action**, they may use their reaction at any time before the beginning of their next turn to perform a major action. If a character **delays their turn**, they choose to wait on to their turn until a later time in the round. Before any character with a lower initiative score takes their turn, the delayed character may take their turn. If more than one character are delaying their turns at the same time, each character is given the opportunity to take their delayed turn in initiative order. If a character is holding their action or delaying their turn at the end of the round, they are given one final opportunity to perform their action or turn. Held actions and delayed turns cannot carry over between rounds.

### Combat Dice
<!-- TODO: Finish this -->
blah blah blah dice that scale with you or whatever

### Accuracy, Potency, and Armor Value
<!-- TODO: If we're gonna go the route of Agility Weapons/Brawn Weapons/Intuition Weapons etc, this will need updating -->
In the real world, you aren't just as good at swinging an axe as you are stabbing with a spear, and Simply Roleplaying seeks to mimic that. To this end, the Accuracy skill and the Potency skill both are actually split into many different skills, each to represent a different weapon size and style. Each Accuracy or Potency skill is followed by a [Size] and [Style] classifier. For example: Accuracy with Small Slashing would be applicable for a knife wielding character, and Potency with Large Repeating would be applicable for a full-auto machine gun wielding character. More on this is discussed on the [weapons page](/basics/equipment/).

In a similar way it's difficult to have a single evasion skill, so evading an attack is split up into two different categories depending on whether the attack is considered Direct or Indirect. An attack is considered Direct if the defender is explicitly targetted by the attack, and if the attack could be completely evaded by quick movement. In the case of a Direct attack, the defender will roll a Dodge check, which is an Agility based skill. An attack is considered Indirect if the defender is not the explicit target, but is somehow affected by the attack- usually in the case of area-of-effect attacks that will affect multiple people, or if the attack could not be completely evaded by quick movement. In the case of an Indirect attack, the defender will roll a Reflexes check, which is an Intuition based skill.

One last thing to that is mentioned on this page is Armor Value. Armor value (AV) is what the attacker rolls their Potency check against when determining damage. Every piece of armor that a character is wearing contributes to their total armor valu. Depending on how well the attacker rolls, the defender is dealt damage for a weak, medium, or strong hit, respectively. More on armor value can be found on the [armor page](/basics/equipment/).

<!-- TODO: ^----- Combine? ------v -->

## Attacking with a Weapon

Attacking with a weapon is a [test of ability](/basics/tests). The attribute for the test can be any of the attributes that the weapon is tagged with, and the difficulty of the test is the [armor value](/basics/equipment/) of the target. Success on the test means dealing damage equal to the amount the attacker rolled, a critical success means double damage, a failure means half damage, and a critical failure means do damage at all.

As an example, here's the test for attacking an armor value 15 target using a greatsword with the tags _brawn_, _melee_, _large_, _cleaving_, and _slashing_:

>  **Attacking with a Greatsword**
>
>  _Difficulty **15** Test of **Brawn**_
>
>  ****
>
>  **Goal:** Striking the target and inflicting injury
>
>  **Risk:** Not inflicting any damage <!-- TODO: Review, what really is the risk here? Is it really just not inflicting as much damage as hoped? -->
>
>  ****
>
>  * **On a critical success:** the target [takes damage](/character/damage_and_injuries) equal to double the attacker's total for the test.
>  * **On a success:** the target [takes damage](/character/damage_and_injuries) equal the attacker's total for the test.
>  * **On a failure:** the target [takes damage](/character/damage_and_injuries) equal to half of the attacker's total for the test, rounded down.
>  * **On a critical failure:** the target takes no damage.

### Improvised Weapons

Sometimes, it makes sense that a character can attack with an object not intended to be a weapon or with a weapon in a way that it's not intended to be used. Examples of this could be using a table leg as a cudgel, throwing a maul, or bashing with the butt of a sniper rifle. Attacking in this way technically may violate the range or attributes tagged on the weapon, but should always be possible.

Your gamemaster may rule that **a character can use a weapon or object to attack with whatever attribute makes sense for the situation** but this improvised weapon carries an additional **risk of being damaged, destroyed, or otherwise lost** in test of ability associated with the attack. For more on risks, see [Making Good Tests](/character/tests#Making-Good-Tests). In addition, **the gamemaster may say that some tags on the weapon do not apply**-- bashing with the butt of a rifle, for instance, would likely not benefit from the rifle's quality tag, since the quality likely refers to how well it fires its rounds.

As an example, here's a possible test for attacking an armor value 15 target using the butt of a sniper rifle with the tags _agility_, _long-range_, _large_, and _precision_:

>  **Attacking with the Butt of a Sniper Rifle**
>
>  _Difficulty **15** Test of **Brawn**_
>
>  ****
>
>  **Goal:** Striking the target and inflicting injury
>
>  **Risk:** Not inflicting any damage, breaking or damaging the Sniper Rifle <!-- TODO: Review, what really is the risk here? Is it really just not inflicting as much damage as hoped? -->
>
>  ****
>
>  * **On a critical success:** the target [takes damage](/character/damage_and_injuries) equal to double the attacker's total for the test.
>  * **On a success:** the target [takes damage](/character/damage_and_injuries) equal the attacker's total for the test.
>  * **On a failure:** the target [takes damage](/character/damage_and_injuries) equal to half of the attacker's total for the test, rounded down, and the sniper rifle jams or is otherwise unusable for a short time.
>  * **On a critical failure:** the target takes no damage and the sniper rifle gets bent or broken in the scuffle and requires repairs.

<!-- TODO: This is no longer accurate. Needs updating. -->
One of the more common major actions that a character will perform in combat is the Attack action. An attack consists broadly of two checks; a test of weapon accuracy and a test of weapon potency. An attack that passes either of those tests is considered exceptionally progresstent or accurate, and inflicts significant damage. An attack that fails both of those tests is considered to be more of a glancing blow and inflicts minimal damage. An attack that passes both checks is both exceptionally accurate and potent, and inflicts maximum damage.

<!-- TODO: How does accuracy work now? AV? Passive stats? -->
* The attacker rolls a check of their weapon's Accuracy stat against the defender's ??? to see whether or not the attack passes the accuracy test
	* If the attacker's roll is higher than the defender's roll, the attack is considered **accurate**.
	* If the attacker's roll is not higher than the defender's roll, the defender may use a Reaction to Evade the attack, nullifying damage.
* If the attack is not evaded, the attacker then rolls for their weapon's Potency, which determines the total amount of damage dealt by the attacker.
	* If the attacker's roll is greater than the defender's Armor Value, the attack is considered **potent**.
* An attack that is both accurate and potent deals **strong** damage. An attack that is either accurate or potent deals **medium** damage. An attack that is neither accurate nor potent deals **weak** damage.
