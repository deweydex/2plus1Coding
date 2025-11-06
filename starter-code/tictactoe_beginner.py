"""
TIC-TAC-TOE GAME - Beginner Starter Code
=========================================

This starter code provides the foundation for building a tic-tac-toe game.
A working board display is already implemented so you can see visual output
immediately when you run this file.

YOUR TASKS:
1. Add a function to let a player make a move
2. Create a game loop so players can alternate turns
3. Add win detection (check rows, columns, and diagonals)
4. Handle tie games (when the board is full)
5. Add enhancements based on your interests

RUN THIS FILE FIRST to see what you're starting with:
    python tictactoe_beginner.py

Then work with Claude Code to build the game step by step.
"""


def create_board():
    """
    Creates and returns a new game board.

    The board is represented as a list of 9 elements (positions 0-8).
    Each position starts with its number (1-9) to show players where they can move.
    When a player makes a move, we'll replace the number with 'X' or 'O'.

    Returns:
        list: A list of 9 strings representing the empty board
    """
    return ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def display_board(board):
    """
    Displays the current state of the game board.

    The board is shown as a 3x3 grid with lines separating the positions.
    This makes it easy for players to see the current game state.

    Parameters:
        board (list): The game board to display
    """
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def main():
    """
    Main function to run the game.

    Right now, this just creates a board and displays it.
    You'll expand this to include the full game logic.
    """
    print("=" * 40)
    print("  WELCOME TO TIC-TAC-TOE!")
    print("=" * 40)
    print("\nShowing an empty board:")

    # Create a new board
    board = create_board()

    # Display it
    display_board(board)

    print("This is your starting point!")
    print("Next step: Add a function to let players make moves.")
    print("\nWork with Claude Code to build the game step by step.")


# This runs the main function when you execute this file
if __name__ == "__main__":
    main()


"""
SUGGESTED PROMPTS FOR CLAUDE CODE:
===================================

After running this starter code, try these prompts one at a time:

1. "Add a function called make_move that takes a board, a position (1-9),
   and a player symbol (X or O), and places the symbol at that position.
   Then update main() to test it."

2. "Create a function called get_player_move that asks the current player
   for their move and returns a valid position. For now, don't worry about
   validating if the position is already taken."

3. "Add a simple game loop that lets X make one move, then O make one move,
   alternating for 9 total moves."

4. "Create a function called check_winner that returns the winning player
   (X or O) if there's a winner, or None if not. Check all rows, columns,
   and diagonals."

5. "Integrate the win checking into the game loop so the game stops when
   someone wins."

Remember: Test after each change! Make sure each piece works before moving on.
"""
