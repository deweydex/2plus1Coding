# Student Handout: Word Guessing Game

## Project Overview
Build a word guessing game (like Hangman) that runs in the terminal!

**What you'll create:**
- A game that picks a random word from a list
- Display the word with hidden letters (underscores)
- Players guess one letter at a time
- Track correct and incorrect guesses
- Win by completing the word, lose after too many wrong guesses

**Time:** 80 minutes  
**Difficulty:** ⭐⭐ Beginner to Intermediate  
**Language:** Python

---

## What You'll Learn
- Working with strings and lists
- Random selection
- String manipulation and formatting
- Tracking game state
- User input validation
- Loop control

---

## Phase 1: Planning (15 minutes)

### Questions to Answer Together

Before writing any code, discuss:

1. **What information do we need to track?**
   - The secret word
   - Letters guessed so far
   - Correct guesses
   - Wrong guesses
   - Number of attempts remaining

2. **How do we display the word?**
   - Hidden at start: `_ _ _ _ _` (for "HELLO")
   - After guessing 'E': `_ E _ _ _`
   - After guessing 'L': `_ E L L _`

3. **What's our MVP (Minimum Viable Product)?**
   - Pick a random word from a list ✓
   - Display word with underscores ✓
   - Take letter guesses ✓
   - Reveal correct letters ✓
   - End when word is complete or tries run out ✓

4. **What features can we add later?**
   - Hangman visual (drawing that gets more complete)
   - Different difficulty levels (word length)
   - Categories (animals, countries, etc.)
   - Score tracking across multiple games
   - Hint system

### Draw Your Game Flow

On paper, sketch out:
```
Pick random word from list
  ↓
Show word as underscores
  ↓
Player guesses a letter
  ↓
Is letter in word?
  ↓ Yes             ↓ No
Reveal letter   Subtract attempt
  ↓                  ↓
Check if won    Check if lost
  ↓                  ↓
Continue or end
```

---

## Phase 2: Building with Claude Code (35 minutes)

### 🎯 Step 1: Pick and Display Word (8 minutes)

**Your prompt to Claude Code:**
```
Help me create a word guessing game in Python. First, create a list 
of 5-10 words, then randomly pick one. Display the word as underscores, 
with one underscore for each letter. For example, if the word is "PYTHON" 
display "_ _ _ _ _ _"
```

**Test it!** Run your code multiple times. Does it pick different words?

**Understanding check:**
- Where is the word list stored?
- How does random selection work?
- How are the underscores created?

---

### 🎯 Step 2: Take One Guess (8 minutes)

**Your prompt to Claude Code:**
```
Now let's add the ability for the player to guess one letter. Ask them 
to input a letter, then check if that letter is in the secret word. 
Print whether they were right or wrong. Don't update the display yet, 
just check the letter.
```

**Test it!** Run your code and make a guess. Does it correctly tell you if the letter is in the word?

**Understanding check:**
- How does the code check if a letter is in the word?
- What data type is the word stored as?
- How is the player's input captured?

---

### 🎯 Step 3: Update Display (10 minutes)

**Your prompt to Claude Code:**
```
When the player guesses correctly, update the display to show that 
letter in the correct position(s). For example, if the word is "HELLO" 
and they guess "L", show "_ _ L L _". Keep the underscores for letters 
they haven't guessed yet.
```

**Test it!** Make several correct guesses. Do the letters appear in the right spots?

**Understanding check:**
- How does the code know which positions to reveal?
- What happens if a letter appears multiple times?
- How is the display updated?

---

### 🎯 Step 4: Add Game Loop (12 minutes)

**Your prompt to Claude Code:**
```
Create a game loop that:
- Lets the player keep guessing until they win or lose
- Tracks wrong guesses (give them 6 tries)
- Shows how many attempts remain
- Displays all letters they've guessed so far
- Ends when they complete the word OR run out of tries
- Shows appropriate win/lose message
```

**Test it!** Play complete games:
- Win by guessing all letters
- Lose by running out of guesses
- Try guessing the same letter twice

**Understanding check:**
- What makes the loop continue?
- What makes it stop?
- How are wrong guesses counted?
- Where are previous guesses stored?

---

## Phase 3: Enhancements (20 minutes)

Choose features to add based on your progress:

### 🌟 Enhancement 1: Input Validation
**Prompt:**
```
Add validation so the game:
- Only accepts single letters (not numbers or multiple letters)
- Converts input to uppercase for consistency
- Tells players if they already guessed that letter
- Doesn't count repeated guesses as wrong attempts
```

### 🌟 Enhancement 2: ASCII Hangman Drawing
**Prompt:**
```
Add a visual hangman that gets drawn progressively with each wrong 
guess. Use ASCII art with 6 stages. Show the current stage after 
each wrong guess.
```

