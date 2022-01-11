import sboxes
import copy
def subBytes(grid):
    for i in range(0, 4):
        for j in range(0, 4):
            grid[i][j] = sboxes.sbox[grid[i][j]]

def subBytesInv(grid):
    for i in range(0, 4):
        for j in range(0, 4):
            grid[i][j] = sboxes.sboxInv[grid[i][j]]


def shiftRows(grid):
    tmpGrid = copy.deepcopy(grid) # Python i dumb, tmpGrid = grid just copies the reference and built-in grid.copy dosent copy the sublist
    for i in range(1, 4):
        for j in range(0, 4):
            grid[i][j] = tmpGrid[i][(j+i) % 4]

def shiftRowsInv(grid):
    tmpGrid = copy.deepcopy(grid)
    for i in range(1, 4):
        for j in range(0, 4):
            grid[i][j] = tmpGrid[i][(j+(4-i)) % 4]
    


def mixColumns(grid):
    return grid

def addRoundKey(grid, roundkey):
    return grid


test = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4],]

