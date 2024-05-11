# Given an m x n matrix, return all elements of the matrix in spiral order.
# constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

# P: return an array representing spiral traversal of a given matrix
# E: m == 1, n == 1, m == 1 and n == 1
# D: traversal of existing 2D array
# A:
# initialize four variables representing:
# - top row: top = 0
# - bottom row: bottom = len(matrix) - 1
# - start column: left = 0
# - end column: right = len(matrix[0] - 1)
# - current row = 0
# - current column = 0
# initialize result array
# loop while bottom > top or right > left
#   iterate over top row until reaching right
#   - append current value to result
#   - increment current column
#   increment top
#
#   iterate over end column until reaching bottom
#   - append current value to result
#   - increment current row
#   decrement right
#
#   iterate over bottom row until reaching left
#   - append current value to result
#   - decrement current column
#   decrement bottom
#
#   iterate over start column until reaching top
#   - append current value to result
#   - decrement current row
#   increment left
#
#  return result

# Algo refinement:
# My solution does not print the last value, and I think it has to do with how I'm incrementing/decrementing current_row and current_column. My solution is similar to the other solutions I've seen, with the difference that I'm maintaining those pointers but also using while loops for each row/column, as opposed to a range.

# previous solution
# def spiralOrder(matrix):
#     top = 0
#     bottom = len(matrix) - 1
#     left = 0
#     right = len(matrix[0]) - 1

#     current_row = 0
#     current_column = 0

#     result = []

#     while left <= right and top <= bottom:
#         while current_column < right:
#             result.append(matrix[current_row][current_column])
#             current_column += 1

#         top += 1

#         while current_row < bottom:
#             result.append(matrix[current_row][current_column])
#             current_row += 1

#         right -= 1

#         while current_column > left:
#             result.append(matrix[current_row][current_column])
#             current_column -= 1

#         bottom -= 1

#         while current_row > top:
#             result.append(matrix[current_row][current_column])
#             current_row -= 1

#         left += 1

#     return result


# revised solution:
def spiralOrder(matrix):
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    result = []

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for j in range(top, bottom + 1):
            result.append(matrix[j][right])
        right -= 1

        if (len(result) < len(matrix) * len(matrix[0])):

            for k in range(right, left - 1, -1):
                result.append(matrix[bottom][k])
            bottom -= 1

            for m in range(bottom, top - 1, -1):
                result.append(matrix[m][left])
            left += 1

    return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix) == [1,2,3,6,9,8,7,4,5])

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix) == [1,2,3,4,8,12,11,10,9,5,6,7])

matrix = [[1,2,3],[4, 5, 6],[7, 8, 9], [10,11,12]]
print(spiralOrder(matrix))

matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

print(spiralOrder(matrix))

# patterns
# -
