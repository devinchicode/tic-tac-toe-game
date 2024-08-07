from tic_tac_toe import *


def main():
    print(rules())
    print(open_message())
    board = create_board()
    validate_input(board)


if __name__ == main():
    main()
