"""
WORD GUESSING GAME - Sample Solution
====================================
This is a working implementation of a word guessing game (Hangman style).
This code demonstrates the MVP (Minimum Viable Product) version.

Features included:
- Random word selection from a list
- Display word with underscores for unguessed letters
- Track guessed letters
- Limited number of wrong guesses
- Input validation
- Win/loss detection
- Play again option
"""

import random


def get_word_list():
    """
    Return a list of words to choose from.
    You can expand this list or organize by categories.
    """
    words = [
        'PYTHON', 'JAVA', 'JAVASCRIPT', 'COMPUTER',
        'PROGRAMMING', 'ALGORITHM', 'FUNCTION', 'VARIABLE',
        'DATABASE', 'NETWORK', 'SOFTWARE', 'HARDWARE',
        'INTERNET', 'KEYBOARD', 'MONITOR', 'DEBUGGING'
    ]
    return words


def pick_random_word(word_list):
    """
    Select and return a random word from the list.
    """
    return random.choice(word_list).upper()


def display_word(word, guessed_letters):
    """
    Display the word with underscores for letters not yet guessed.
    Example: If word is "PYTHON" and guessed_letters is ['P', 'O']
             Display: "P _ _ O _"
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def display_hangman(wrong_count):
    """
    Display ASCII art hangman based on number of wrong guesses.
    This is optional but makes the game more visual!
    """
    stages = [
        # 0 wrong guesses
        """
           --------
           |      |
           |
           |
           |
           |
        """,
        # 1 wrong guess
        """
           --------
           |      |
           |      O
           |
           |
           |
        """,
        # 2 wrong guesses
        """
           --------
           |      |
           |      O
           |      |
           |
           |
        """,
        # 3 wrong guesses
        """
           --------
           |      |
           |      O
           |     /|
           |
           |
        """,
        # 4 wrong guesses
        """
           --------
           |      |
           |      O
           |     /|\\
           |
           |
        """,
        # 5 wrong guesses
        """
           --------
           |      |
           |      O
           |     /|\\
           |     /
           |
        """,
        # 6 wrong guesses (game over)
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |
        """
    ]
    print(stages[wrong_count])


def get_guess(guessed_letters):
    """
    Get a valid letter guess from the player.
    Validates input and checks if already guessed.
    """
    while True:
        guess = input("Guess a letter: ").upper()
        
        # Check if input is a single letter
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        
        # Check if it's actually a letter
        if not guess.isalpha():
            print("Please enter a letter (A-Z).")
            continue
        
        # Check if already guessed
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue
        
        return guess


def play_game():
    """
    Main game loop for one complete word guessing game.
    """
    # Game setup
    word_list = get_word_list()
    secret_word = pick_random_word(word_list)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6
    
    print("\n" + "=" * 50)
    print("WORD GUESSING GAME")
    print("=" * 50)
    print(f"Try to guess the word! You have {max_wrong_guesses} wrong guesses.\n")
    
    # Main game loop
    while wrong_guesses < max_wrong_guesses:
        # Display current state
        display_hangman(wrong_guesses)
        print(f"\nWord: {display_word(secret_word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None yet'}")
        print(f"Wrong guesses remaining: {max_wrong_guesses - wrong_guesses}")
        
        # Get player's guess
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print(f"✓ Good guess! '{guess}' is in the word!")
            
            # Check if word is complete
            if all(letter in guessed_letters for letter in secret_word):
                print(f"\n🎉 Congratulations! You guessed the word: {secret_word}")
                return True
        else:
            wrong_guesses += 1
            print(f"✗ Sorry, '{guess}' is not in the word.")
            
            if wrong_guesses < max_wrong_guesses:
                print(f"You have {max_wrong_guesses - wrong_guesses} guesses left.")
        
        print()
    
    # Player lost
    display_hangman(wrong_guesses)
    print(f"\n😢 Game Over! The word was: {secret_word}")
    return False


def main():
    """
    Main function to run the game with play-again option and score tracking.
    """
    wins = 0
    losses = 0
    
    print("\nWelcome to Word Guessing Game!")
    
    while True:
        # Display score if any games have been played
        if wins + losses > 0:
            print(f"\n📊 Score - Wins: {wins} | Losses: {losses}")
        
        # Play one game
        won = play_game()
        
        # Update score
        if won:
            wins += 1
        else:
            losses += 1
        
        # Ask if they want to play again
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print(f"\nFinal Score - Wins: {wins} | Losses: {losses}")
            print("Thanks for playing! Goodbye!")
            break


# Run the game if this file is executed directly
if __name__ == "__main__":
    main()


"""
ENHANCEMENTS YOU COULD ADD:
===========================

1. Word Categories:
   - Create different word lists (animals, countries, tech terms)
   - Let player choose a category
   - Tell them the category before starting

2. Hint System:
   - Allow one hint per game
   - Reveal a random letter that hasn't been guessed
   - Or provide a definition/clue about the word

3. Difficulty Levels:
   - Easy: Short words, more guesses
   - Medium: Medium words, standard guesses
   - Hard: Long words, fewer guesses

4. Two-Player Mode:
   - One player enters a word (hidden input)
   - Other player tries to guess it
   - No preset word list needed

5. Time Limit:
   - Add a timer for each guess or whole game
   - Display time taken after winning

6. High Score System:
   - Track fastest wins
   - Save to a file
   - Display top scores

7. Better Visual Design:
   - Use colors for correct/wrong guesses
   - Animate the hangman drawing
   - Add sound effects (optional)

8. Word Validation:
   - Let player try to guess the whole word
   - If wrong, counts as multiple wrong guesses
   - If right, instant win

9. Multiplayer:
   - Track multiple players' scores
   - Tournament mode
"""
