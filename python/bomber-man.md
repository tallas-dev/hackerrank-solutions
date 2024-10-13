
[https://www.hackerrank.com/challenges/bomber-man/problem] 

In the "Bomberman Game" task on HackerRank, you're given a grid representing bombs ('O') and empty spaces ('.'). Bomberman can place and detonate bombs every second. The challenge is to compute the grid's state after a given number of seconds. The behavior follows specific rules where bombs explode after 3 seconds, affecting neighboring cells. The task asks for simulating this over several seconds to determine the grid's state.


Here is a Python solution for "The Bomberman Game" task:

```python
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

# Example usage
grid = ['.......', '...O...', '....O..', '.......', 'OO.....', 'OO.....']
n = 3
result = bomberMan(n, grid)
for row in result:
    print(row)
```

### Explanation:
- **Initial state (n = 1)**: The grid remains the same.
- **n = 2**: The grid is filled with bombs ('O').
- **n = 3**: Bombs explode, leaving a modified grid.
- The solution alternates between two precomputed grid states after initial explosions.
