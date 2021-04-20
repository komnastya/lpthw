class InvalidMoveError(Exception):
    pass

def gameover (board, why):
    print (show(board, why), '\nGame over!')
    exit(0)

def winner(v, h, moves):
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    while len(moves) < 9:
        for istep, (v, h) in enumerate(moves):
            if board[v][h] != " ":
                raise InvalidMoveError()
            if istep % 2 == 0:
                board[v][h] = 'X'
            else:
                board[v][h] = 'O'
            if (
                    # check row v
                    board[v][0] == board[v][1] == board[v][2] != " "
                    # check col h
                    or board[0][h] == board[1][h] == board[2][h] != " "
                    # check diagonal 1
                    or board[0][0] == board[1][1] == board[2][2] != " "
                    # check diagonal 2
                    or board[2][0] == board[1][1] == board[0][2] != " "):
                if board[v][h] == 'X':
                    return gameover (board, 'A is winner')
                if board[v][h] == 'O':
                    return gameover (board, 'B is winner')
        return board, 'Pending...\n'
    if len(moves) == 9:
        return gameover (board, 'Draw')


def show(board, output):
    for i in range(len(board)):
        print("+---+---+---+")
        print('|', end='')
        for j in range(len(board)):
            print(f" {board[i][j]} |", end='')
        print()
    print('+---+---+---+')
    print(f'\n{output}')


def game():
    moves = []
    while True:
        v = (int(input('Choose the row ')) - 1)
        h = (int(input('Choose the column ')) - 1)
        if 0 <= v < 4 and 0 <= h < 4:
            moves.append((v, h))
            board, output = winner(v,h,moves)
            show(board, output)
        # TODO Check if the last move is valid.
        # continue this yourself
        # TODO Check when this game has ended.
        else:
            raise InvalidMoveError


print("Welcome to the Tic Tac Toe game!\n")

game()  # Start the game.
