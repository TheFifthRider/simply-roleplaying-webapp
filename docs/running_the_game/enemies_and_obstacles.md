# Enemies and obstacles

Along with the responsibilities of creating tests, as a gamemaster you will likely need to create enemies and obstacles for your players to overcome. You can use the [character creation](../getting_started/creation.md) process to create the characters your players will tangle with, but there are a number of things on a character sheet that don't really matter for a character who only shows up for a maximum of a couple of scenes.

## Shorthand

I like using emoji in my stat blocks to make it easier for me to read them at a glance. These are entirely optional, but the examples listed here will use them. I recommend including some kind of graphical component in your enemy and obstacle notes -- I mostly play digitally so emoji are ideal, but consistent doodles or stickers would be great for paper play!

Here's a quick rundown of the symbols I use:

| Symbol | What it means |
| - | - |
| <i class="fa-solid fa-play"></i> | One action per symbol |
| <i class="fa-solid fa-arrow-rotate-left"></i> | An ability which reacts to circumstances |
| <i class="fa-solid fa-pause"></i> | An ability which telegraphs danger |
| <i class="fa-solid fa-play"></i><i class="fa-solid fa-pause"></i> | A telegraphed danger |
| <i class="fa-solid fa-arrows-rotate"></i> | An ability that provides some kind of passive benefit |
| <i class="fa-regular fa-square-full fa-fw"></i> | A space in a telegraphed danger that won't be affected |
| <span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i></span> | A space in a telegraphed danger that will be affected |
| <span style="color:var(--yellow);"><i class="fa-solid fa-star fa-fw"></i></span> | A space in a telegraphed danger that contains the character using it |



## Enemies

Enemies are simplified characters -- you usually don't need to know their attributes, skills, legacies, or backgrounds. Instead, an enemy will rely on their level and you can just assume that they have the appropriate skills, legacies, and backgrounds to always roll a number of d12s equal to their level. To make an enemy more interesting, you can give them strengths and weaknesses in the form of different levels for different attributes or [basic actions](../gameplay/basic_actions.md).

