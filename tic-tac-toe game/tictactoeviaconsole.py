class InvalidMoveError(Exception):
    def __init__(self, v, h, cell):
        self.h = h
        self.v = v
        self.cell = cell
        super().__init__(
            "Invalid move, cell ({}, {}) is already occupied with {}".format(
                self.v, self.h, self.cell))

board = None
moves = None


def reset_game():
    global board
    global moves
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    moves = []


def current_player():
    if len(moves) % 2 == 0:
        return "X"
    return "O"


def winner(v, h):
    player = current_player()
    cell = board[v][h]
    if cell != " ":
        raise InvalidMoveError(v, h, cell)
    moves.append((v, h))
    board[v][h] = player
    if (board[v][0] == board[v][1] == board[v][2] != " "
            or board[0][h] == board[1][h] == board[2][h] != " "
            or board[0][0] == board[1][1] == board[2][2] != " "
            or board[2][0] == board[1][1] == board[0][2] != " "):
        if player == "X":
            return "A is winner"
        if player == "O":
            return "B is winner"
    if len(moves) == 9:
        return "Draw"
    return "Pending..."


def show(output):
    for i in range(len(board)):
        print("+---+---+---+")
        print("|", end="")
        for j in range(len(board)):
            print(f" {board[i][j]} |", end="")
        print()
    print("+---+---+---+")
    print(f"\n{output}")


def get_move():
    while True:
        move = input(f"Player {current_player()} chose your move: ")
        parts = move.strip().split(" ")
        if len(parts) == 2:
            try:
                v, h = parts
                v, h = int(v), int(h)
                if 1 <= v <= 3 and 1 <= h <= 3:
                    return (v - 1, h - 1)
            except ValueError:
                pass
        print("Please enter two numbers in range [1,3]")


def game():
    reset_game()
    while True:
        v, h = get_move()
        try:
            output = winner(v, h)
        except InvalidMoveError as error:
            print(error)
            continue
        show(output)
        if output != "Pending...":
            print("\nGame over!")
            break


print("Welcome to the Tic Tac Toe game!\n")

while True:
    print("Let's play!\n")
    game()
