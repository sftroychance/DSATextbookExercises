# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.

# Note that 0 is neither positive nor negative.

# Solve the problem in O(logN) complexity

# Binary search on conditions:
#  - value at index is negative and value at index + 1 is 0 or positive
#  - value at index is positive and value at index - 1 is 0 or negative
# neg count = left index + 1
# pos count = len(arr) - right index
# return max of neg/pos

# Time: O(logN)
# Space: O(1)

def maximum_count(arr):
    if arr[-1] < 0 or arr[0] > 0:
        return len(arr)

    if arr[0] == 0 and arr[-1] == 0:
        return 0

    left = 0
    right = len(arr) - 1

    neg_stop = -1

    while left <= right:
        midpoint = (left + right) // 2

        if arr[midpoint] < 0 and arr[midpoint + 1] >= 0:
            neg_stop = midpoint
            break
        elif arr[midpoint] >= 0:
            right = midpoint - 1
        else:
            left = midpoint + 1

    left = 0
    right = len(arr) - 1

    pos_stop = len(arr) - 1
    while left <= right:
        midpoint = (left + right) // 2

        if arr[midpoint] > 0 and arr[midpoint - 1] <= 0:
            pos_stop = midpoint
            break
        elif arr[midpoint] > 0:
            right = midpoint - 1
        else:
            left = midpoint + 1

    return max(neg_stop + 1, len(arr) - pos_stop)


print(maximum_count([-2,-1,-1,1,2,3]) == 3)
print(maximum_count([-2,-1,-1,-1,2,3]) == 4)
print(maximum_count([1,1,1,2,3]) == 5)
print(maximum_count([-1,-1,-1,-2,-3]) == 5)
print(maximum_count([-3,-2,-1,0,0,1,2]) == 3)
print(maximum_count([0, 0, 0, 1]) == 1)
print(maximum_count([0, 0, 0, 0]) == 0)
print(maximum_count([0]) == 0)
print(maximum_count([-1, 1]) == 1)
