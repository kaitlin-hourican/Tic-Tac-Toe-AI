SIZE = 3

def new_board():
    return [[None, None, None], [None, None, None], [None, None, None]]


def print_board(board):
    board_image = ""

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is None:
                board_image += "   "
            else:
                board_image += f" ${cell} "

            if j == (SIZE - 1):
               continue
            board_image += "|"

        if i == (SIZE - 1):
            continue
        board_image += "\n-----------\n"

    print(board_image)





def start_game():
    board = new_board()

    print_board(board)




start_game()