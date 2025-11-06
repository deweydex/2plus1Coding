# Student Handout: Tic-Tac-Toe Game

## Project Overview
Build a two-player Tic-Tac-Toe game that runs in the terminal!

**What you'll create:**
- A 3x3 game board that displays in the terminal
- Player X and Player O take turns
- The game detects wins, losses, and ties
- Players can restart and play again

**Time:** 80 minutes  
**Difficulty:** ⭐ Beginner-friendly  
**Language:** Python

---

## What You'll Learn
- Breaking problems into small steps
- Using functions to organize code
- Lists and 2D data structures
- Loops and conditional logic
- User input and output
- Testing your code incrementally

---

## Phase 1: Planning (15 minutes)

### Questions to Answer Together

Before writing any code, discuss and sketch out:

1. **What does our game board look like?**
   - How will we display it? (hint: think about using print statements)
   - How will we represent empty spaces?

2. **How do we track the game state?**
   - How do we remember where X's and O's are placed?
   - What data structure should we use? (list? list of lists?)

3. **What's our MVP (Minimum Viable Product)?**
   - Display a board ✓
   - Let players take turns ✓
   - Detect a winner ✓
   - That's it! Keep it simple.

4. **What features can we add later?**
   - Input validation (reject invalid moves)
   - Play again option
   - Score tracking
   - Computer opponent

### Draw Your Game Flow

On paper, sketch out:
```
Start game
  ↓
Display board
  ↓
Player 1 makes move
  ↓
Display updated board
  ↓
Check for winner?
  ↓
Player 2 makes move
  ↓
... and so on
```

---

## Phase 2: Building with Claude Code (35 minutes)

### 🎯 Step 1: Display the Board (10 minutes)

**Your prompt to Claude Code:**
```
Help me create a tic-tac-toe game in Python. First, let's just create a 
function that displays a 3x3 board. Use a list to represent the board, 
where empty spaces are numbers 1-9. Show me how to print it nicely 
formatted.
```

**Test it!** Run your code. You should see a board.

**Understanding check:**
- Where is the board data stored?
- What does the print function do?
- Can you change what's displayed in a position?

---

### 🎯 Step 2: Add Player Input (10 minutes)

**Your prompt to Claude Code:**
```
Now let's add the ability for a player to make a move. Ask the player 
which position (1-9) they want to place their mark, then update the 
board and display it again. Just do this once for now.
```

**Test it!** Run your code. Make one move. Does the board update?

**Understanding check:**
- Where does the player's input go?
- How does the board get updated?
- What happens if someone enters an invalid position?

---

### 🎯 Step 3: Alternate Turns (10 minutes)

**Your prompt to Claude Code:**
```
Let's make players alternate turns. Player X goes first, then Player O, 
then X again. Use a loop so they keep taking turns. For now, let's just 
do 9 turns total (a full board).
```

**Test it!** Play through a full game. Do players alternate correctly?

**Understanding check:**
- How does the game know whose turn it is?
- What makes the players alternate?
- Where does the loop start and end?

---

### 🎯 Step 4: Detect Winner (15 minutes)

**Your prompt to Claude Code:**
```
Add a function to check if someone has won the game. Check all rows, 
columns, and diagonals. If someone wins, display a message and end 
the game. Also check for a tie (board full, no winner).
```

**Test it!** Play games where:
- X wins
- O wins  
- It's a tie

**Understanding check:**
- What are all the ways to win?
- How does the function check for a win?
- When does the game stop?

---

## Phase 3: Enhancements (20 minutes)

Choose features to add based on your progress:

### 🌟 Enhancement 1: Input Validation
**Prompt:**
```
Add error checking so players can't:
- Choose a spot that's already taken
- Enter numbers outside 1-9
- Enter non-numeric input
Give them a helpful error message and let them try again.
```

### 🌟 Enhancement 2: Play Again
**Prompt:**
```
After a game ends, ask if players want to play again. If yes, reset 
the board and start a new game. If no, exit gracefully.
```

### 🌟 Enhancement 3: Score Tracking
**Prompt:**
```
Keep track of how many games X has won, how many O has won, and 
how many ties. Display the score after each game.
```

### 🌟 Enhancement 4: Better Display
**Prompt:**
```
Make the board display look nicer with borders and lines separating 
the squares. Make it look more like a real tic-tac-toe board.
```

### 🌟 Enhancement 5: Computer Opponent
**Prompt:**
```
Add a single-player mode where the player competes against the 
computer. Start with the computer making random valid moves.
```

---

## Tips for Success

### For the Beginner:
- **Ask questions!** If you don't understand something, ask your partner or Claude
- **Type the prompts yourself** - you'll learn more by doing
- **Test after each change** - don't wait until the end
- **It's okay to struggle** - that's how you learn

### For the Advanced Student:
- **Let your partner lead** - you're the guide, not the coder
- **Ask questions, don't give answers** - "What do you think this does?"
- **Help them debug** - teach them to read error messages
- **Make it collaborative** - you both should understand the code

### For Both:
✅ Start simple - you can always add more  
✅ Test frequently - after every new feature  
✅ Read the code together - understand before moving on  
✅ Celebrate small wins - display board working? Awesome!  
✅ Don't copy code blindly - ask Claude to explain  

---

## Debugging Tips

**Problem:** "Nothing happens when I run the code"
- Check: Did you call your main function?
- Check: Are you running the right file?

**Problem:** "Invalid syntax error"
- Check: Do you have matching parentheses and quotes?
- Ask Claude: "I'm getting this error: [paste error]. What does it mean?"

**Problem:** "Board doesn't update"
- Check: Are you displaying the board after updating it?
- Check: Is the board variable being passed correctly?

**Problem:** "Game doesn't stop when someone wins"
- Check: Is your win detection being called?
- Check: Do you have a break statement or return?

---

## Sample Session with Claude Code

Here's what a good back-and-forth looks like:

**You:** "Help me create a tic-tac-toe game in Python. Start with just displaying a 3x3 board."

**Claude Code:** [Creates basic board display function]

**You:** "This works! Now can you explain what the 'board' variable represents?"

**Claude Code:** [Explains the list structure]

**You:** "Great. Now let's add player input. Keep it simple - just let one player make one move."

**Claude Code:** [Adds input function]

**You:** "It works but what happens if I enter 10? Can we add a check for that?"

**Claude Code:** [Adds validation]

Notice: Each step builds on the last, and you're understanding as you go!

---

## Challenge Questions

Once your basic game works, try to answer these:

1. How would you modify the code to use X and O instead of X and O?
2. How could you make the board 4x4 instead of 3x3?
3. What's the time complexity of your win-checking function?
4. How would you make the computer opponent smarter?
5. Could you save game history to a file?

---

## Reflection (End of Session)

Think about:
- What was easier than you expected?
- What was harder?
- What did you learn about working with Claude Code?
- What would you build next?

---

## Resources

- Python docs: https://docs.python.org/3/
- Testing your code: Try `python your_filename.py` in terminal
- Need help? Ask your facilitator or use Claude Code's explanations

---

Good luck and have fun! Remember: working code is better than perfect code. Get something running first, then make it better.
