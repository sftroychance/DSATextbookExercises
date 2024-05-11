# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

from functools import cache

def minimum_total(triangle):
    last_row = len(triangle) - 1

    @cache
    def helper(row, column):
        if row > last_row or column > len(triangle[row]):
            return 0

        print('current val', triangle[row][column])
        return triangle[row][column] + \
            min(helper(row + 1, column), helper(row + 1, column + 1))

    return helper(0, 0)


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
output = 11
print(minimum_total(triangle) == output)

triangle = [[-10]]
output = -10
print(minimum_total(triangle) == output)