Example stages:
```
  +---+       +---+       +---+  
      |       O   |       O   |  
      |           |      /|\  |  
      |           |      / \  |  
     ===         ===         ===
  (0 wrong)   (3 wrong)  (6 wrong)
```

### 🌟 Enhancement 3: Multiple Rounds
**Prompt:**
```
After each game ends, ask if the player wants to play again. 
Track their wins and losses across multiple rounds. Display 
their record before starting each new round.
```

### 🌟 Enhancement 4: Word Categories
**Prompt:**
```
Create different categories of words (animals, countries, foods, etc.). 
Let the player choose a category at the start. Tell them the category 
before they start guessing.
```

### 🌟 Enhancement 5: Hint System
**Prompt:**
```
Add a hint system where the player can use one hint per game. When 
used, reveal one random letter that hasn't been guessed yet. Make 
it optional - they can choose to use it or not.
```

### 🌟 Enhancement 6: Difficulty Levels
**Prompt:**
```
Add three difficulty levels:
- Easy: 4-5 letter words, 8 attempts
- Medium: 6-8 letter words, 6 attempts  
- Hard: 9+ letter words, 5 attempts
Let the player choose at the start.
```

---

## Tips for Success

### For the Beginner:
- **Think about strings vs. lists** - when do we need each?
- **Print often** - use print statements to see what's happening
- **Don't worry about perfect code** - make it work first
- **Ask "why"** - why did Claude use this approach?

### For the Advanced Student:
- **Explain string methods** - help them understand .upper(), .isalpha(), etc.
- **Discuss data structures** - why use a list for guessed letters?
- **Walk through logic** - trace through what happens on each guess
- **Suggest improvements** - "How could we make this cleaner?"

### For Both:
✅ Test edge cases - what if they guess a number?  
✅ Read error messages carefully  
✅ Understand the flow - follow the logic from start to end  
✅ Keep it fun - add personality with messages  
✅ Iterate - start simple, add complexity  

---

## Debugging Tips

**Problem:** "Same word every time"
- Check: Are you importing random?
- Check: Is random.choice() being called correctly?

**Problem:** "Underscores don't update"
- Check: Are you storing the updated display?
- Check: Are you printing the updated version?

**Problem:** "Case sensitivity issues"
- Solution: Convert all input to uppercase or lowercase
- Check: Is your comparison consistent?

**Problem:** "Game doesn't end"
- Check: Are your win/lose conditions correct?
- Check: Is your loop condition right?

**Problem:** "Can guess same letter multiple times"
- Check: Are you tracking guessed letters?
- Check: Are you checking if letter was already guessed?

---

## Sample Session with Claude Code

Here's what a good back-and-forth looks like:

**You:** "Help me make a word guessing game. Start by creating a list of words and picking one randomly."

**Claude Code:** [Creates word list and random selection]

**You:** "Great! Now show me how to display that word as underscores."

**Claude Code:** [Adds underscore display logic]

**You:** "It works! Can you explain how the underscore creation works? I see you're using a loop."

**Claude Code:** [Explains the logic]

**You:** "Now let's add guessing. Just one guess for now."

**Claude Code:** [Adds single guess logic]

**You:** "Perfect! What happens if the letter appears twice in the word?"

**Claude Code:** [Explains and potentially improves the code]

---

## Challenge Questions

Once your basic game works, try to answer these:

1. How would you add a timer (player must guess within 60 seconds)?
2. Could you create a two-player mode where one player picks the word?
3. How would you save high scores to a file?
4. What if you wanted to allow phrase guessing (with spaces)?
5. How could you add difficulty that adjusts based on player performance?

---

## Code Structure Tips

Your final code might have functions like:
- `pick_random_word()` - selects word from list
- `display_word(word, guessed_letters)` - shows current progress
- `get_guess()` - gets and validates player input
- `check_guess(guess, word)` - checks if guess is correct
- `draw_hangman(wrong_count)` - displays hangman figure
- `play_game()` - main game loop
- `main()` - handles multiple rounds

Don't worry if yours looks different! There are many good ways to structure this.

---

## Reflection (End of Session)

Think about:
- What string operations did you learn?
- How did you track game state?
- What was the trickiest part?
- How did working with Claude Code help?
- What would make this game more fun?

---

## Word List Ideas

**Easy (4-5 letters):**
- CAKE, BOOK, TREE, MOON, STAR

**Medium (6-8 letters):**
- PYTHON, COMPUTER, MOUNTAIN, ELEPHANT

**Hard (9+ letters):**
- PROGRAMMING, CHOCOLATE, BASKETBALL

**Categories:**
- Animals: DOG, ELEPHANT, PENGUIN
- Countries: FRANCE, BRAZIL, JAPAN
- Foods: PIZZA, SUSHI, TACOS

---

Good luck! Remember: the goal is understanding, not just working code. Take time to read and understand what Claude Code generates.
