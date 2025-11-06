"""
TIC-TAC-TOE GAME - Advanced Starter Code
=========================================

This starter code provides a more complete foundation with board display
and basic player input already working. Your focus will be on game logic,
win detection, and enhancements.

RUN THIS FILE FIRST to see what you're starting with:
    python tictactoe_advanced.py

The program will let you make a few moves to see the basic mechanics.

YOUR TASKS:
1. Add comprehensive win detection for all 8 winning conditions
2. Add tie detection (board full with no winner)
3. Create a full game loop that continues until win or tie
4. Add input validation (handle invalid positions, occupied squares)
5. Add enhancements: play again, score tracking, better UI, etc.
"""


def create_board():
    """
    Creates and returns a new game board.

    Returns:
        list: A list of 9 strings representing positions 1-9
    """
    return ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def display_board(board):
    """
    Displays the current game board in a formatted grid.

    Parameters:
        board (list): The current game state
    """
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def make_move(board, position, player):
    """
    Places a player's mark on the board at the specified position.

    Parameters:
        board (list): The game board
        position (int): Position 1-9 where the player wants to move
        player (str): The player's symbol ('X' or 'O')

    Note: This function assumes the position is valid. You'll want to add
    validation to check if the position is already occupied.
    """
    # Convert position (1-9) to list index (0-8)
    board[position - 1] = player


def get_player_move(player):
    """
    Gets a move from the current player.

    Parameters:
        player (str): The current player's symbol

    Returns:
        int: The position (1-9) where the player wants to move

    Note: This currently has minimal error handling. You should enhance it
    to validate input and check for occupied positions.
    """
    while True:
        try:
            position = int(input(f"Player {player}, enter your move (1-9): "))
            if 1 <= position <= 9:
                return position
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    """
    Main function demonstrating the basic game mechanics.

    This is a simplified version that lets you make 4 moves to test the system.
    You'll expand this into a full game loop with win detection and proper flow.
    """
    print("=" * 40)
    print("  TIC-TAC-TOE - Advanced Starter")
    print("=" * 40)

    board = create_board()
    current_player = 'X'

    print("\nThis starter code lets you make a few moves to test the mechanics.")
    print("Your job is to add win detection, full game logic, and enhancements.\n")

    # Simple demonstration: 4 moves alternating between players
    for turn in range(4):
        display_board(board)

        # Get the player's move
        position = get_player_move(current_player)

        # Make the move
        make_move(board, position, current_player)

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

    # Show final board
    display_board(board)

    print("\n" + "=" * 40)
    print("Demo complete! Now build the full game:")
    print("  - Add win detection")
    print("  - Add tie detection")
    print("  - Create proper game loop")
    print("  - Add input validation")
    print("  - Add enhancements")
    print("=" * 40)


if __name__ == "__main__":
    main()


"""
SUGGESTED PROMPTS FOR CLAUDE CODE:
===================================

After running this starter code, work on these features:

1. "Create a function called check_winner that examines the board and returns
   'X' if X has won, 'O' if O has won, or None if there's no winner yet.
   It should check all 8 winning conditions: 3 rows, 3 columns, 2 diagonals."

2. "Add a function called is_board_full that returns True if all positions
   are filled (no numbers 1-9 remain), indicating a tie game."

3. "Create a function called is_valid_move that checks whether a given position
   is still available (hasn't been taken by X or O)."

4. "Modify get_player_move to use is_valid_move and keep asking until the
   player chooses an available position."

5. "Rewrite the main game loop to continue until there's a winner or a tie,
   checking after each move and announcing the result appropriately."

6. "Add a play_again feature that asks if players want another game after
   one finishes."

7. For enhancements, consider:
   - Score tracking across multiple games
   - Better board display with colors or unicode characters
   - Single-player mode against a computer opponent
   - Undo feature
   - Custom player names instead of X and O

Remember to test thoroughly after each addition!
"""
