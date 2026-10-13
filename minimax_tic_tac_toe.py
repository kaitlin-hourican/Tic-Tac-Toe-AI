SIZE = 3

def new_board():
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

def is_winner(board):
    # column
    for col in zip(*board):
        if col[0] is not None and all(cell == col[0] for cell in col):
            return True

    # row
    for row in board:
        if row[0] is not None and all(cell == row[0] for cell in row):
            return True

    # diagonal 
    diag1 = [board[i][i] for i in range(SIZE)]
    diag2 = [board[i][SIZE - 1 - i] for i in range(SIZE)]
        
    if diag1[0] is not None and all(cell == diag1[0] for cell in diag1):
        return True
    if diag2[0] is not None and all(cell == diag2[0] for cell in diag2):
        return True
    
    # tie
    if all(cell is not None for row in board for cell in row):
        return None

    # not terminal state 
    return False


def minimax_ai(board, depth, is_maximiser = True):
    # base case - terminal state
    result = is_winner(board)

    if result:
        return 10 - depth if is_maximiser else -10 - depth
    elif result is None:
        return 0

    # is_maximiser true - ie X
    if is_maximiser:
        best_score = float("-inf")

        for row in range(SIZE):
            for col in range(SIZE):
               if board[row][col] is None:
                   board[row][col] = "X"
                   score = minimax_ai(board, depth + 1, False)
                   board[row][col] = None

                   best_score = max(score, best_score)

        return best_score

    else:
        best_score = float("inf")

        for row in range(SIZE):
            for col in range(SIZE):
                if board[row][col] is None:
                    board[row][col] = "O"
                    score = minimax_ai(board, depth + 1, True)
                    board[row][col] = None

                    best_score = min(score, best_score)

        return best_score


def make_move(board):
    while True:
        try:
            row = int(input(f"Enter row (0--{SIZE - 1}): "))
            col = int(input(f"Enter column (0--{SIZE - 1}): "))
    
            if 0 <= row < SIZE and 0 <= col < SIZE and board[row][col] is None:
                board[row][col] = "O"
                return
    
            print("Must be empty cell within bounds!")
        except ValueError:
            print("Invalid coordinate value!")

def start_game():
    board = new_board()
    print_board(board)

    while not is_winner(board):
        make_move(board)
        print_board(board)
        minimax_ai(board, 0)
        print_board(board)

start_game()

