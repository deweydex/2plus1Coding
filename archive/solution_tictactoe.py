"""
TIC-TAC-TOE GAME - Sample Solution
==================================
This is a working implementation of a basic tic-tac-toe game.
This code demonstrates the MVP (Minimum Viable Product) version.

Features included:
- Display game board
- Two players alternate turns
- Input validation
- Win detection (rows, columns, diagonals)
- Tie detection
- Play again option
"""

def create_board():
    """
    Create and return a new game board.
    Board is a list of 9 elements representing positions 1-9.
    """
    return ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def display_board(board):
    """
    Display the current game board in a nice format.
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
    Place the player's mark (X or O) at the specified position.
    Position is 1-9, but we use 0-8 for list indexing.
    """
    board[position - 1] = player


def is_valid_move(board, position):
    """
    Check if a move is valid (position is available).
    A position is valid if it still contains its number (1-9).
    """
    return board[position - 1].isdigit()


def check_winner(board):
    """
    Check if there's a winner.
    Returns the winning player ('X' or 'O') or None if no winner yet.
    """
    # All possible winning combinations (indices)
    winning_combos = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal top-left to bottom-right
        [2, 4, 6]   # Diagonal top-right to bottom-left
    ]
    
    # Check each winning combination
    for combo in winning_combos:
        if (board[combo[0]] == board[combo[1]] == board[combo[2]]):
            # All three positions match - we have a winner!
            return board[combo[0]]
    
    return None


def is_board_full(board):
    """
    Check if the board is full (all positions are X or O).
    If full and no winner, it's a tie.
    """
    return all(not cell.isdigit() for cell in board)


def get_player_move(board, player):
    """
    Get a valid move from the player.
    Keeps asking until they provide a valid position.
    """
    while True:
        try:
            position = int(input(f"Player {player}, enter your move (1-9): "))
            
            # Check if position is in valid range
            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
                continue
            
            # Check if position is available
            if not is_valid_move(board, position):
                print("That position is already taken. Choose another.")
                continue
            
            return position
            
        except ValueError:
            print("Please enter a valid number.")


def play_game():
    """
    Main game loop for one complete game of tic-tac-toe.
    """
    board = create_board()
    current_player = 'X'
    
    print("=" * 40)
    print("Welcome to Tic-Tac-Toe!")
    print("=" * 40)
    print("Players will take turns marking positions 1-9")
    
    while True:
        display_board(board)
        
        # Get the player's move
        position = get_player_move(board, current_player)
        make_move(board, position, current_player)
        
        # Check for winner
        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"🎉 Player {winner} wins! Congratulations! 🎉")
            break
        
        # Check for tie
        if is_board_full(board):
            display_board(board)
            print("It's a tie! Well played both players!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


def main():
    """
    Main function to run the game with play-again option.
    """
    while True:
        play_game()
        
        # Ask if they want to play again
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye!")
            break


# Run the game if this file is executed directly
if __name__ == "__main__":
    main()


"""
ENHANCEMENTS YOU COULD ADD:
===========================

1. Score Tracking:
   - Keep track of wins for X and O across multiple games
   - Display score before each game

2. Computer Opponent:
   - Add single-player mode
   - Start with random moves, later add smart AI

3. Better Board Display:
   - Add colors using colored text
   - Make the board look more polished

4. Larger Boards:
   - Modify to support 4x4 or 5x5 boards
   - Adjust win condition accordingly

5. Custom Player Names:
   - Ask for player names instead of just X and O
   - Personalize messages

6. Move History:
   - Keep track of all moves made
   - Allow undo feature

7. Difficulty Levels:
   - Easy: Random AI moves
   - Medium: AI blocks player wins
   - Hard: AI plays optimally (minimax algorithm)
"""
