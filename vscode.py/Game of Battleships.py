from random import randint
print("hello to our Game of Battleships")
hard=int(input("how difficult u want to play from 1 to 8: "))

i=hard
h="0 "*i+"\n"
if hard<=8:
    for i in range(hard):
        print(h)

def get_ship_location():
    row=input('Please enter a ship row: ')
    while row not in hard :
        print("Please enter a valid row ")
        row=input('Please enter a ship row: ')
    col=int(input("Enter a ship column: "))
    while col not in hard:
         print("Please enter a valid column: ")
         col=int(input("Enter a ship column: "))
         return int(row)+1,int(col)+1

def creat_ship_location(board):
    for ship in range(hard):
        ship_r , ship_col=randint(range(hard)),randint(range(hard))
        while board[ship_r][ship_col]=="x":
              ship_r , ship_col=randint(range(hard)),randint(range(hard))
        board[ship_r][ship_col]=="x"

def count_hit_ships(board):
    c=0
    for row in row :
        for col in row :
            if col =="X":
                c+=1
    return c

turns=5
while turns>0:
    row,col=get_ship_location()
    

