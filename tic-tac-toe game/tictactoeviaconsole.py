import random


class InvalidMoveError(Exception):
    pass


class Board:
    def __init__(self):
        self._board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self._moves = []
        self._winner = None

    def make_move(self, v, h):
        if self.is_game_over():
            raise InvalidMoveError("Game is already over.")
        cell = self._board[v][h]
        if cell != " ":
            raise InvalidMoveError(
                f"Cell ({v+1}, {h+1}) is already occupied with {cell}."
            )
        player = self.get_current_player()
        self._moves.append((v, h))
        board = self._board
        board[v][h] = player
        if (
            board[v][0] == board[v][1] == board[v][2] != " "
            or board[0][h] == board[1][h] == board[2][h] != " "
            or board[0][0] == board[1][1] == board[2][2] != " "
            or board[2][0] == board[1][1] == board[0][2] != " "
        ):
            self._winner = player

    def is_game_over(self):
        return self.get_winner() is not None or len(self._moves) == 9

    def get_winner(self):
        return self._winner

    def get_current_player(self):
        if len(self._moves) % 2 == 0:
            return "X"
        return "O"

    def show(self):
        for i in range(len(self._board)):
            print("+---+---+---+")
            print("|", end="")
            for j in range(len(self._board)):
                print(f" {self._board[i][j]} |", end="")
            print()
        print("+---+---+---+")


def get_computer_move(board):
    while True:
        v = random.randint(0, 2)
        h = random.randint(0, 2)
        if board._board[v][h] == " ":
            print(f"\nComputer move is: {v + 1} {h + 1}")
            return v, h


def get_human_move(board):
    while True:
        move = input(f"\nHuman move is: ")
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


def get_move(board):
    if board.get_current_player() == "X":
        return get_human_move(board)
    else:
        return get_computer_move(board)


def game():
    board = Board()

    while not board.is_game_over():
        v, h = get_move(board)
        try:
            board.make_move(v, h)
        except InvalidMoveError as error:
            print(error)
            continue
        board.show()

    print("Game over!")
    winner = board.get_winner()
    if winner is not None:
        print(f"The winner is {winner}")
    else:
        print("Draw")


print("Welcome to the Tic Tac Toe game!")

while True:
    print("Let's play!")
    game()
