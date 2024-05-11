# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# comments
# binary search on the first digit of the subarrays to find the target subarray
#   after first loop, the right pointer will indicate the target subarray
# binary search on the subarray to find the target value

# Time: O(logN)
# Space: O(1)

def searchMatrix(matrix, target):
    left = 0
    right = len(matrix) - 1

    while left <= right:
        midpoint = (left + right) // 2
        value = matrix[midpoint][0]
        if value == target:
            return True
        elif value < target:
            left = midpoint + 1
        else:
            right = midpoint - 1

    subarr = matrix[right]

    left = 0
    right = len(subarr) - 1

    while left <= right:
        midpoint = (left + right) // 2
        value = subarr[midpoint]
        if value == target:
            return True
        elif value < target:
            left = midpoint + 1
        else:
            right = midpoint - 1

    return target == subarr[right]

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60], [72, 84, 93, 101]], 10) == True)
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 14) == False)
