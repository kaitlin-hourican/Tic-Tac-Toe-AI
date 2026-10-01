SIZE = 3
PLAYERS = ('X', 'O')

def new_board():
    return [[None for _ in range(SIZE)] for _ in range(SIZE)]

    # TEST - checking winning condition
    # return [["X", None, None], ["X", None, None], ["X", None, None]]      # col winner
    # return [[None, None, None], ["O", "O", "O"], ["X", None, None]]       # row winner
    # return [[None, None, "X"], [None, "X", None], ["X", None, None]]      # diagonal winner

    # TEST - checking if board empty
    # return [["O", "X", "O"], ["O", "X", "O"], ["X", None, "X"]]         # false - continue game
    # return [["O", "X", "O"], ["O", "X", "O"], ["X", "O", "X"]]          # true - game over


def print_board(board):
    board_image = ""

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is None:
                board_image += "   "
            else:
                board_image += f" {cell} "

            if j == (SIZE - 1):
               continue
            board_image += "|"

        if i == (SIZE - 1):
            continue
        board_image += "\n-----------\n"

    print(board_image)


def make_move(player, board):
    coords = None

    while True:
        print(f"{player}'s move:")
        coords = get_coords()

        if is_cell_empty(board, coords):
            board[coords[1]][coords[0]] = player
            return

        print("Cell must be empty")


def get_coords():
    valid_coords = [i for i in range(SIZE)]
    
    while True:
        try:
            x = int(input("x coordinate: "))
            y = int(input("y coordinate: "))

            if x in valid_coords and y in valid_coords:
                return (x, y)

            print("Enter valid coordinates")
        except ValueError:
            print("Coordinates must be integers")


def is_cell_empty(board, coords):
    return board[coords[1]][coords[0]] is None


def game_over(board):
    winner = [check_diagonals(board), check_rows(board), check_columns(board)]

    for result in winner:
        if result in PLAYERS:
            return result

    if board_full(board):
        return True

    return False
    
 
def check_columns(board):
    for col in range(SIZE):
        full_column = set()

        for row in range(SIZE):
            full_column.add(board[row][col])

        if len(full_column) == 1:
            return full_column.pop()

    return 


def check_rows(board):
    for row in range(SIZE):
        full_row = set(board[row])
        
        if len(full_row) == 1:
            el = full_row.pop()

            if el in PLAYERS:
                return el

    return


def check_diagonals(board):
    asc_diagonal = [board[i][i] for i in range(SIZE)]
    desc_diagonal = [board[i][SIZE - 1 - i] for i in range(SIZE)]

    if asc_diagonal[0] is not None and len(set(asc_diagonal)) == 1:
        return asc_diagonal.pop()

    if desc_diagonal[0] is not None and len(set(desc_diagonal)) == 1:
        return desc_diagonal.pop()

    return


def board_full(board):
    for i in range(SIZE):
        if None in board[i]:
            return False

    return True

def start_game():
    board = new_board()

    x_move = True

    while True:
        print_board(board)

        if x_move:
            make_move("X", board)
        else:
            make_move("O", board)

        is_over = game_over(board)

        if is_over == True:
            print("Game Over - No Winner")
            break
        elif is_over == False:
            x_move = not x_move
            continue
        else:
            print(f"Game Over - Winner is {is_over}")
            break



start_game()