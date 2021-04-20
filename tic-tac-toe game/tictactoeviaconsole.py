class InvalidMoveError(Exception):
    # TODO An an excersice, extend this class with the details about the invalid move,
    # such as `v` and `h` to show a pretty error message, such as:
    # "Invalid move, the cell (1, 2) is already occupied with 'X'."
    pass


def winner(moves):
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    for istep, (v, h) in enumerate(moves):
        if board[v][h] != " ":
            raise InvalidMoveError()
        mark = None
        if istep % 2 == 0:
            mark = 'X'
        else:
            mark = 'O'
        board[v][h] = mark
        if (
                board[v][0] == board[v][1] == board[v][2] != " "
                or board[0][h] == board[1][h] == board[2][h] != " "
                or board[0][0] == board[1][1] == board[2][2] != " "
                or board[2][0] == board[1][1] == board[0][2] != " "):
            if mark == 'X':
                return board, 'A is winner'
            if mark == 'O':
                return board, 'B is winner'
    if len(moves) == 9:
        return board, 'Draw'
    return board, 'Pending...'


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
        move = input('\nChose your move: ').strip()
        v, h = move.split(" ")
        v, h = int(v) - 1, int(h) - 1
        if 0 <= v < 4 and 0 <= h < 4:
            moves.append((v, h))
            board, output = winner(moves)
            show(board, output)
            if output == 'A is winner' or output == 'B is winner' or output == 'Draw':
                print('\nGame is over!')
                break
        else:
            # FIXME You are overeacting here.
            # It is the responsibility of the winner function to raise exceptions.
            # But here we can simply print an error message and continue the cycle.
            raise InvalidMoveError


print("Welcome to the Tic Tac Toe game!\n")

game()
