class InvalidMoveError(Exception):
    pass


def winner(list):
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    for istep, (v, h) in enumerate(list):
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
                return board, 'A is winner'
            if board[v][h] == 'O':
                return board, 'B is winner'
    if len(list) == 9:
        return board, 'Draw'
    return board, 'Pending'


def show(board, winner):
    for i in range(len(board)):
        print("+---+---+---+")
        print('|', end='')
        for j in range(len(board)):
            print(f" {board[i][j]} |", end='')
        print()
    print('+---+---+---+')
    print(f'\n{winner}')


input = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 2], [2, 2], [2, 0], [1, 0],
         [2, 1]]

board, winner = winner(input)
show(board, winner)
