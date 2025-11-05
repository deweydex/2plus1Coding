# Claude Code Quick Reference Guide

## What is Claude Code?

Claude Code is a command-line tool that lets you work with Claude to write, edit, and understand code directly in your terminal. Think of it as having an expert programming assistant right alongside you.

---

## Getting Started

### Basic Command
```bash
claude-code
```

This starts an interactive session where you can have a conversation with Claude about code.

### Working with Files
Claude Code can:
- Read your existing files
- Create new files
- Edit files
- Run your code
- Explain what code does

---

## How to Ask Good Questions

### ❌ Poor Prompts (Too Vague or Too Broad)

**Bad:** "Make a game"
- Problem: Too vague, Claude might create something too complex

**Bad:** "Write all the code for tic-tac-toe"
- Problem: You won't understand it, and it's too much at once

**Bad:** "Fix my code"
- Problem: Doesn't explain what's wrong

---

### ✅ Good Prompts (Clear and Incremental)

**Good:** "Help me create a function that displays a 3x3 tic-tac-toe board using print statements. Keep it simple."
- Why: Specific, focused on one feature, asks for simplicity

**Good:** "I'm getting an error on line 15 that says 'list index out of range'. Can you help me understand what that means?"
- Why: Includes specific error information

**Good:** "Can you explain what this function does line by line?"
- Why: Asks for understanding, not just code

---

## The Iterative Approach

### Step-by-Step Building

Think of building your project like building with blocks:

**Step 1:** Foundation
```
"Create a function to display an empty game board"
```
→ Test it! Make sure it works.

**Step 2:** Add one feature
```
"Now add the ability to place an X at a position the user chooses"
```
→ Test it! Make sure it works.

**Step 3:** Add next feature
```
"Now let players alternate between X and O"
```
→ Test it! Make sure it works.

Continue this pattern. Each step should:
1. Build on what works
2. Add ONE new thing
3. Be testable

---

## Example Conversation Flow

Here's what a good back-and-forth looks like:

**You:** "Help me create a word guessing game. Start with just picking a random word from a list and displaying it as underscores."

**Claude Code:** *[Creates basic code]*

**You:** "Great! Can you explain how the underscore creation works? I see there's a loop but I'm not sure what it's doing."

**Claude Code:** *[Explains the logic]*

**You:** "That makes sense. Now let's add the ability to guess one letter and check if it's in the word."

**Claude Code:** *[Adds guessing logic]*

**You:** "This works but what happens if someone guesses the same letter twice? Should we check for that?"

**Claude Code:** *[Adds duplicate checking]*

Notice the pattern:
1. Ask for one thing
2. Test it
3. Ask questions about it
4. Understand it
5. Add next thing

---

## Key Phrases That Help

### Starting Out
- "Keep it simple"
- "Start with just..."
- "Let's begin with the most basic version"
- "Create a minimal example"

### Understanding
- "Can you explain what this does?"
- "What is this line doing?"
- "Why did you use [concept] here?"
- "Walk me through this function"

### Testing
- "How can I test if this works?"
- "What should happen when I run this?"
- "Can you add some test cases?"

### Debugging
- "I'm getting this error: [paste error]"
- "This isn't working how I expected. When I do X, Y happens, but I expected Z"
- "Can you help me trace through what happens when...?"

### Improving
- "How could we make this more efficient?"
- "Is there a cleaner way to write this?"
- "What edge cases should we handle?"

---

## Common Pitfalls to Avoid

### 1. Asking for Everything at Once
❌ "Create a complete tic-tac-toe game with AI, score tracking, and graphics"
✅ "Create a function to display a basic tic-tac-toe board"

### 2. Not Testing Between Steps
❌ Adding 5 features before testing anything
✅ Test after each feature addition

### 3. Not Asking Questions
❌ Copying code without understanding
✅ "What does this function parameter do?"

### 4. Giving Up When Stuck
❌ "This is too hard, I'll just copy the solution"
✅ "I'm stuck on this part. Can you explain the error message I'm getting?"

---

## Understanding Code Claude Generates

When Claude Code creates code, don't just run it. Follow these steps:

### 1. Read It First
Look at the code before running it. Try to understand what it's doing.

### 2. Ask About Anything Unclear
```
"I see you used a dictionary here. Why not a list?"
"What does this 'return' statement do?"
"Why do we need this if statement?"
```

### 3. Predict What Will Happen
Before running it, try to predict:
- What will print?
- What will the user see?
- What happens if the user types something unexpected?

