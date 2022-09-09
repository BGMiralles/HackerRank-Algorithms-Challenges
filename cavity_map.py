# Function Description:
#     Complete the cavityMap function in the editor below.
#     cavityMap has the following parameter(s):
#         string grid[n]: each string represents a row of the grid
#
# Returns:
#     string{n}: the modified grid
#
# Input Format:
#     The first line contains an integer `n`, the number of rows and columns in the grid.
#     Each of the following `n` lines (rows) contains `n` positive digits without spaces (columns) that represent the
#     depth at grid[row, column].

import os


def cavityMap(grid):
    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[0]) - 1):
            if grid[x][y - 1] < grid[x][y] and grid[x - 1][y] < grid[x][y] and grid[x + 1][y] < grid[x][y] and \
                    grid[x][y + 1] < grid[x][y]:
                grid[x] = grid[x][:y] + "X" + grid[x][y + 1:]

    return grid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