Enemies are usually either **bosses** or **minions**. There are many differences between the two, but one major is that **bosses** may take multiple [injuries](../character/health.md#injuries) before they are defeated, but minions only get one.

!!! error "Ruffian (level 1 minion)"
    6/6 Health
    
    <i class="ra ra-crossed-swords"></i> Attacks at level 2.
    
    Injuries:
    
    * [ ] Defeated

!!! error "Bandit Leader (level 1 boss)"
    6/6 Health
    
    <i class="fa-solid fa-cubes-stacked"></i> Hinders at level 2.
    
    Injuries:
    
    * [ ] \_\_\_\_\_\_\_\_
    * [ ] \_\_\_\_\_\_\_\_
    * [ ] Defeated: \_\_\_\_\_\_\_\_

### Enemy abilities

Once you've got the hang of enemies, you can start introducing [abilities](../character/abilities.md) to your enemies to make them still more interesting. It can be tempting to go overboard, but even just one ability can make an enemy interesting to fight. Three is often the most they need, unless you're making a particularly epic boss fight.

Enemies don't work as well with ability points as player characters because they only tend to use their abilities in the scene where they antagonize a character. If you do choose to give them ability points, make sure to only give them a small number. Alternatively, consider limiting enemy abilities with [requirements](../running_the_game/creating_abilities.md#requirements), such as putting a used ability on cooldown for a certain number of turns, or only unlocking some of their abilities after they've taken a certain number of injuries.

!!! error "**Kaiserwulf** (Level 9)"
    54/54 Health 
    
    * [ ] Defeated: \_\_\_\_\_\_\_\_
    
    <i class="ra ra-crossed-swords"></i> <i class="fa-solid fa-cubes-stacked"></i> **Maw of Mort**: <i class="ra ra-crossed-swords"></i> Attack for 9d12, then <i class="fa-solid fa-cubes-stacked"></i> Hinder your target with _chomped_ d12s using the same roll. They can't move while chomped.
    
    
    <i class="fa-solid fa-person-walking"></i> <i class="ra ra-crossed-swords"></i> <i class="ra ra-crossed-swords"></i> **Feral Lunge**: Move 5 spaces, then make two 9d12 attacks against all targets within close range. 

## Obstacles

Obstacles are like enemies, but even simpler. Usually they can perform one or two basic actions, and often in response to players doing something. Unlike enemies you usually can't just hit obstacles until they are defeated, so they'll have some other condition for defeating them.

!!! warning "Trapped Hallway (Level 1)"
    **To defeat:** Pass a difficulty 5 test to disarm the tripwire.
    
    If the party doesn't defeat the trap, the traps can't be deactivated! After each player's turn, activate the traps!
    
    <i class="ra ra-crossed-swords"></i> **Activate:** Swinging blades attack anyone in the hallway for 2d12!

Obstacles can also be almost indistinguishable from an enemy, except the party needs to do something clever to defeat them!

!!! warning "The Devouring Tree (Level 6)"
    **To defeat:** You can't defeat the Devouring Tree, but you can escape it! Roots block the stairs up from where you came and the stairs down deeper into the labyrinth. You can _Make Progress_ until you clear them, then escape beyond!
    
    60/60 Entrance
    
    60/60 Exit
    
    <i class="fa-solid fa-arrows-rotate"></i> **Aversion to Flame:** If a character uses fire as a part of a test against the tree, they get +10 to their roll.
    
    <i class="fa-solid fa-cubes-stacked"></i> **Branches and Vines Entangle:** Hinder a target by _entangling_ them as if you rolled a 60. They can't move while they are _entangled_. 
    
    <i class="ra ra-crossed-swords"></i> **Devouring Maw:** Drag anyone who is _entangled_ a short distance towards the maw and attack them for 9d12.

## Telegraphed danger

If you want to create a dangerous effect that your players can react to, you can **telegraph** the danger by giving it its own turn after a character does something to trigger it. Maybe a countdown started and you want to give your players a blast radius to scramble away from or a boss is going to unleash a powerful attack and you want them to be able to evade.

> <span style="color: var(--branding-color);"><i class="fa-solid fa-play"></i> <i class="fa-solid fa-play"></i> <i class="fa-solid fa-pause "></i> | **Roar and Unfurl Wings**</span>
> 
> The telegraphed danger **Curtain of Flames** can be passed to this round.
> 
> <span style="color: var(--branding-color);"><i class="fa-solid fa-play"></i><i class="fa-solid fa-pause"></i> | **Curtain of Flames**</span>
> 
> Attack the shaded spaces below for 7d12.
> 
> <i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i>  
> <i class="fa-regular fa-square-full fa-fw"></i><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><span style="color: var(--yellow);"><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i></span><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><i class="fa-regular fa-square-full fa-fw"></i>  
> <i class="fa-regular fa-square-full fa-fw"></i><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><span style="color: var(--yellow);"><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i></span><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><i class="fa-regular fa-square-full fa-fw"></i>  
> <i class="fa-regular fa-square-full fa-fw"></i><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><span style="color: var(--yellow);"><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i></span><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><i class="fa-regular fa-square-full fa-fw"></i>  
> <i class="fa-regular fa-square-full fa-fw"></i><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><i class="fa-regular fa-square-full fa-fw"></i>  
> <i class="fa-regular fa-square-full fa-fw"></i><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><i class="fa-regular fa-square-full fa-fw"></i>  
> <i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i>  

If you want to give a boss an attack pattern, you can create telegraphed dangers that lead into more telegraphed dangers.

> <span style="color: var(--branding-color);"><i class="fa-solid fa-play"></i> <i class="fa-solid fa-play"></i> <i class="fa-solid fa-play"></i> <i class="fa-solid fa-pause"></i> | **Roar and Unfurl Wings**</span>
> 
> Create the telegraphed danger **Blazing Takeoff**.
> 
> <span style="color: var(--branding-color);"><i class="fa-solid fa-play"></i><i class="fa-solid fa-pause"></i> <i class="fa-solid fa-pause"></i> | **Blazing Takeoff**</span>
> 
> Lift off and ignite the ground beneath you, attacking the shaded spaces below for 7d12, then lift off ten spaces into the air. Then, target a 3x3 area to land within 10 spaces and create the telegraphed danger **Meteor Slam**.
> 
> <i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i>  
> <i class="fa-regular fa-square-full fa-fw"></i><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><span style="color: var(--yellow);"><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i></span><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><i class="fa-regular fa-square-full fa-fw"></i>  
> <i class="fa-regular fa-square-full fa-fw"></i><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><span style="color: var(--yellow);"><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i></span><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><i class="fa-regular fa-square-full fa-fw"></i>  
> <i class="fa-regular fa-square-full fa-fw"></i><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><span style="color: var(--yellow);"><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i></span><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><i class="fa-regular fa-square-full fa-fw"></i>  
> <i class="fa-regular fa-square-full fa-fw"></i><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><i class="fa-regular fa-square-full fa-fw"></i>  
> <i class="fa-regular fa-square-full fa-fw"></i><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><i class="fa-regular fa-square-full fa-fw"></i>  
> <i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i>  
>
> <span style="color: var(--branding-color);"><i class="fa-solid fa-play"></i><i class="fa-solid fa-pause"></i> | **Meteor Slam**</span>
> 
> Slam into the area targetted by **Blazing Takeoff**, landing there and attacking the shaded spaces and anything you land on for 7d12.
> 
><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i>  
><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i>  
><i class="fa-regular fa-square-full fa-fw"></i><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i></span><span style="color: var(--yellow);"><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i></span><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i></span><i class="fa-regular fa-square-full fa-fw"></i>  
><i class="fa-regular fa-square-full fa-fw"></i><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i></span><span style="color: var(--yellow);"><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i></span><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i></span><i class="fa-regular fa-square-full fa-fw"></i>  
><i class="fa-regular fa-square-full fa-fw"></i><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i></span><span style="color: var(--yellow);"><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i><i class="fa-solid fa-star fa-fw"></i></span><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i></span><i class="fa-regular fa-square-full fa-fw"></i>  
><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><span style="color: var(--red);"><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i><i class="fa-solid fa-square-full fa-fw"></i></span><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i>  
><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i><i class="fa-regular fa-square-full fa-fw"></i>