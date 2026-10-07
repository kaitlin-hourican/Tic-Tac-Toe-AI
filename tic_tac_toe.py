import random

SIZE = 3
PLAYERS = ('X', 'O')

def new_board():
    """
    Creates and returns a new empty game board grid

    Returns:
        list[list[None]]: a 2D matrix representing an empty grid
    """
    return [[None for _ in range(SIZE)] for _ in range(SIZE)]


def print_board(board):
    """
    Renders current game board with uniform box borders and coordinates

    Args:
        board (list[list[str[None]]]): current 2D game state matrix
    """
    headers = "    " + "   ".join(f"{col}" for col in range(SIZE))
    divider = "  " + "+" + "---+" * SIZE
    
    print(headers)
    print(divider)
    for r, row in enumerate(board):
        row_str = f"{r} | " + " | ".join(cell if cell else " " for cell in row) + " |"
        print(row_str)
        print(divider)


def make_move(player, board):
    """
    Prompts active player for coordinates and places their token on the board

    Args:
        player (str): token string of current player ('X' or 'O')
        board (list[list[str[None]]]): current 2D game state matrix
    """
    while True:
        print(f"\n{player}'s turn:")
        row, col = random_ai(board, player)

        if board[row][col] is None:
            board[row][col] = player
            return

        print("Cell is already occupied! Try again.")


def get_coords():
    """
    repeatedly prompts user for grid coordinates until valid input provided

    Returns:
        tuple[int, int]: verified (row, column) coordinate index pair
    """
    while True:
        try:
            row = int(input(f"Enter row (0-{SIZE-1}): "))
            col = int(input(f"Enter column (0-{SIZE-1}): "))

            if 0 <= row < SIZE and 0 <= col < SIZE:
                return row, col

            print("Out of bounds! Stay within the grid parameters.")
        except ValueError:
            print("Invalid character! Coordinates must be integers.")


def random_ai(board, player):
    free_cells = []

    for col in range(SIZE):
        for row in range(SIZE):
            if board[col][row] is None:
                free_cells.append((col, row))

    return random.choice(free_cells)


def game_over(board):
    """
    evaluates board state to check for row, col, diagonal wins, or a tie

    Args:
        board (list[list[str[None]]]): current 2D game state matrix
    """
    # check rows
    for row in board:
        if row[0] is not None and all(cell == row[0] for cell in row):
            return row[0]

    # check cols
    for col in zip(*board):
        if col[0] is not None and all(cell == col[0] for cell in col):
            return col[0]

    # check diagonals
    diag1 = [board[i][i] for i in range(SIZE)]
    diag2 = [board[i][SIZE - 1 - i] for i in range(SIZE)]
    
    if diag1[0] is not None and all(cell == diag1[0] for cell in diag1):
        return diag1[0]
    if diag2[0] is not None and all(cell == diag2[0] for cell in diag2):
        return diag2[0]

    # check tie
    if all(cell is not None for row in board for cell in row):
        return "Tie"

    return None


def start_game():
    """manages main execution thread, setup sequence, and turn rotations"""
    board = new_board()
    player_index = 0

    while True:
        print_board(board)
        current_player = PLAYERS[player_index]
        
        make_move(current_player, board)
        result = game_over(board)

        if result:
            print_board(board)  
            if result == "Tie":
                print("\nGame Over - It's a draw!")
            else:
                print(f"\nGame Over - Winner is {result}!")
            break

        player_index = (player_index + 1) % len(PLAYERS)


if __name__ == "__main__":
    start_game()
