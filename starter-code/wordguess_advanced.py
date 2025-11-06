"""
WORD GUESSING GAME - Advanced Starter Code
==========================================

This starter code provides word selection, display, and basic input handling.
Your focus will be on game logic, tracking guesses, and win/lose conditions.

RUN THIS FILE FIRST to see what you're starting with:
    python wordguess_advanced.py

The program will let you guess a few letters to see the basic mechanics.

YOUR TASKS:
1. Add comprehensive tracking of guessed letters (both correct and incorrect)
2. Implement win/lose conditions with appropriate limits
3. Create a full game loop that continues until win or lose
4. Add visual feedback (ASCII art, progress indicators)
5. Add enhancements: categories, difficulty levels, hints, etc.
"""

import random


def choose_word(category="general"):
    """
    Selects a random word from a category.

    Parameters:
        category (str): The category to choose from

    Returns:
        str: A randomly selected word in uppercase
    """
    word_lists = {
        "general": ["PYTHON", "CODING", "FUNCTION", "VARIABLE", "COMPUTER"],
        "animals": ["ELEPHANT", "GIRAFFE", "PENGUIN", "DOLPHIN", "BUTTERFLY"],
        "food": ["PIZZA", "CHOCOLATE", "SANDWICH", "AVOCADO", "SPAGHETTI"]
    }

    words = word_lists.get(category, word_lists["general"])
    return random.choice(words)


def display_word(word, guessed_letters):
    """
    Displays the word with guessed letters revealed.

    Parameters:
        word (str): The secret word
        guessed_letters (set): Letters the player has guessed

    Returns:
        str: Display string with underscores for unguessed letters
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def get_letter_guess(already_guessed):
    """
    Gets a valid letter guess from the player.

    Parameters:
        already_guessed (set): Letters already guessed

    Returns:
        str: A valid uppercase letter that hasn't been guessed yet

    Note: This has basic validation but you may want to enhance error handling.
    """
    while True:
        guess = input("\nGuess a letter: ").upper().strip()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if not guess.isalpha():
            print("Please enter a letter (A-Z).")
            continue

        if guess in already_guessed:
            print(f"You already guessed {guess}. Try a different letter.")
            continue

        return guess


def main():
    """
    Main function demonstrating the basic game mechanics.

    This is a simplified version that lets you make a few guesses to test.
    You'll expand this into a full game with win/lose conditions.
    """
    print("=" * 50)
    print("  WORD GUESSING GAME - Advanced Starter")
    print("=" * 50)

    # Choose a secret word
    secret_word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print(f"\nGuess the {len(secret_word)}-letter word!")
    print("(This demo lets you make 3 guesses to test the mechanics)\n")

    # Simple demonstration: 3 guesses
    for turn in range(3):
        print(f"\nWord: {display_word(secret_word, guessed_letters)}")
        print(f"Wrong guesses: {wrong_guesses}")

        # Get a guess
        guess = get_letter_guess(guessed_letters)
        guessed_letters.add(guess)

        # Check if it's in the word
        if guess in secret_word:
            print(f"✓ Good guess! {guess} is in the word.")
        else:
            print(f"✗ Sorry, {guess} is not in the word.")
            wrong_guesses += 1

    # Show final state
    print(f"\n{display_word(secret_word, guessed_letters)}")
    print(f"\nThe secret word was: {secret_word}")

    print("\n" + "=" * 50)
    print("Demo complete! Now build the full game:")
    print("  - Add proper win/lose conditions")
    print("  - Create full game loop")
    print("  - Add visual feedback (ASCII art)")
    print("  - Add enhancements (hints, categories, etc.)")
    print("=" * 50)


if __name__ == "__main__":
    main()


"""
SUGGESTED PROMPTS FOR CLAUDE CODE:
===================================

After running this starter code, work on these features:

1. "Create a function called check_win that returns True if all letters in
   the secret word have been guessed."

2. "Add a constant for maximum wrong guesses (like 6) and create a function
   called check_lose that returns True if wrong guesses reach that limit."

3. "Create a function that displays a simple ASCII art hangman that changes
   based on the number of wrong guesses."

4. "Rewrite the main game loop to continue until the player wins or loses,
   checking after each guess and ending with an appropriate message."

5. "Add a display function that shows: the current word state, wrong guesses
   remaining, letters already guessed, and the hangman figure."

6. "Add a play_again feature that asks if the player wants another game."

7. For enhancements, consider:
   - Let the player choose a category before starting
   - Add a hint system (reveal one random letter)
   - Add difficulty levels (more/fewer allowed wrong guesses)
   - Score system based on remaining guesses
   - Two-player mode where one player enters the secret word
   - Custom word lists loaded from a file

Remember to test thoroughly after each addition!
"""
