class InvalidMoveError(Exception):
    # TODO An an excersice, extend this class with the details about the invalid move,
    # such as `v` and `h` to show a pretty error message, such as:
    # "Invalid move, the cell (1, 2) is already occupied with 'X'."
    pass


#def gameover(board, why):
 #   show(board, why) # you already call the show function after each move,
                     # so you can simplify by altering the game function.
                     # print this text in the game function instead.
  #  print('Game is over!')
    # FIXME This is a valid strategy to exit a programm,
    # but there are better alternatives.
    # Try to fix your code in such a way that the `game` function
    # simply returns when a game is over.
    # exit(0)

def winner(v, h, moves):
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    while len(moves) < 9:
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
                    # check row v
                    board[v][0] == board[v][1] == board[v][2] != " "
                    # check col h
                    or board[0][h] == board[1][h] == board[2][h] != " "
                    # check diagonal 1
                    or board[0][0] == board[1][1] == board[2][2] != " "
                    # check diagonal 2
                    or board[2][0] == board[1][1] == board[0][2] != " "):
                if mark == 'X':
                    return board, 'A is winner'
                if mark == 'O':
                    return board, 'B is winner'
        return board, 'Pending...\n'
    if len(moves) == 9:
        # FIXME Again, the purpose of this function is to simply determine
        # the current winner. By terminating the program it takes on itself
        # too many responsibilities.
        # FIXME No need for the `return` keyword. The gameover function never returns!
        return board, 'Draw'


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
        # To improve the user experience we can input both v and h in a single string:
        move = input('Chose your move: ').strip()
        v, h = move.split(" ")
        v, h = int(v) - 1, int(h) - 1
        if 0 <= v < 4 and 0 <= h < 4:
            moves.append((v, h))
            board, output = winner(v, h, moves)
            show(board, output)
            if output == 'A is winner' or output == 'B is winner' or output == 'Draw':
                print('\nGame is over!')
                break
            # TODO Determine if the game is over, show a message and break.
            # ok
        else:
            # FIXME You are overeacting here.
            # It is the responsibility of the winner function to raise exceptions.
            # But here we can simply print an error message and continue the cycle.
            raise InvalidMoveError


print("Welcome to the Tic Tac Toe game!\n")

game()  # Start the game.
