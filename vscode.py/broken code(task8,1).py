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
turns=5
board = create_board(size)



print()

s=len(board)
ship_row = randint(0, size-1)
ship_col = randint(0, size-1)
for turn in range(turns):


    print("Turn: ",turn+1)
    print_board(board)
    print(f"Enter comma separated coordinates from 0 to {size - 1}")
    guess_row, guess_col = [i for i in input("> ").split(",")]
    guess_row=int()
    guess_col=int()
    
    
#    print()

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        board[guess_row][guess_col] = "V"
        break

    elif guess_row < 0 or guess_row>= size or guess_col < 0 or guess_col>= size:
        print("Oops, that's not even in the ocean.")
        print("\n-------------------------------------\n")
        continue

    elif board[guess_row][guess_col]=="X": 
        print("u gussed that one already")
    else:
        if guess_row == ship_row or guess_col == ship_col:
            print("Whew! That was close!")
        else:
            print("Ha! Not even close!")

        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"
        print("\n-------------------------------------\n")
        
        continue

if turn == 4:
    print("Game Over")
    board[ship_row][ship_col] = "V"
    print_board(board)
    
else:
    print("Turn", turn + 2)
    print_board(board)
