# Binary search

# array - must be ordered
# find index of a value, or -1/None if not present
# start pointer = 0, end pointer = len(arr) - 1
# loop while start <= end
# - find midpoint of the array
# - check value at midpoint to see if it matches target_value
# - if values match, return midpoint
# - if value at midpoint is > target value, set end point at midpoint - 1
# - if value at midpoint < target value, set start pointer at midpoint + 1
# return None or -1


def binary_search(arr, target_value):
    start = 0
    end = len(arr) - 1


    while start <= end:
        middle = (end + start) // 2

        if arr[middle] == target_value:
            return middle
        elif arr[middle] > target_value:
            end = middle - 1
        else:
            start = middle + 1

    return -1

def recursive_binary_search(arr, target_value, end, start = 0):
    if start > end:
        return -1

    middle = (end + start) // 2

    if arr[middle] == target_value:
        return middle
    elif arr[middle] > target_value:
        return recursive_binary_search(arr, target_value, middle - 1, start)
    else:
        return recursive_binary_search(arr, target_value, end, middle + 1)


my_arr = [1, 2, 3, 4, 5]
target_value = 8
# print(binary_search(my_arr, target_value))
print(recursive_binary_search(my_arr, 2, len(my_arr) - 1))
print(recursive_binary_search(my_arr, 8, len(my_arr) - 1))
