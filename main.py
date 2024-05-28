import random

print("Welcome to tic-tac-toe. Place your 'X' or 'O' with 1-9")
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
current_player = "X"
winner = None
game_running = True


# printing game board
def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("______")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("______")
    print(board[6] + "|" + board[7] + "|" + board[8])


# take player input
def player_input(board):
    x = int(input("Mark your 'X'. Select position 1-9: "))
    if 1 <= x <= 9 and board[x-1] == "-":
        board[x - 1] = current_player
    else:
        print("That spot is already  taken.")


# check for win or tie
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True


def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True


def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True


def check_tie(board):
    global game_running
    if '-' not in board:
        print_board(board)
        print("It's a tie!")
        game_running = False


def check_win():
    global game_running
    if check_diagonal(board) or check_horizontal(board) or check_vertical(board):
        # if winner == '-':
        #     return game_running
        print(f"The winner is player {winner}")
        game_running = False


# switch players
def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


# computer
def computer(board):
    while current_player == 'O':
        position = random.randint(0,8)
        if board[position] == '-':
            board[position] = "O"
            switch_player()


# check for win or tie again
while game_running:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
    computer(board)
    check_win()
    check_tie(board)
