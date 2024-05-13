from random import randint

def create_board(size):
    board = []

    for _ in range(size):
        row=[]
        for _ in range(size):
            
            row.append("O")
        board.append(row)
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

print("Welcome to the game of Battleships!")
print(" ")

size = int(input("Enter grid size (difficulty level): "))

board = create_board(size)

ship_row = randint(0, size)
ship_col = randint(0, size)

print()

print("Turn 1")
print_board(board)

for turn in range(5):

    print(f"Enter comma separated coordinates from 0 to {size - 1}")
    guess_row, guess_col = [i for i in input("> ").split(",")]
    
    print()

    if int(guess_row) == ship_row and int(guess_col) == ship_col:
        print("Congratulations! You sunk my battleship!")
        board[int(guess_row)][int(guess_col)] = "V"
        break

    elif (int(guess_row) < 0 or int(guess_row)> size - 1) or (int(guess_col) < 0 or int(guess_col)> size - 1):
        print("Oops, that's not even in the ocean.")
        print("\n-------------------------------------\n")

    elif (board[int(guess_row)][int(guess_col)] == "X"):
        print("You guessed that one already.")
        print("\n-------------------------------------\n")
        board[int(guess_row)][int(guess_col)] = "X"

    else:
        if guess_row == ship_row or guess_col == ship_col:
            print("Whew! That was close!")
        else:
            print("Ha! Not even close!")

        print("You missed my battleship!")
        print("\n-------------------------------------\n")
        board[int(guess_row)][int(guess_col)] = "X"

    if turn == 4:
        print("Game Over")
        board[int(ship_row)][int(ship_col)] = "V"
        print_board(board)
    else:
        print("Turn", turn + 2)
        print_board(board)