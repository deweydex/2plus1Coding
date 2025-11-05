"""
TURN-BASED RPG BATTLE GAME - Sample Solution
============================================
This is a working implementation of a turn-based battle game.
This code demonstrates the MVP (Minimum Viable Product) version.

Features included:
- Player and enemy characters with stats
- Turn-based combat system
- Attack with damage variation
- Health tracking
- Victory/defeat conditions
- Multiple rounds with stat carry-over
"""

import random


def create_character(name, hp, attack, defense=0):
    """
    Create a character dictionary with stats.
    Using a dictionary makes it easy to add more stats later.
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
    Display a character's current stats in a readable format.
    """
    hp_bar = '█' * (character['hp'] // 5)  # Visual HP bar
    print(f"{character['name']}: {character['hp']}/{character['max_hp']} HP {hp_bar}")


def display_battle_status(player, enemy):
    """
    Show the current status of both fighters.
    """
    print("\n" + "=" * 50)
    display_stats(player)
    display_stats(enemy)
    print("=" * 50 + "\n")


def calculate_damage(attacker, defender):
    """
    Calculate damage dealt by attacker to defender.
    Adds some randomness to make battles more interesting.
    Base damage is attacker's attack power, with +/- 20% variation.
    """
    base_damage = attacker['attack']
    
    # Add randomness: damage ranges from 80% to 120% of attack power
    variation = random.randint(-2, 2)
    damage = base_damage + variation
    
    # Subtract defender's defense (if any)
    damage -= defender['defense']
    
    # Damage can't be negative
    damage = max(damage, 1)
    
    return damage


def attack(attacker, defender):
    """
    Perform an attack from attacker to defender.
    Returns the damage dealt.
    """
    damage = calculate_damage(attacker, defender)
    defender['hp'] -= damage
    
    # Make sure HP doesn't go below 0
    defender['hp'] = max(defender['hp'], 0)
    
    return damage


def is_alive(character):
    """
    Check if a character is still alive (HP > 0).
    """
    return character['hp'] > 0


def player_turn(player, enemy):
    """
    Handle the player's turn with action choices.
    """
    print(f"\n{player['name']}'s Turn!")
    print("Choose your action:")
    print("1. Attack")
    print("2. Defend (reduce damage taken next turn)")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-2): "))
            
            if choice == 1:
                damage = attack(player, enemy)
                print(f"\n⚔️  You attack the {enemy['name']}!")
                print(f"💥 Dealt {damage} damage!")
                
                # Check for critical hit (20% chance)
                if random.random() < 0.2:
                    bonus_damage = damage // 2
                    enemy['hp'] -= bonus_damage
                    enemy['hp'] = max(enemy['hp'], 0)
                    print(f"🔥 CRITICAL HIT! Bonus {bonus_damage} damage!")
                
                return False  # Not defending
                
            elif choice == 2:
                print(f"\n🛡️  You take a defensive stance!")
                return True  # Is defending
                
            else:
                print("Please enter 1 or 2.")
                
        except ValueError:
            print("Please enter a valid number.")


def enemy_turn(player, enemy, player_defending):
    """
    Handle the enemy's turn (automatic).
    Enemy always attacks, but damage is reduced if player is defending.
    """
    print(f"\n{enemy['name']}'s Turn!")
    
    damage = attack(enemy, player)
    
    # Reduce damage if player was defending
    if player_defending:
        damage = damage // 2
        print(f"\n🛡️  Your defense reduces the damage!")
    
    print(f"⚔️  The {enemy['name']} attacks you!")
    print(f"💥 You take {damage} damage!")


def battle(player, enemy):
    """
    Main battle loop between player and enemy.
    Returns True if player wins, False if player loses.
    """
    print("\n" + "🗡️ " * 15)
    print(f"⚔️  A wild {enemy['name']} appears!")
    print("🗡️ " * 15)
    
    player_defending = False
    
    while is_alive(player) and is_alive(enemy):
        display_battle_status(player, enemy)
        
        # Player's turn
        player_defending = player_turn(player, enemy)
        
        # Check if enemy is defeated
        if not is_alive(enemy):
            display_battle_status(player, enemy)
            print(f"\n🎉 Victory! You defeated the {enemy['name']}!")
            return True
        
        # Small pause for readability
        input("\nPress Enter to continue...")
        
        # Enemy's turn
        enemy_turn(player, enemy, player_defending)
        
        # Check if player is defeated
        if not is_alive(player):
            display_battle_status(player, enemy)
            print(f"\n💀 Defeat! You were defeated by the {enemy['name']}!")
            return False
    
    return is_alive(player)


