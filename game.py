import random
import os
import time

# check if cell is alive or dead
def check_cell_status(grid, new_grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                check_live(grid, i, j, new_grid)
            else:
                check_dead(grid, i, j, new_grid)

# perform Conway's Game of Life rules on live cell
def check_live(grid, i, j, new_grid):
    if(find_live_neighbors(grid, i, j) in [2,3]):
        new_grid[i][j] = 1
    else:
        new_grid[i][j] = 0

# perform Conway's Game of Life rules on dead cell
def check_dead(grid, i, j, new_grid):
    if(find_live_neighbors(grid, i, j) == 3):
        new_grid[i][j] = 1

# determine how many live neighbors a cell has at position grid[i][j]
def find_live_neighbors(grid, i, j):
    count = 0

    #check left, right, up, down
    if i > 0 and grid[i-1][j] == 1:
        count += 1
    if i < len(grid)-1 and grid[i+1][j] == 1:
        count += 1
    if j > 0 and grid[i][j-1] == 1:
        count += 1
    if j < len(grid)-1 and grid[i][j+1] == 1:
        count += 1

    #check diagonals
    if i > 0 and j > 0 and grid[i-1][j-1] == 1:
        count += 1
    if i > 0 and j < len(grid)-1 and grid[i-1][j+1] == 1:
        count += 1
    if i < len(grid)-1 and j > 0 and grid[i+1][j-1] == 1:
        count += 1
    if i < len(grid)-1 and j < len(grid)-1 and grid[i+1][j+1] == 1:
        count += 1
    return count

#  generate starting grid of random values
def create_initial_grid(orthoganal_grid_size):
    grid = []
    for i in range(orthoganal_grid_size):
        grid.append([])
        for j in range(orthoganal_grid_size):
            grid[i].append(random.choice([0,1]))
    return grid

# generate empty grid of same orthoganal size as original for next generation
def create_grid(orthoganal_grid_size):
    grid = []
    for i in range(orthoganal_grid_size):
        grid.append([])
        for j in range(orthoganal_grid_size):
            grid[i].append(0)
    return grid

# convert live cells to smiley faces
def convert_to_simleys(grid):
    new_grid = create_grid(orthoganal_grid_size)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                new_grid[i][j] = ":)"
            else:
                new_grid[i][j] = "  "
    return new_grid

def show_grid_lines():
    show_lines = raw_input("Would you like to see grid lines? (Y or N): ")
    response = show_lines[0].lower()
    if response == "y":
        return True
    return False

# display the grid on screen. the variable "show_lines" is a global variable
# identifying whether the user would like to see the gridlines or not.
def show_grid(grid):
    new_grid = convert_to_simleys(grid)

    if show_lines:
        print(generate_cell_divider(grid))

    for g in new_grid:
        if show_lines:
            values = "|"
        else:
            values = ""
        for v in g:
            if show_lines:
                values += (" "+v+" |")
            else:
                values += " "+v+" "
        print(values)

        if show_lines:
            print(generate_cell_divider(grid))

def generate_cell_divider(grid):
    unit_divider = "_____"
    divider = ""

    for i in range(len(grid)):
        divider += unit_divider
    return divider

# boolean check to see if population is still alive. If not, then population
# died off, and we need to return False to break out of while-loop
def population_alive(grid):
    for g in grid:
        for v in g:
            if v == 1:
                return True
    return False

# boolean check to see if our population is in a continuous loop. If the states
# repeat twice, then we are in a loop and will continue in a loop, so use this
# flag to break out of while-loop
def loop_state(grid, new_grid):
    if grid == new_grid:
        return True

# run program with provided orthoganal size for grid.
def run(orthoganal_grid_size):
    os.system("clear")
    first_generation = create_initial_grid(orthoganal_grid_size)
    show_grid(first_generation)
    alive = True
    looping = False

    while(alive and not looping):
        time.sleep(1)
        os.system("clear")
        next_generation = create_grid(orthoganal_grid_size)
        check_cell_status(first_generation, next_generation)
        show_grid(next_generation)
        looping = loop_state(first_generation, next_generation)
        first_generation = next_generation
        alive = population_alive(first_generation)

    if looping:
        print("Current state will loop endlessly!")
    if not alive:
        print("Population Depleted!")

# grab user's preferred grid size, and run program.
if __name__ == "__main__":
    os.system("clear")
    orthoganal_grid_size = input("Enter the preferred size of your Orthoganal Grid: ")
    show_lines = show_grid_lines()
    run(orthoganal_grid_size)
