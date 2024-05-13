def create_board(rows, cols):
    board = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(" ")
        board.append(row)
    return board

def print_board(board):
    print("-------------")
    for row in board:
        print('|', end=' ')
        for cell in row:
            print(cell, end=' | ')
        print("\n-------------")

def check_win(board):
    marks = ["X", "O"]
    for mark in marks:
        for row in board:
            if all(cell == mark for cell in row):
                return mark

        for col in range(len(board[0])):
            if all(row[col] == mark for row in board):
                return mark

        if board[0][0] == board[1][1] == board[2][2] == mark:
            return mark
        if board[0][2] == board[1][1] == board[2][0] == mark:
            return mark

    return ""

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True
print("Enter space separated coordinates from 0 to 2")
hit = input("> ").split(" ")
row=int[hit(0)]
col=int[hit(1)]
import random

   
def play_game():
    board = create_board(3, 3)
    print_board(board)

    player_turn = random.choice(["user", "computer"])

    while True:
        if player_turn == "user":
            board[row][col] = "X"

        else:
            row_o = random.randint(0,2)
            col_o = random.randint(0,2)
            board[row_o][col_o]="O"

        print_board(board)

        winner = check_win(board)
        if winner:
            print(f"{winner} wins!")
            break

        if check_tie(board):
            print("It's a tie!")
            break

        player_turn = "user" if player_turn == "computer" else "computer"

play_game()