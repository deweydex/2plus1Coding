"""
TURN-BASED RPG BATTLE - Beginner Starter Code
==============================================

This starter code provides character creation with stats display, so you can
see the characters immediately when you run this file.

YOUR TASKS:
1. Add an attack function where one character damages another
2. Create a simple battle loop with turn-by-turn combat
3. Add win/lose conditions
4. Add player choice (attack, defend, special ability)
5. Add enhancements based on your interests

RUN THIS FILE FIRST to see what you're starting with:
    python rpg_beginner.py

Then work with Claude Code to build the battle system step by step.
"""

def create_character(name, hp, attack, defense=0):
    """
    Creates a character with stats.

    Parameters:
        name (str): Character's name
        hp (int): Health points
        attack (int): Attack power
        defense (int): Defense rating (reduces damage taken)

    Returns:
        dict: A dictionary containing the character's stats
    """
    return {
        'name': name,
        'max_hp': hp,
        'hp': hp,
        'attack': attack,
        'defense': defense
    }


def display_stats(character):
    """
    Displays a character's current stats.

    Parameters:
        character (dict): The character to display
    """
    # Create a visual HP bar
    hp_percentage = character['hp'] / character['max_hp']
    bar_length = 20
    filled = int(bar_length * hp_percentage)
    bar = '█' * filled + '░' * (bar_length - filled)

    print(f"\n{character['name']}")
    print(f"HP: {character['hp']}/{character['max_hp']} [{bar}]")
    print(f"Attack: {character['attack']} | Defense: {character['defense']}")


def main():
    """
    Main function demonstrating character creation and display.

    You'll expand this to include combat, turns, and victory conditions.
    """
    print("=" * 50)
    print("  WELCOME TO RPG BATTLE!")
    print("=" * 50)

    # Create a player character
    player = create_character("Hero", hp=100, attack=15, defense=5)

    # Create an enemy character
    enemy = create_character("Goblin", hp=50, attack=10, defense=2)

    print("\nYour Character:")
    display_stats(player)

    print("\nYour Opponent:")
    display_stats(enemy)

    print("\n" + "=" * 50)
    print("This is your starting point!")
    print("Next step: Add an attack function so characters can battle.")
    print("=" * 50)


if __name__ == "__main__":
    main()


"""
SUGGESTED PROMPTS FOR CLAUDE CODE:
===================================

After running this starter code, try these prompts one at a time:

1. "Add a function called attack that takes an attacker and a defender,
   calculates damage (attack minus defense, with some randomness), reduces
   the defender's HP, and returns the damage dealt."

2. "Create a function that checks if a character is still alive (HP > 0)."

3. "Make a simple battle where the player attacks first, then the enemy
   attacks back. Display stats after each attack. Just do one round."

4. "Create a full battle loop that continues turn-by-turn until either the
   player or enemy reaches 0 HP, then announce the winner."

5. "Add player choice: each turn, ask if they want to attack or defend.
   Defending temporarily increases defense for that turn."

6. "Add a special ability that the player can use once per battle that does
   extra damage."

Remember: Test after each change! Make sure each piece works before moving on.
"""
