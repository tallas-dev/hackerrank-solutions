
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#


    # Write your code here
def bomberMan(n, grid):
    if n == 1:
        return grid
    
    rows, cols = len(grid), len(grid[0])
    
    def detonate(grid):
        new_grid = [['O'] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'O':
                    new_grid[r][c] = '.'
                    if r > 0: new_grid[r-1][c] = '.'
                    if r < rows-1: new_grid[r+1][c] = '.'
                    if c > 0: new_grid[r][c-1] = '.'
                    if c < cols-1: new_grid[r][c+1] = '.'
        return new_grid
    
    grid = [list(row) for row in grid]
    
    if n % 2 == 0:
        return ['O' * cols for _ in range(rows)]
    
    grid_after_first = detonate(grid)
    grid_after_second = detonate(grid_after_first)
    
    return [''.join(row) for row in (grid_after_first if (n // 2) % 2 == 1 else grid_after_second)]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

