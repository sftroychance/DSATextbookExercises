# Given an array nums, sorted in ascending order (where elements are equal to or increase as you move through the array), determine if a specified number, target, appears more than three times in the array. The function should return true if target is found at least four times, and false otherwise.

# A:
# find index of leftmost target
# find index of rightmost target
# return (rightmost - leftmost + 1) > 3

# find index of leftmost target
# left = 0, right = len(arr) - 1
# leftmost = len(arr)
# while left <= right:
# - find mid
# - if arr[mid] == target:
#   - leftmost = mid
#   - right = mid - 1
# - elsif arr[mid] < target:
#   - left = mid + 1
# - else
#   - right = mid - 1
# if leftmost < len(arr) return leftmost else return -1

# find index of rightmost target
# left = leftmost index, right = len(arr) - 1
# rightmost = -1
# while left <= right
# - find mid
# - if arr[mid] == target:
#   - rightmost = mid
#   - left = mid + 1
# - if arr[mid] < target:
#   - left = mid + 1
# - else
#   - right = mid - 1
#
# return leftmost

def find_leftmost_index(arr, target):
    left = 0
    right = len(arr) - 1
    leftmost = len(arr)

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            leftmost = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if leftmost < len(arr):
        return leftmost
    else:
        return -1

def find_rightmost_index(arr, leftmost, target):
    left = leftmost
    right = len(arr) - 1
    rightmost = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            rightmost = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return rightmost

def is_target_frequent(arr, target):
    leftmost = find_leftmost_index(arr, target)
    if leftmost == -1:
        return False

    rightmost = find_rightmost_index(arr, leftmost, target)
    return rightmost != -1 and (rightmost - leftmost + 1) > 3

print(is_target_frequent([1, 2, 3, 3, 3, 3, 4], 3) == True)
print(is_target_frequent([1, 1, 1, 1, 2, 3, 4], 1) == True)
print(is_target_frequent([1, 2, 3, 4, 5], 2) == False)
print(is_target_frequent([1, 1, 3, 4, 5], 2) == False)
print(is_target_frequent([2, 2, 2, 3, 3, 3, 4], 3) == False)
print(is_target_frequent([4, 4, 4, 4, 4, 4, 4], 4) == True)
