# Student Handout: Turn-Based RPG Battle Game

## Project Overview
Build a turn-based battle game (like Pokémon or Final Fantasy) that runs in the terminal!

**What you'll create:**
- Player character with health, attack power, and name
- Enemy character with health and attack power
- Turn-based combat system
- Different attack options
- Victory and defeat conditions

**Time:** 80 minutes  
**Difficulty:** ⭐⭐⭐ Intermediate  
**Language:** Python

---

## What You'll Learn
- Managing game state across turns
- Working with multiple functions
- Data structures for characters
- Random number generation for combat
- Game loop design
- Balancing game mechanics

---

## Phase 1: Planning (15 minutes)

### Questions to Answer Together

Before writing any code, discuss:

1. **What information defines a character?**
   - Name
   - Health (HP)
   - Attack power
   - Defense? Speed? Special abilities?
   - Start simple - you can add more later

2. **How does combat work?**
   - Who goes first?
   - What actions can you take? (attack, defend, use item?)
   - How much damage does an attack do?
   - Is there randomness involved?

3. **What's our MVP (Minimum Viable Product)?**
   - Create player character ✓
   - Create enemy character ✓
   - Players take turns attacking ✓
   - Display health after each turn ✓
   - Declare winner when someone reaches 0 HP ✓

4. **What features can we add later?**
   - Multiple attack types (normal, heavy, critical)
   - Defend/dodge actions
   - Healing items/spells
   - Multiple enemies
   - Experience points and leveling
   - Special abilities

### Draw Your Game Flow

On paper, sketch out:
```
Create Player (name, HP, attack)
Create Enemy (name, HP, attack)
  ↓
Display both character stats
  ↓
Player's turn - choose action
  ↓
Calculate and apply damage
  ↓
Check if enemy defeated
  ↓ No
Enemy's turn - attack player
  ↓
Calculate and apply damage
  ↓
Check if player defeated
  ↓ No
Back to player's turn
```

---

## Phase 2: Building with Claude Code (35 minutes)

### 🎯 Step 1: Create Characters (8 minutes)

**Your prompt to Claude Code:**
```
Help me create a turn-based battle game in Python. Start by creating 
two characters: a player and an enemy. Each should have a name, 
health (HP), and attack power. Use a dictionary or simple variables 
to store this information. Display both characters' stats.
```

**Test it!** Run your code. Do you see both characters' information?

**Understanding check:**
- How is character data stored?
- Can you change a character's health?
- What data structure would work best? (dictionary? variables? class?)

---

### 🎯 Step 2: Basic Attack (10 minutes)

**Your prompt to Claude Code:**
```
Add a function where the player can attack the enemy. When the player 
attacks, subtract the player's attack power from the enemy's health. 
Display how much damage was dealt and show the enemy's remaining health. 
Just do one attack for now.
```

**Test it!** Run an attack. Does the enemy's health decrease correctly?

**Understanding check:**
- How is damage calculated?
- How is health updated?
- What happens if health goes negative?

---

### 🎯 Step 3: Both Sides Attack (10 minutes)

**Your prompt to Claude Code:**
```
Now add the enemy's turn. After the player attacks, the enemy should 
automatically attack back. Display the damage dealt to the player and 
show both characters' remaining health. Do this for just one round 
(player attacks, then enemy attacks).
```

**Test it!** Run one round. Do both characters lose health?

**Understanding check:**
- Who goes first? Why?
- How do you track whose turn it is?
- What's the sequence of events?

---

### 🎯 Step 4: Battle Loop (12 minutes)

**Your prompt to Claude Code:**
```
Create a battle loop that continues until either the player or enemy 
reaches 0 health or below. Each turn, show the current stats, let the 
player attack, then let the enemy attack. When someone reaches 0 HP, 
display who won and end the game.
```

**Test it!** Play through a complete battle. 
- Does it end when someone dies?
- Is the winner displayed correctly?
- Are stats shown each turn?

**Understanding check:**
- What condition keeps the loop running?
- What condition stops the loop?
- When is health checked?
- What happens on the last turn?

---

## Phase 3: Enhancements (20 minutes)

Choose features to add based on your progress:

### 🌟 Enhancement 1: Player Choices
**Prompt:**
```
Instead of auto-attacking, give the player a menu each turn:
1. Attack (normal attack)
2. Heavy Attack (more damage but might miss)
3. Defend (reduce damage taken next turn)

Let them choose what to do each turn.
```

### 🌟 Enhancement 2: Damage Variation
**Prompt:**
```
Add randomness to combat. Instead of fixed damage, make attacks do 
damage in a range. For example, if attack power is 10, damage could 
be between 8-12. This makes each battle different. Use the random 
module.
```

### 🌟 Enhancement 3: Critical Hits
**Prompt:**
```
Add a 20% chance for attacks to be critical hits that do double damage. 
When a critical hit happens, display an exciting message like "CRITICAL 
HIT!" Make the feedback satisfying.
```

### 🌟 Enhancement 4: Healing Items
**Prompt:**
```
Give the player 3 health potions at the start. Add a "Use Potion" option 
to the combat menu. When used, restore 30 HP to the player. Show how 
many potions remain. Can't use if you have none left.
```

