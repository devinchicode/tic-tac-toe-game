import random

x_symbol = "X"
o_symbol = "O"
player_1 = "Jackson"
player_2 = "Super Mario"


def create_board():  # Create the game board.
    board = [["00", "01", "02"],
             ["10", "11", "12"],
             ["20", "21", "22"]]
    return board


def rules():  # Tic - Tac - Toe rules.
    rules_open_message = """Welcome to my Tic-Tac-Toe game. Two players method. You need to do a strike of 3 symbols 
    in line horizontal, vertical or diagonal. The most important thing is to do it faster than your enemy, 
    other way you loss! If the whole board finished and there is no place to put your symbols while no one have 
    strike of his own three symbol, it will be Tie.
    Have Fun!"""
    return rules_open_message


def player_get_symbols():  # Each player get symbol.
    players_symbols_dict = {player_1: x_symbol,
                            player_2: o_symbol}
    return players_symbols_dict


def random_beginner():  # Randomize the symbols, every game the one who starts, start with "X" object.
    # This function randomize the object that do the first move.
    players_symbols_dict = player_get_symbols()
    beginner = random.choice(list(players_symbols_dict.keys()))
    second_player = ""

    if beginner == player_1:
        second_player = player_2
    elif beginner == player_2:
        second_player = player_1
    random_players_symbols = {beginner: x_symbol,
                              second_player: o_symbol}
    return random_players_symbols


random_beginner_var = random_beginner()


def return_key():
    # Get the key to know who start and who's th second one.
    # It's not like the first dictionary because we randomize the objects.
    # Need to know the winner by his symbol.
    beginner = ""
    second_player = ""
    players_dict = random_beginner_var

    count = 0
    for key in players_dict:
        count += 1
        if count == 1:
            beginner = key
        if count == 2:
            second_player = key
    return [beginner, second_player]


return_key_var = return_key()


def open_message():
    # Open message after randomize objects.
    # Give the players information which symbol each one get.
    message = ""
    random_players_symbols = random_beginner_var
    count = 0
    for key in random_players_symbols:
        count += 1
        if count == 1:
            message = ("%s is the beginner with %s symbol.\n" % (key, random_players_symbols[key]))
        elif count == 2:
            message += ("%s is the second player with %s symbol." % (key, random_players_symbols[key]))
    return message


def check_vertical(board: list):  # Check vertical win.
    winner = False
    players_keys_list = return_key_var

    if board[0][0] == board[1][0] == board[2][0]:
        if board[0][0] == "X":
            winner = ("the winner is %s." % (players_keys_list[0]))
        elif board[0][0] == "O":
            winner = ("the winner is %s." % (players_keys_list[1]))

    if board[0][1] == board[1][1] == board[2][1]:
        if board[0][1] == "X":
            winner = ("the winner is %s." % (players_keys_list[0]))
        elif board[0][1] == "O":
            winner = ("the winner is %s." % (players_keys_list[1]))

    if board[0][2] == board[1][2] == board[2][2]:
        if board[0][2] == "X":
            winner = ("the winner is %s." % (players_keys_list[0]))
        elif board[0][2] == "O":
            winner = ("the winner is %s." % (players_keys_list[1]))

    return winner


def check_horizontal(board: list):  # Check horizontal win.
    winner = False
    players_keys_list = return_key_var

    if board[0][0] == board[0][1] == board[0][2]:
        if board[0][0] == "X":
            winner = ("the winner is %s." % (players_keys_list[0]))
        elif board[0][0] == "O":
            winner = ("the winner is %s." % (players_keys_list[1]))

    if board[1][0] == board[1][1] == board[1][2]:
        if board[1][0] == "X":
            winner = ("the winner is %s." % (players_keys_list[0]))
        elif board[1][0] == "O":
            winner = ("the winner is %s." % (players_keys_list[1]))

    if board[2][0] == board[2][1] == board[2][2]:
        if board[2][0] == "X":
            winner = ("the winner is %s." % (players_keys_list[0]))
        elif board[2][0] == "O":
            winner = ("the winner is %s." % (players_keys_list[1]))

    return winner


def check_diagonal(board: list):  # Check diagonal win.
    winner = False
    players_keys_list = return_key_var

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            winner = ("the winner is %s." % (players_keys_list[0]))
        elif board[0][0] == "O":
            winner = ("the winner is %s." % (players_keys_list[1]))

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            winner = ("the winner is %s." % (players_keys_list[0]))
        elif board[0][2] == "O":
            winner = ("the winner is %s." % (players_keys_list[1]))

    return winner


def check_tie():  # if all other options are false &
    # turn_count is 9 in "check_winner" function (which means the whole columns are full and the game over).
    winner = "Tie"
    return winner


def validate_input(board: list):  #
    turn_count = 0
    get_user_mark = ""
    symbol = ""
    first_round = True  # Let the program know if it is the player first round or not, to know which message print.

    while turn_count < 9:  # Max game rounds by columns.
        value_exist_check = False
        """
        If the get_user_mark is in the board it will change this variable to "True".
        If it won't be "True", the "turn_count" variable won't add himself +1,
        what cause the symbol stay the same and not finish the turn.
        """

        print(f"{turn_count}")
        for value in board:  # Make the board shaped as Tic-Tac-Toe board.
            print(value)

        if turn_count % 2 == 0:
            symbol = "X"
        if turn_count % 2 != 0:
            symbol = "O"
        """
        Because the beginner always start with "X"
        And it once "X" and once "O", the turns were divide by this way. (Once "X", Once "O").
        """

        if first_round:
            get_user_mark = input("Which number in the board you would like to mark?: ")
        if not first_round:
            get_user_mark = input("Your value isn't in the board.\nEnter new one: ")

        for value in board:
            for index in value:
                if index == get_user_mark:
                    x = int(get_user_mark[0])
                    y = int(get_user_mark[1])
                    board[x][y] = symbol
                    value_exist_check = True

        if value_exist_check:
            turn_count += 1
            first_round = True

        if not value_exist_check:
            first_round = False

        if check_winner(board, turn_count):
            print(check_winner(board, turn_count))
            break

    return board


def check_winner(board: list, turn_count: int):
    winner = False

    if check_horizontal(board):
        winner = check_horizontal(board)
    if check_vertical(board):
        winner = check_vertical(board)
    if check_diagonal(board):
        winner = check_diagonal(board)
    if turn_count == 9:
        if not check_diagonal(board) and not check_vertical(board) and not check_horizontal(board):
            winner = check_tie()

    return winner
