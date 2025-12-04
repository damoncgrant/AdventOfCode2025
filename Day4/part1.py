
def checkValid(row: int, col: int, grid) -> bool:
    surrounding = 0

    # Check Above
    if row != 0:
        # Top Left
        if col != 0:
            if grid[row-1][col-1] == '@':
                surrounding += 1 
        # Top Middle
        if grid[row-1][col] == '@':
            surrounding += 1
        # Top Right
        if col != len(grid[row]) - 1:
            if grid[row-1][col+1] == '@':
                surrounding += 1

    # Check Below
    if row != len(grid) - 1:
        # Bottom Left
        if col != 0:
            if grid[row+1][col-1] == '@':
                surrounding += 1 
        # Bottom Middle 
        if grid[row+1][col] == '@':
            surrounding += 1
        # Bottom Right
        if col != len(grid[row]) - 1:
            if grid[row+1][col+1] == '@':
                surrounding += 1

    # Check Sides
    # Check Left
    if col != 0:
        if grid[row][col-1] == '@':
            surrounding += 1
    # Check Right
    if col != len(grid[row]) - 1:
        if grid[row][col+1] == '@':
            surrounding += 1

    return surrounding < 4

validRolls = 0

with open("input.txt", "r") as file:
    grid = file.readlines()
    for i in range(len(grid)):
        grid[i] = grid[i].strip()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                if checkValid(i, j, grid):
                    validRolls += 1

print(validRolls)
    