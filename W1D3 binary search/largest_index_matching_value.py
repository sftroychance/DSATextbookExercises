# Given an array nums of distinct integers sorted in ascending order, your task is to find the largest index j such that nums[j] is equal to j. If no such index exists, return -1.

# A
# binary search
# find mid
# if mid = num[mid]
# - capture index as max_index
# - set left to mid + 1 to try to find a larger value
# else
# - if num[mid] > mid => all values to the right will have num[mid] > mid (*distinct* integers)
#   - right = mid - 1
# - else
#   - left = mid + 1

def find_largest_index(arr):
    left = 0
    right = len(arr) - 1
    max_index = -1

    while left <= right:
        mid = (left + right) // 2

        if mid == arr[mid]:
            max_index = max(max_index, mid)
            left = mid + 1
        elif arr[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1

    return max_index

print(find_largest_index([-1, 0, 2, 3]) == 3)
print(find_largest_index([0, 1, 2, 3, 4]) == 4)
print(find_largest_index([-5, 0, 3, 4, 7, 9]) == -1)
print(find_largest_index([-2, 0, 1, 3, 3, 5]) == 5)
print(find_largest_index([0]) == 0)
