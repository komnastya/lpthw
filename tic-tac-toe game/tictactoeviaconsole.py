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
            raise InvalidMoveError(f"Cell ({v+1}, {h+1}) is already occupied with {cell}.")
        player = self.get_current_player()
        self._moves.append((v, h))
        self._board[v][h] = player
        if (self._board[v][0] == self._board[v][1] == self._board[v][2] != " "
                or self._board[0][h] == self._board[1][h] == self._board[2][h] != " "
                or self._board[0][0] == self._board[1][1] == self._board[2][2] != " "
                or self._board[2][0] == self._board[1][1] == self._board[0][2] != " "):
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


def get_move(board):
    while True:
        move = input(f"\nPlayer {board.get_current_player()} chose your move: ")
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
        print(f"The winner is {winner}\n")
    else:
        print ("Draw\n")



print("Welcome to the Tic Tac Toe game!\n")

while True:
    print("Let's play!\n")
    game()