### 4. Test It
Run the code and see if your predictions were correct.

### 5. Experiment
Try changing something small and see what happens:
- Change a number
- Change a message
- Add a print statement to see what a variable contains

---

## Working in Pairs

### If You're the Beginner
- **Type all the prompts yourself** - you'll learn more by doing
- **Ask questions constantly** - "What does this mean?"
- **Explain back** - try to explain what the code does in your own words
- **Don't just watch** - actively participate in decisions

### If You're the Advanced Student
- **Let them struggle a bit** - don't rush to give answers
- **Ask guiding questions** - "What do you think this does?"
- **Explain, don't do** - help them understand, don't code for them
- **Check understanding** - "Can you explain this back to me?"

### Together
- **Discuss before prompting** - agree on what to build next
- **Read code together** - go through new code line by line
- **Test together** - both think about what should happen
- **Debug together** - both try to understand errors

---

## Debugging with Claude Code

### When Something Goes Wrong

**1. Read the Error Message**
Error messages tell you what's wrong. They include:
- What type of error
- Which line it occurred on
- Usually a hint about the problem

**2. Share the Error with Claude**
```
"I'm getting this error: [paste the full error message]
This happens when I try to [describe what you were doing]"
```

**3. Explain What You Expected**
```
"When I input 5, I expected the board to update at position 5,
but instead I get an index error."
```

**4. Ask for Explanation**
```
"Can you explain what's causing this error and how to fix it?"
```

---

## Testing Your Code

### Test After Every Change

Don't wait until everything is "done" to test. Test constantly:

**After adding display function:**
- Does the board show correctly?
- Are all positions visible?

**After adding player input:**
- Can the player enter a position?
- Does it update the board?
- What if they enter an invalid number?

**After adding win detection:**
- Does it detect when someone wins?
- Does it detect all winning combinations?
- Does it keep playing when there's no winner yet?

### Think About Edge Cases

What unusual things might a user do?
- Enter a letter instead of a number
- Enter a number outside the valid range
- Try to play in an occupied spot
- Press Enter without typing anything

Test these cases!

---

## Getting Unstuck

### "I don't understand this code"
1. Ask Claude to explain it line by line
2. Ask what each variable represents
3. Ask Claude to add comments explaining it
4. Try changing one thing and see what happens

### "My code has a bug"
1. Identify exactly when it breaks (which input causes the problem?)
2. Add print statements to see what's happening
3. Ask Claude: "When I do X, I get Y, but I expected Z. Why?"

### "I don't know what to build next"
1. Look at your handout for suggested next steps
2. Test what you have - find something that could be better
3. Ask your partner what feature would be cool
4. Ask Claude: "What's a good next feature to add?"

### "This is too hard"
1. Take a step back - make it simpler
2. Focus on making one small thing work
3. Ask your facilitator for help
4. Remember: everyone finds programming challenging at first!

---

## Pro Tips

### 1. Use Comments
Ask Claude to add comments to explain complex parts:
```
"Can you add comments to this function explaining what each part does?"
```

### 2. Break Down Problems
If something seems too hard, break it into smaller pieces:
- Instead of "make the game work"
- Try "make the board display, then add input, then add win checking"

### 3. Compare Solutions
After you have something working, ask:
```
"Are there other ways to solve this problem?"
"What are the pros and cons of different approaches?"
```

### 4. Learn Patterns
Notice patterns in how code is structured:
- Functions have a purpose
- Loops repeat actions
- If statements make decisions
- Variables store information

### 5. Celebrate Small Wins
Got the board to display? Awesome!
Got player input working? Great!
Each small victory is progress.

---

## Remember

- **There's no "right" way** - many solutions work
- **Mistakes are learning** - bugs teach you more than perfect code
- **Understanding > Speed** - it's better to go slow and understand
- **Ask questions** - there are no stupid questions
- **Help each other** - teaching someone helps you learn too
- **Have fun!** - programming is creative and rewarding

---

## Quick Command Reference

### Starting Claude Code
```bash
claude-code
```

### In the Claude Code Session
- **Type your request** and press Enter
- **Ask questions** about code
- **Request edits** to files
- **Type "exit"** to quit

### Common Requests
```
"Create a new file called game.py"
"Show me what's in game.py"
"Add a function to check for winners"
"Run my code"
"Explain what this function does"
```

---

Good luck with your project! Remember: the goal is to learn, not to create perfect code. Take your time, ask questions, and enjoy the process of building something!
