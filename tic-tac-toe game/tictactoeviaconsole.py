class InvalidMoveError(Exception):
    pass
    # TODO An an excersice, extend this class with the details about the invalid move,
    # such as `v` and `h` to show a pretty error message, such as:
    # "Invalid move, the cell (1, 2) is already occupied with 'X'."

def winner(moves):
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    for istep, (v, h) in enumerate(moves):
        if board[v][h] != " ":
            raise InvalidMoveError(f'Invalid move, the cell ({v}, {h}) is already occupied with "{board[v][h]}" ')
        mark = None
        if istep % 2 == 0:
            mark = 'X'
        else:
            mark = 'O'
        board[v][h] = mark
        if (board[v][0] == board[v][1] == board[v][2] != " "
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


def get_move():
    while True:
        move = input('\nChose your move: ')
        parts = move.strip().split(" ")
        if len(parts) == 2:
            try:
                v, h = parts
                v, h = int(v), int(h)
                if 1 <= v <= 3 and 1 <= h <= 3:
                    return (v - 1, h - 1)
            except ValueError:
                pass
        print('Please, enter two numbers in range [1,3] separated by space')

def game():
    moves = []
    while True:
        v, h = get_move()
        moves.append((v, h))
        board, output = winner(moves)
        show(board, output)
        if output != "Pending...":
            print("\nGame over!")
            break


print("Welcome to the Tic Tac Toe game!\n")

game()
