import random
def creat_grid(level):
    grid=[]
    for _ in range(level):
        row=[]
        for _ in range(level):
            row.append("O")
        grid.append(row)
        
    return grid


def print_grid(grid):
    for row in grid:
        print(" ".join(row))

    
def coordinates(level):
    r=random.randint(0, level-1 )
    c=random.randint(0, level-1 )
    return r,c

def play(grid,turns):
    level=len(grid)
    r_enemy,c_enemy=coordinates(level)
    for i in range(turns):
        print("turn:",i + 1)
        print_grid(grid)

        hit=input("Enter ypur hit in row and column(Please enter a comm separaded between row , column): ").split(",")

        r=int(hit[0])
        c=int(hit[1])
        
        if r<0 or r>=level or c<0 or c>=level:
            print("oops!that's not even in the ocen")
            continue
        if grid[r][c]=="X":
            print("u are Already hit that one")
            continue
        
        if r==r_enemy and c==c_enemy:
            grid[r][c]="V"
            print_grid(grid)
            print("congratulation!u sunk my battle ship")

            break

        else:
            if r == r_enemy or c == r_enemy:
                print("Whew! That was close!")
            else:
                print("Ha! Not even close!")
            print("u missed my battle ship")
            grid[r][c]="X"
            continue
            
    else:
        grid[r_enemy][c_enemy]="V"
        print_grid(grid)
        print("Game over my battle ship was at({},{})".format(r_enemy,c_enemy))
        

def main():
    print("welcome to our battle ship game , have fun!!")
    level=int(input("Enter diffiuclty level: "))
    turns=5
    grid=creat_grid(level)
    
    play(grid,turns)

main()