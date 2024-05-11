# Given an array nums sorted in ascending order, determine the minimum between the count of positive integers and the count of negative integers.

# Please note that the number 0 is neither positive nor negative.

# A
# find last negative value
# find first positive value
# last_negative = -1
# first_positive = len(arr)

# find last negative number
# left = 0
# right = len(arr) - 1
# while left <= right:
# - get mid value
# - if arr[mid] is negative
#   - last_negative = max(last_negative, mid)
#   - left = mid + 1
# - else
#   - right = mid - 1

# find first positive number
# left = last_negative + 1
# right = len(arr) - 1
# while left <= right:
# - get mid
# - if arr[mid] is positive:
#   - first_positive = min(first_positive, mid)
#   - right = mid - 1
# - else
#   - left = mid + 1

# return min(last_negative, first_positive)

def find_last_negative(arr):
    left = 0
    right = len(arr) - 1
    last_negative = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < 0:
            # last_negative = max(last_negative, mid)
            last_negative = mid
            left = mid + 1
        else:
            right = mid - 1

    return last_negative

def find_first_positive(arr, last_negative):
    left = last_negative + 1
    right = len(arr) - 1
    first_positive = len(arr)

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > 0:
            # first_positive = min(first_positive, mid)
            first_positive = mid
            right = mid - 1
        else:
            left = mid + 1

    return first_positive

def minimum_count(arr):
    last_negative = find_last_negative(arr)
    negative_count = last_negative + 1
    positive_count = len(arr) - find_first_positive(arr, last_negative)

    return min(negative_count, positive_count)

print(minimum_count([-4, -3, -2, -1, 3, 4]) == 2)
print(minimum_count([-3, 1, 2, 3, 4, 5]) == 1)
print(minimum_count([-5, -4, -3, -2, -1]) == 0)
print(minimum_count([1, 2, 3, 4, 5]) == 0)
print(minimum_count([-2, -1, 1, 2]) == 2)
print(minimum_count([-7, -5, -4, 1, 2, 6, 10]) == 3)
print(minimum_count([-3, -2, -1, 0, 5, 6]) == 2)
print(minimum_count([-1, 0, 1]) == 1)
print(minimum_count([]) == 0)
