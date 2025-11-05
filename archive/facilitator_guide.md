# Claude Code Workshop: Facilitator Guide

## Workshop Overview
**Duration:** 80 minutes  
**Tool:** Claude Code  
**Skill Levels:** Mixed (beginners + advanced students)  
**Pairing Strategy:** Advanced student mentors beginner

---

## Three Project Options

### Option 1: Tic-Tac-Toe ⭐ RECOMMENDED FOR BEGINNERS
**Best for:** True beginners, first-time programmers  
**Complexity:** Low  
**Estimated completion:** 60-70 minutes for basic version

**Why this works:**
- Clear rules everyone knows
- Visual board display is satisfying
- Natural progression: display → player moves → win detection
- Can be enhanced infinitely (AI opponent, larger boards, etc.)

---

### Option 2: Word Guessing Game (Hangman)
**Best for:** Beginners with some Python exposure  
**Complexity:** Medium  
**Estimated completion:** 60-70 minutes for basic version

**Why this works:**
- Combines string manipulation with game logic
- Visual feedback (showing guessed letters)
- Creative freedom in word lists
- Good introduction to lists and string operations

---

### Option 3: Turn-Based RPG Battle
**Best for:** Students comfortable with variables and functions  
**Complexity:** Medium-High  
**Estimated completion:** May need full 80 minutes

**Why this works:**
- Teaches state management (health, attacks)
- Multiple functions working together
- Can be simple or complex based on skill level
- Very engaging for students interested in game dev

---

## Workshop Timeline (All Projects)

### Phase 1: Planning & Design (15 minutes)
**Advanced student's role:**
- Ask beginner: "What game features do you think we need?"
- Sketch out game flow on paper
- List what data we need to track
- Write down 3-4 core features for MVP

**Facilitator circulates:** Ensure pairs aren't over-planning. Keep it simple.

---

### Phase 2: Build MVP (35 minutes)
**Key principle:** Start with smallest working version

**Advanced student's role:**
- Help beginner craft prompts for Claude Code
- Review code Claude generates together
- Ask: "Do you understand what this line does?"
- Test frequently

**Critical instruction for all students:**
> "Ask Claude Code to build ONE feature at a time. Test it before moving to the next."

**Facilitator circulates:** 
- Watch for pairs that jump too fast
- Encourage testing after each addition
- Help debug when needed

---

### Phase 3: Enhance (20 minutes)
Students add features based on their progress:
- **If ahead:** Add enhancements from handout
- **If on track:** Polish and test thoroughly
- **If behind:** Focus on making current version work well

---

### Phase 4: Demo & Reflect (10 minutes)
- Pairs swap computers and play each other's games
- Quick discussion: "What was easiest? What was hardest?"
- "What would you add next time?"

---

## Using Claude Code Effectively

### Good Prompting Strategy (teach students this)

**❌ Bad prompt:**
"Make me a tic-tac-toe game"

**✅ Good prompt:**
"Help me create a tic-tac-toe game in Python. Start with just displaying a 3x3 board using print statements. Keep it simple."

**Then, after that works:**
"Now add the ability for player X to make one move and update the board display."

### Key Phrases for Students
- "Keep it simple"
- "Start with just..."
- "Let's test this before adding more"
- "Can you explain what this function does?"
- "Show me one way to do this"

---

## Troubleshooting Common Issues

### "Claude wrote too much code and we're lost"
→ Have them ask: "Can you explain what each part of this code does?"
→ Suggest starting over with a simpler prompt

### "We finished too early"
→ Point to enhancement ideas on their handout
→ Have them add error handling
→ Suggest code review: "Can you make this code clearer?"

### "We're stuck and nothing works"
→ Ask them to describe what should happen vs. what is happening
→ Help them craft a debugging prompt for Claude Code
→ Suggest testing smaller pieces

### "Advanced student is doing everything"
→ Remind advanced student: "Your job is to help THEM understand, not to code it yourself"
→ Encourage beginner to type all prompts to Claude Code

---

## Assessment Questions (Optional)

Use these to check understanding during circulation:

**For beginners:**
- "Can you show me where the user's input is stored?"
- "What happens in this if statement?"
- "Can you trace through what happens when someone makes a move?"

**For advanced students:**
- "How would you explain this function to someone new to Python?"
- "What edge cases might break this code?"
- "If you were starting over, what would you do differently?"

---

## Materials Needed

✅ Computers with Claude Code installed  
✅ Python installed  
✅ Student handouts (choose one per pair)  
✅ Paper/whiteboard for planning phase  
✅ Sample solutions (for your reference)

---

## Tips for Success

1. **Emphasize the planning phase** - 15 minutes planning saves 30 minutes of confusion
2. **Test frequently** - After every feature addition
3. **Start simpler than you think** - Students can always add more
4. **Let them struggle a bit** - Don't rush to help immediately
5. **Celebrate working code** - Even simple versions are achievements

---

## Extension Ideas (If Time Remains)

- Add a score tracking system
- Save game history to a file
- Add color/formatting to terminal output
- Create a "replay" feature
- Add difficulty levels
- Let students design their own enhancement

---

## Learning Outcomes

By the end of this workshop, students should be able to:
- Break a project into smaller, manageable steps
- Craft effective prompts for AI coding assistants
- Read and understand Python code they didn't write
- Test and debug incrementally
- Collaborate on a coding project
- Use functions and basic data structures

---

## Quick Reference: Which Project for Which Pair?

**Choose Tic-Tac-Toe if:**
- Beginner has minimal Python experience
- Pair wants clearest structure
- You want highest success rate

**Choose Word Guessing if:**
- Beginner knows lists and strings
- Pair likes puzzles
- You want creative freedom (word lists)

**Choose RPG Battle if:**
- Beginner is comfortable with functions
- Pair is interested in game mechanics
- You want to explore state management

---

## Post-Workshop

Consider having students:
- Push code to GitHub (learning opportunity)
- Write a brief README explaining their game
- Demo to whole class
- Reflect on what they'd improve

Good luck! This is going to be a great learning experience.
