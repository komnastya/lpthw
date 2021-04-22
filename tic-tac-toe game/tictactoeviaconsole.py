class InvalidMoveError(Exception):
    def __init__(self, v, h, cell):
        self.h = h
        self.v = v
        self.cell = cell
        super().__init__(
            "Invalid move, cell ({}, {}) is already occupied with {}".format(
                self.v, self.h, self.cell))

class Board:
    def __init__ (self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.moves = []

    def winner(self, v, h):
        player = self.current_player()
        cell = self.board[v][h]
        if cell != " ":
            raise InvalidMoveError(v, h, cell)
        self.moves.append((v, h))
        self.board[v][h] = player
        if (self.board[v][0] == self.board[v][1] == self.board[v][2] != " "
                or self.board[0][h] == self.board[1][h] == self.board[2][h] != " "
                or self.board[0][0] == self.board[1][1] == self.board[2][2] != " "
                or self.board[2][0] == self.board[1][1] == self.board[0][2] != " "):
            if player == "X":
                return "A is winner"
            if player == "O":
                return "B is winner"
        if len(self.moves) == 9:
            return "Draw"
        return "Pending..."

    def current_player(self):
        if len(self.moves) % 2 == 0:
            return "X"
        return "O"

    def show(self, output):
        for i in range(len(self.board)):
            print("+---+---+---+")
            print("|", end="")
            for j in range(len(self.board)):
                print(f" {self.board[i][j]} |", end="")
            print()
        print("+---+---+---+")
        print(f"\n{output}")


def get_move(board):
    while True:
        move = input(f"Player {board.current_player()} chose your move: ")
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
    board = Board()
    while True:
        v, h = get_move(board)
        try:
            output = board.winner(v, h)
        except InvalidMoveError as error:
            print(error)
            continue
        board.show(output)
        if output != "Pending...":
            print("\nGame over!")
            break


print("Welcome to the Tic Tac Toe game!\n")

while True:
    print("Let's play!\n")
    game()
