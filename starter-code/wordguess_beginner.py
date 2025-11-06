"""
WORD GUESSING GAME - Beginner Starter Code
==========================================

This starter code provides the foundation for building a word guessing game
(similar to Hangman). A word has been selected and is displayed as underscores,
so you can see visual output immediately when you run this file.

YOUR TASKS:
1. Add functionality to let the player guess a letter
2. Update the display to reveal correctly guessed letters
3. Track incorrect guesses and set a limit
4. Create a game loop that continues until win or lose
5. Add enhancements based on your interests

RUN THIS FILE FIRST to see what you're starting with:
    python wordguess_beginner.py

Then work with Claude Code to build the game step by step.
"""

import random


def choose_word():
    """
    Selects a random word from a predefined list.

    Returns:
        str: A randomly selected word in uppercase
    """
    word_list = [
        "PYTHON",
        "CODING",
        "FUNCTION",
        "VARIABLE",
        "COMPUTER",
        "KEYBOARD",
        "PROGRAM",
        "ALGORITHM"
    ]
    return random.choice(word_list)


def display_word(word, guessed_letters):
    """
    Displays the word with guessed letters revealed and others as underscores.

    Parameters:
        word (str): The secret word to display
        guessed_letters (set): Set of letters the player has guessed

    Returns:
        str: The display string with underscores for unguessed letters
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def main():
    """
    Main function to run the game.

    Right now, this demonstrates the basic display functionality.
    You'll expand this to include guessing, tracking, and game logic.
    """
    print("=" * 50)
    print("  WELCOME TO THE WORD GUESSING GAME!")
    print("=" * 50)

    # Choose a secret word
    secret_word = choose_word()

    # Start with no guessed letters
    guessed_letters = set()

    print("\nYour mission: Guess the secret word letter by letter!")
    print(f"\nThe word has {len(secret_word)} letters:\n")

    # Display the word (all underscores at the start)
    print(display_word(secret_word, guessed_letters))

    # For demonstration, let's pretend the player guessed 'A' and 'O'
    print("\n--- Demo: What it looks like after guessing A and O ---")
    guessed_letters.add('A')
    guessed_letters.add('O')
    print(display_word(secret_word, guessed_letters))

    print("\n" + "=" * 50)
    print("This is your starting point!")
    print("Next step: Add functionality for the player to guess letters.")
    print("=" * 50)


if __name__ == "__main__":
    main()


"""
SUGGESTED PROMPTS FOR CLAUDE CODE:
===================================

After running this starter code, try these prompts one at a time:

1. "Add a function called get_letter_guess that asks the player to enter a
   letter, validates that it's a single letter, and returns it in uppercase."

2. "Create a simple loop that lets the player guess 5 letters, displaying
   the word state after each guess. Don't worry about win/lose logic yet,
   just let them guess."

3. "Add a variable to track wrong guesses. When the player guesses a letter
   not in the word, increment the wrong guess counter and display it."

4. "Add win detection: if all letters in the word have been guessed, the
   player wins. Add lose detection: if wrong guesses reach 6, the player loses."

5. "Create the full game loop that continues until the player wins or loses,
   then displays an appropriate message."

6. "Add ASCII art that shows a simple hangman figure that progresses with
   each wrong guess."

Remember: Test after each change! Make sure each piece works before moving on.
"""