def create_enemy(difficulty=1):
    """
    Create an enemy with stats based on difficulty level.
    Difficulty increases with each battle won.
    """
    enemy_names = ['Goblin', 'Orc', 'Troll', 'Dragon', 'Dark Knight']
    
    # Select enemy name based on difficulty
    name_index = min(difficulty - 1, len(enemy_names) - 1)
    name = enemy_names[name_index]
    
    # Scale stats with difficulty
    hp = 60 + (difficulty * 15)
    attack = 8 + (difficulty * 2)
    
    return create_character(name, hp, attack)


def heal_player(player, amount):
    """
    Heal the player by the specified amount.
    Can't exceed max HP.
    """
    player['hp'] += amount
    player['hp'] = min(player['hp'], player['max_hp'])


def main():
    """
    Main game function with multiple battles.
    """
    print("\n" + "⚔️ " * 20)
    print(" " * 15 + "BATTLE ARENA")
    print("⚔️ " * 20 + "\n")
    
    # Get player name
    player_name = input("Enter your warrior's name: ").strip()
    if not player_name:
        player_name = "Hero"
    
    # Create player character
    player = create_character(player_name, 100, 15)
    
    print(f"\nWelcome, {player_name}!")
    print("Prepare for battle!\n")
    
    enemies_defeated = 0
    difficulty = 1
    
    # Battle loop
    while True:
        # Create enemy for this round
        enemy = create_enemy(difficulty)
        
        # Start battle
        won = battle(player, enemy)
        
        if won:
            enemies_defeated += 1
            print(f"\n✨ Enemies defeated: {enemies_defeated}")
            
            # Heal player between battles (partial recovery)
            heal_amount = 30
            heal_player(player, heal_amount)
            print(f"💚 You recover {heal_amount} HP!")
            
            # Ask if player wants to continue
            continue_game = input("\nFace another enemy? (yes/no): ").lower()
            if continue_game not in ['yes', 'y']:
                print(f"\n🏆 You defeated {enemies_defeated} enemies!")
                print("Thanks for playing!")
                break
            
            # Increase difficulty for next battle
            difficulty += 1
            print("\n⚡ The enemies grow stronger...")
            
        else:
            # Player lost
            print(f"\n🏆 Final Score: {enemies_defeated} enemies defeated")
            print("Thanks for playing!")
            break


# Run the game if this file is executed directly
if __name__ == "__main__":
    main()


"""
ENHANCEMENTS YOU COULD ADD:
===========================

1. Character Classes:
   - Warrior: High HP, medium attack
   - Mage: Low HP, high attack
   - Rogue: Medium HP, medium attack, higher crit chance
   - Let player choose at start

2. Special Abilities:
   - Each class gets unique abilities
   - Mage: Fireball (high damage, cooldown)
   - Warrior: Power Strike (2x damage)
   - Rogue: Dodge (avoid next attack)

3. Items and Inventory:
   - Health Potions: Restore HP
   - Attack Potions: Boost attack temporarily
   - Defense Potions: Boost defense temporarily
   - Limited quantities

4. Experience and Leveling:
   - Gain XP for defeating enemies
   - Level up increases stats
   - Show level and progress bar

5. Equipment System:
   - Weapons: Increase attack
   - Armor: Increase defense
   - Find/buy better equipment

6. Shop Between Battles:
   - Buy potions
   - Upgrade equipment
   - Earn gold from victories

7. Status Effects:
   - Poison: Damage over time
   - Stun: Skip turn
   - Regeneration: Heal over time
   - Burn: Damage and reduced attack

8. Boss Battles:
   - Every 5 enemies, face a boss
   - Bosses have more HP and special moves
   - Extra rewards for victory

9. Save/Load System:
   - Save game progress to file
   - Load and continue previous game

10. Multiple Enemy Types:
    - Fast enemies: High attack, low HP
    - Tank enemies: High HP, low attack
    - Balanced enemies: Medium stats
    - Each requires different strategy

11. Combo System:
    - Build combo meter with consecutive hits
    - Unlock special moves at high combo
    - Combo breaks if you miss or get hit

12. Party System:
    - Control multiple characters
    - Switch between party members
    - Different roles (tank, healer, DPS)
"""
