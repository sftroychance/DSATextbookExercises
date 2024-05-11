# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

from functools import cache

def min_path_sum(grid):
    last_row = len(grid) - 1
    last_column = len(grid[0]) - 1

    @cache
    def helper(row, column):
        if row > last_row or column > last_column:
            return float('inf')

        if row == last_row and column == last_column:
            return grid[row][column]

        return grid[row][column] + min(helper(row + 1, column), helper(row, column + 1))

    return helper(0, 0)

grid = [[1,3,1],[1,5,1],[4,2,1]]
output = 7
print(min_path_sum(grid) == output)

grid = [[1,2,3],[4,5,6]]
output = 12
print(min_path_sum(grid) == output)
