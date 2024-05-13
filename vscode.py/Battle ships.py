import random
plan=int(input("Enter your level: "))
height=plan
width=plan
def create_grid(height, width):
    grid = [["O"] * width for _ in range(height)]
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(str(cell) for cell in row))

def place_ships(grid, num_ships):
    height = len(grid)
    width = len(grid[0])
    for _ in range(num_ships):
        while True:
            row = random.randint(0, height - 1)
            col = random.randint(0, width - 1)
            if grid[row][col] != 'O':
                grid[row][col] = 'O'
                break

def is_valid_guess(guess, grid):
    height = len(grid)
    width = len(grid[0])
    row, col = map(int, guess.split(','))
    return 0 <= row < height and 0 <= col < width

def check_guess(guess, grid):
    row, col = map(int, guess.split(','))
    if grid[row][col] == 'O':
        grid[row][col] = 'V'
        print('Hit!')
    else:
        grid[row][col] = 'X'
        print('Miss!')

def count_remaining_ships(grid):
    count = 0
    for row in grid:
        count += row.count('O')
    return count

def play_battleship(height, width, num_ships):
    grid = create_grid(height, width)
    place_ships(grid, num_ships)
    print('----- BATTLESHIP -----')
    print('Start guessing!')
    print_grid(grid)
    while True:
        guess = input('Enter your guess (row, col): ')
        if not is_valid_guess(guess, grid):
            print('Invalid guess! Try again.')
            continue
        check_guess(guess, grid)
        print_grid(grid)
        if count_remaining_ships(grid) == 0:
            print('Congratulations! All ships destroyed.')
            break


import random

# Function to create the game grid
def create_grid(size):
    grid = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append("O")
        grid.append(row)
    return grid

# Function to print the game grid
def print_grid(grid):
    for row in grid:
        print(" ".join(row))

# Function to place the battleships randomly on the grid
def place_battleships(grid, num_battleships):
    size = len(grid)
    for _ in range(num_battleships):
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        grid[x][y] = "B"

# Function to play the game

def play_game(grid):
    num_battleships = sum(row.count("B") for row in grid)
    attempts = 0
    while True:
        print("Attempts:", attempts)
        print_grid(grid)
        x = int(input("Enter row number (0 to {}): ".format(len(grid) - 1)))
        y = int(input("Enter column number (0 to {}): ".format(len(grid) - 1)))
        if grid[x][y] == "B":
            print("Congratulations! You sunk a battleship!")
            num_battleships -= 1
            grid[x][y] = "X"
        else:
            print("Oops! You missed!")
            grid[x][y] = "M"
        attempts += 1
        if num_battleships == 0:
            print("Congratulations! You sunk all the battleships!")
            break

# Main function
def main():
    size = int(input("Enter the size of the grid: "))
    num_battleships = int(input("Enter the number of battleships: "))
    grid = create_grid(size)
    place_battleships(grid, num_battleships)
    play_game(grid)

# Run the main function
main()


import random

# Function to create the game grid
def create_grid(size):
    grid = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append("O ")
        grid.append(row)
    return grid

# Function to print the game grid
def print_grid(grid):
    for row in grid:
        print(" ".join(row))

# Function to generate random coordinates for the enemy battleship
def generate_coordinates(size):
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)
    return x, y

# Function to play the game
def play_game(grid, rounds):
    size = len(grid)
    enemy_x, enemy_y = generate_coordinates(size)
    for _ in range(rounds):
        print("Round:", _ + 1)
        print_grid(grid)
        coordinates = input("Enter comma-separated coordinates (row, column): ").split(",")
        x = int(coordinates[0].strip())
        y = int(coordinates[1].strip())
        if x < 0 or x >= size or y < 0 or y >= size:
            print("Oops! Coordinates are out of bounds.")
            continue
        if grid[x][y] == "X" or grid[x][y] == "V":
            print("Oops! You have already guessed that coordinate.")
            continue
        if x == enemy_x and y == enemy_y:
            print("Congratulations! You sunk the battleship!")
            grid[x][y] = "V"
            break
        else:
            print("Oops! You missed!")
            grid[x][y] = "X"
    else:
        
        print("Game over! The battleship was at coordinates ({}, {}).".format(enemy_x, enemy_y))
        grid[x][y]="v"
# Main function
def main():
    size = int(input("Enter the size of the grid: "))
    grid = create_grid(size)
    rounds = 5
    play_game(grid, rounds)

# Run the main function
main()