### 🌟 Enhancement 5: Multiple Enemies
**Prompt:**
```
After defeating one enemy, spawn a new, slightly stronger enemy. Track 
how many enemies the player has defeated. The player's health carries 
over between fights. Game ends when player is defeated.
```

### 🌟 Enhancement 6: Character Classes
**Prompt:**
```
Let the player choose a class at the start (Warrior, Mage, Rogue). 
Each class has different starting stats:
- Warrior: High HP, medium attack
- Mage: Low HP, high attack  
- Rogue: Medium HP, medium attack, higher crit chance
```

### 🌟 Enhancement 7: Experience and Leveling
**Prompt:**
```
Award experience points when enemies are defeated. When the player 
gains enough XP, they level up and get stat increases (more HP, more 
attack). Show level and XP progress after each battle.
```

---

## Tips for Success

### For the Beginner:
- **Think about state** - what needs to be tracked turn-by-turn?
- **Print everything** - see health, damage, all changes
- **Test battles** - play through multiple times
- **Understand the loop** - when does it check for victory?

### For the Advanced Student:
- **Discuss functions** - how to organize code cleanly
- **Explain random module** - how randomness works
- **Consider balance** - is the game too easy/hard?
- **Suggest refactoring** - how to make code clearer

### For Both:
✅ Balance the numbers - too easy is boring, too hard is frustrating  
✅ Give good feedback - make attacks feel impactful  
✅ Test edge cases - what if damage exceeds remaining HP?  
✅ Make it fun - add personality to messages  
✅ Save frequently - test after each feature  

---

## Debugging Tips

**Problem:** "Battle never ends"
- Check: Is health actually decreasing?
- Check: Is your loop condition checking health correctly?
- Check: Are you using the right comparison operator?

**Problem:** "Health goes negative"
- Solution: That's okay! Or add a check to set it to 0 minimum
- Check: Does your victory condition check for <= 0?

**Problem:** "Same damage every time"
- Check: Are you using random.randint()?
- Check: Is the random module imported?

**Problem:** "Enemy doesn't attack"
- Check: Is enemy attack code inside the loop?
- Check: Is it after the health check?

**Problem:** "Player always wins/loses"
- Check: Is the damage balanced?
- Try: Adjust attack values for fair fights

---

## Sample Session with Claude Code

Here's what a good back-and-forth looks like:

**You:** "Help me make a turn-based battle game. Start with creating a player and enemy with health and attack stats."

**Claude Code:** [Creates characters with stats]

**You:** "Good! Now let the player attack once and show the enemy's health decrease."

**Claude Code:** [Adds attack function]

**You:** "It works, but the damage seems high. How can I make attacks do a random amount in a range?"

**Claude Code:** [Adds random damage]

**You:** "Perfect! Now let's make it turn-based. After the player attacks, the enemy should attack back."

**Claude Code:** [Adds enemy turn]

**You:** "Great! How do I make this repeat until someone wins?"

**Claude Code:** [Adds battle loop]

---

## Challenge Questions

Once your basic game works, try to answer these:

1. How would you save the player's progress to a file?
2. Could you add elemental types (fire/water/grass) with advantages?
3. How would you implement a boss battle with multiple phases?
4. What if you wanted party-based combat (multiple player characters)?
5. How could you add status effects (poison, stun, etc.)?

---

## Code Structure Tips

Your final code might have functions like:
- `create_character(name, hp, attack)` - creates character dictionary
- `display_stats(character)` - shows character info
- `player_attack(player, enemy)` - handles player's attack
- `enemy_attack(player, enemy)` - handles enemy's attack
- `calculate_damage(attacker, defender)` - determines damage amount
- `is_alive(character)` - checks if character still has HP
- `battle()` - main battle loop
- `main()` - game setup and start

Don't worry if your structure is different! Many approaches work.

---

## Balancing Tips

For a fair and fun game:

**Starting Stats Example:**
- Player: 100 HP, 15-20 attack
- Enemy: 80 HP, 10-15 attack

**Guidelines:**
- Battle should last 5-8 turns ideally
- Player should win ~60% of the time
- Add randomness so outcome isn't guaranteed
- If too easy: Increase enemy HP or attack
- If too hard: Decrease enemy HP or attack

**Test by playing 5-10 battles and adjusting!**

---

## Making Combat Feel Good

Add personality to your messages:

**Boring:**
```
Player attacks. Enemy takes 15 damage.
Enemy attacks. Player takes 12 damage.
```

**Better:**
```
You swing your sword! Dealt 15 damage to the Goblin!
The Goblin counterattacks! You take 12 damage. Ouch!

💚 Player HP: 88/100
💀 Goblin HP: 45/60
```

Small touches make big differences!

---

## Reflection (End of Session)

Think about:
- How did you manage game state?
- What made the combat feel fun or not fun?
- How did randomness affect gameplay?
- What was most challenging about this project?
- If you could start over, what would you do differently?

---

## Extension Ideas for Next Time

- Add equipment (weapons, armor) that boost stats
- Create different enemy types with unique abilities
- Add a shop to buy items between battles
- Implement a story with dialogue
- Create a save/load system
- Add animations or ASCII art
- Make a tournament mode against multiple enemies

---

Good luck creating your battle system! Remember: balance is key. Test frequently and adjust numbers to make it fun!
