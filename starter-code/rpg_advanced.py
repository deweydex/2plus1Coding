"""
TURN-BASED RPG BATTLE - Advanced Starter Code
==============================================

This starter code provides character creation, stat display, and a basic
attack function. Your focus will be on battle mechanics, player choices,
and game balance.

RUN THIS FILE FIRST to see what you're starting with:
    python rpg_advanced.py

The program demonstrates one attack to show the basic mechanics.

YOUR TASKS:
1. Create a complete turn-based battle system
2. Add player action choices (attack, defend, special abilities)
3. Implement victory/defeat conditions
4. Add strategic elements (abilities, items, status effects)
5. Balance gameplay for an enjoyable experience
"""

import random


def create_character(name, hp, attack, defense=0):
    """
    Creates a character dictionary with combat stats.

    Parameters:
        name (str): Character name
        hp (int): Health points
        attack (int): Base attack power
        defense (int): Damage reduction

    Returns:
        dict: Character data structure
    """
    return {
        'name': name,
        'max_hp': hp,
        'hp': hp,
        'attack': attack,
        'defense': defense,
        'defending': False  # Track if character is defending this turn
    }


def display_stats(character):
    """
    Displays character stats with a visual HP bar.

    Parameters:
        character (dict): The character to display
    """
    hp_percentage = max(0, character['hp'] / character['max_hp'])
    bar_length = 20
    filled = int(bar_length * hp_percentage)
    bar = '█' * filled + '░' * (bar_length - filled)

    status = " [DEFENDING]" if character.get('defending', False) else ""
    print(f"\n{character['name']}{status}")
    print(f"HP: {character['hp']}/{character['max_hp']} [{bar}]")
    print(f"ATK: {character['attack']} | DEF: {character['defense']}")


def calculate_damage(attacker, defender):
    """
    Calculates damage dealt from attacker to defender.

    Damage is based on attack power minus defense, with randomness added.
    Defending doubles defense for that turn.

    Parameters:
        attacker (dict): The attacking character
        defender (dict): The defending character

    Returns:
        int: The damage dealt (minimum 1)
    """
    base_damage = attacker['attack']

    # Add randomness: ±20% variation
    variation = random.randint(-2, 2)
    damage = base_damage + variation

    # Apply defense (doubled if defending)
    defense_value = defender['defense']
    if defender.get('defending', False):
        defense_value *= 2

    damage -= defense_value

    # Minimum damage is 1
    return max(1, damage)


def attack(attacker, defender):
    """
    Executes an attack from attacker to defender.

    Parameters:
        attacker (dict): The attacking character
        defender (dict): The defending character

    Returns:
        int: Damage dealt
    """
    damage = calculate_damage(attacker, defender)
    defender['hp'] -= damage
    defender['hp'] = max(0, defender['hp'])  # Don't go below 0

    return damage


def is_alive(character):
    """
    Checks if a character is still alive.

    Parameters:
        character (dict): The character to check

    Returns:
        bool: True if HP > 0, False otherwise
    """
    return character['hp'] > 0


def main():
    """
    Main function demonstrating one attack.

    You'll expand this into a full turn-based battle system with
    player choices and strategic options.
    """
    print("=" * 50)
    print("  RPG BATTLE SYSTEM - Advanced Starter")
    print("=" * 50)

    # Create characters
    player = create_character("Hero", hp=100, attack=18, defense=5)
    enemy = create_character("Orc Warrior", hp=80, attack=15, defense=3)

    print("\n" + "-" * 50)
    print("Battle Start!")
    print("-" * 50)

    # Show initial stats
    display_stats(player)
    display_stats(enemy)

    print("\n" + "-" * 50)
    print("Demonstrating one round of combat:")
    print("-" * 50)

    # Player attacks
    print(f"\n{player['name']} attacks!")
    damage = attack(player, enemy)
    print(f"Dealt {damage} damage to {enemy['name']}!")
    display_stats(enemy)

    # Enemy attacks back (if still alive)
    if is_alive(enemy):
        print(f"\n{enemy['name']} counterattacks!")
        damage = attack(enemy, player)
        print(f"Dealt {damage} damage to {player['name']}!")
        display_stats(player)

    print("\n" + "=" * 50)
    print("Demo complete! Now build the full battle system:")
    print("  - Add player action choices (attack/defend/special)")
    print("  - Create battle loop until victory or defeat")
    print("  - Add special abilities and strategic elements")
    print("  - Balance difficulty for good gameplay")
    print("=" * 50)


if __name__ == "__main__":
    main()


"""
SUGGESTED PROMPTS FOR CLAUDE CODE:
===================================

After running this starter code, work on these features:

1. "Create a function called get_player_action that asks the player to choose
   an action (1: Attack, 2: Defend) and returns their choice."

2. "Add a defend function that sets the character's 'defending' flag to True,
   which doubles their defense for one turn."

3. "Create a player_turn function that gets the player's choice and executes
   the chosen action. Include stat display after the action."

4. "Create an enemy_turn function where the enemy decides to attack (or defend
   if HP is low). You can start with simple logic."

5. "Build the main battle loop that alternates between player and enemy turns
   until one character's HP reaches 0. Display victory or defeat message."

6. "Add a special ability: a powerful attack that the player can use once per
   battle. Track whether it's been used."

7. For enhancements, consider:
   - Multiple enemies in sequence (gauntlet mode)
   - Character classes with different stats and abilities
   - Item system (potions, equipment)
   - Status effects (poison, stun, buff)
   - Experience and leveling up
   - Multiple special abilities with cooldowns
   - Better enemy AI (strategic decisions)
   - Boss battles with special mechanics

Remember to test thoroughly and balance the difficulty!
"""
