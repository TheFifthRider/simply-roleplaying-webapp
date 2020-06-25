# Weapons

Weapons are any carried equipment used to attack another character from table legs to semi-automatic rifles. Each weapon has an attribute associated with it based on how the weapon is used to attack. 

_Brawn_ weapons are often heavy or strenuous to operate effectively, demanding great strength from their wielder and rewarding them with crushing blows. _Agility_ weapons are often light or rely on precision, perfect for characters with the skill to wound their opponent where it is most devastating. Depending on your setting, there may even be _charisma_, _intuition_, and _knowledge_ based weapons.

Each weapon also has a **quality modifier** based on the craftsmanship, materials, and renown of the weapon that ranges from +0 to +9.

 



## Attacking with a Weapon

To attack another character with a weapon is a special [test of ability](/character/tests) with the attribute associated with the weapon. In addition to the attribute modifier and dice rolled, the attacker also adds their weapon's quality modifier and compares it to the difficulty of the test-- the [armor value](/action/armor/) of the target.

**If the attacker succeeds** the defender takes damage equal the attacker's total for the test. <!-- TODO: This should be a link to the health page-- maybe fold that together with healing and put it in character? -->

**If the attacker critically succeeds** the defender takes damage equal to double the attacker's total for the test.

**If the attacker fails** the defender takes damage equal to half of the attacker's total for the test, rounded down. <!-- TODO: And? -->

**If the attacker critically fails** the defender takes no damage. <!-- TODO: And? -->



<!-- TODO: Do we care about size and style anymore? See old combat page-->

<!-- Weapons in Simply Roleplaying come in many different varieties, and are specifically categorized by their size and the style of the weapon. Any weapon should be able to be categorized in this way. -->
<!-- In terms of size, small weapons should be able to be wielded with one hand and nearly impossible to be wielded with two. Daggers, miniature crossbows, pistols, and brass knuckles are typically considered to be small weapons. Large weapons, on the other hand, typically require two hands to hold them. Rocket launchers, mauls, longbows, and staves are typically considered to be large weapons. Medium weapons are the weapons that end up between those two categories. Longswords, many rifles, police batons, and crossbows are typically considered to be medium weapons.-->

<!-- ## Melee Weapons -->

<!-- Melee weapons have six possible styles; Improvised, Battering, Hooking, Slashing, Impaling, and Cleaving. Battering weapons are typically blunt instruments, such as staves, batons, and maces. Hooking weapons are curved blades that necessitates the wielder making hooking motions when they attack, such as sickles, scythes, and some curved blades. Slashing weapons are any types of weapons used in a slashing manner, such as katanas, hunting knives, or longswords. Impaling weapons are weapons that are used with stabbing motions, like rapiers, bayonets, and spears. Cleaving weapons are typically heavy, bladed instruments that are swung with a chop, like axes and cleavers. Improvised melee weapons are typically either weaponized objects that are not intended to be used as weapons, ranged weapons used in a melee fashion, or melee weapons used in an unintended way. Examples of improvised melee weapons are table legs, bashing with the butt of a rifle, or hitting someone with the flat of your blade. See table C1 below for melee weapon damage by style and size. -->

<!-- {{ renderWeaponTable("Melee Weapon Damage Table",
   [
   ["",       "Improvised", "Battering", "Cleaving", "Hooking", "Slashing", "Impaling"],
   ["Small",  [1,3,4],      [4,4,5],     [3,4,6],   [2,4,7],    [2,3,8],    [1,3,9]   ],
   ["Medium", [2,3,5],      [5,5,6],     [4,5,7],   [3,5,8],    [3,4,9],    [2,4,10]  ],
   ["Large",  [3,4,8],      [6,8,11],    [5,8,12],  [4,8,13],   [4,7,14],   [3,7,15]  ]
   ])
 }} -->

<!-- ## Ranged Weapons -->

<!-- Ranged weapons function similarly to melee weapons, but have different styles. The five ranged weapon styles are Improvised, Payload, Precision, Repeating, and Spread. A Payload ranged weapon is something that delivers a heavy or explosive charge, like a grenade launcher or a cannon. A Precision ranged weapon is something that fires typically one round with a lot of power behind the shot, like a crossbow or a semi-automatic rifle. A Repeating ranged weapon is something that fires in clusters, like spears from a Hwacha or a burst from an automatic rifle. A Spread ranged weapon is something that typically fires some kind of shrapnel instead of an individual shot, like a shotgun or a sling filled with gravel. Improvised ranged weapons are typically either objects that fire projectiles but are not intended to be used as weapons, thrown weapons that are not intended to be thrown, or ranged weapons used in an unintended way. Examples of improvised ranged weapons are modified tranquilizer guns, a thrown battleaxe, and bashing with the butt of a rifle. See table C2 for ranged weapon damage by style and size. -->



<!-- TODO: Rework range increments-- this is way too complicated lmao -->

<!-- In addition, ranged weapons can be fired over varying ranges. Each ranged weapon typically has two distance values, a **close range distance** (typically 15m), an **effective range**, and a **maximum range**. When entering any combat, any character wielding a ranged weapon must choose whether they are aiming for close or distant targets. **Close range** firing allows the character to move and attack targets freely, as long as those targets are within their weapon's minimum range. **Long range** firing allows the character to fully utilize the effective and maximum range of their weapon by focusing further away from them, slowing their movement speed to half of their normal speed (Rules for speed are detailed on the [armor page).]({{url_for('armor')}}) While firing at long range, a ranged weapon can be used to attack any target closer than the weapon's maximum range. However, if the target is closer than the weapon's minimum range or beyond the weapon's effective range, the wielder must min their stat die for accuracy checks. -->

<!-- {{ renderWeaponTable("Ranged Weapon Damage Table",
    [
    ["",       "Improvised", "Payload", "Precision", "Repeating", "Spread"],
    ["Small",  [1,3,4],      [3,4,6],     [2,4,7],   [2,3,8],    [1,3,9]  ],
    ["Medium", [2,3,5],      [4,5,7],     [3,5,8],   [3,4,9],    [2,4,10] ],
    ["Large",  [3,4,8],      [5,8,12],    [4,8,13],  [4,7,14],   [3,7,15] ]
    ])
  }} -->

<!-- ## Elemental Weapons -->

<!-- Sometimes a weapon will behave in a way that utilizes a raw application of matter. This is usually the case when wielding some kind of weapon that utilizes raw chemical reactions, such as a homemade flamethrower or a piece of ancient alien technology. Often these weapons will deal damage in an area of effect, rather than a single target. Because they are typically area of effect weapons, these type of weapons are always considered to be large in size. However, they will have distinct levels of power associated with the damage they deal. The five styles of elemental weapons are Force, Gaseous, Liquid, Solid, and Plasma. Each style is fairly self explanatory, indicating the element which is manipulated by the weapon. See table C3 below for elemental weapon damage by style and power level. -->

<!-- {{ renderWeaponTable("Elemental Weapon Damage Table",
  [
  ["",            "Force",         "Gaseous",    "Liquid",   "Solid",   "Plasma" ],
  ["Low Power",   ["*","*","*"],   [3,4,6],      [2,4,7],   [2,3,8],    [1,3,9]  ],
  ["Medium Power",["*","*","*"],   [4,5,7],      [3,5,8],   [3,4,9],    [2,4,10] ],
  ["High Power",  ["*","*","*"],   [5,8,12],     [4,8,13],  [4,7,14],   [3,7,15] ],
  ])
}} -->