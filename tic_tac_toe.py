SIZE = 3

def new_board():
    return [[None for _ in range(SIZE)] for _ in range(SIZE)]


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
        coords = get_coords()

        if is_empty(board, coords):
            board[coords[0]][coords[1]] = player
            print(board[coords[0]])
            print_board(board)
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

def is_empty(board, coords):
    return board[coords[0]][coords[1]] is None


def game_over(board):
    return

def start_game():
    board = new_board()

    print_board(board)
    make_move("x", board)

    print(game_over(board))


start_game()