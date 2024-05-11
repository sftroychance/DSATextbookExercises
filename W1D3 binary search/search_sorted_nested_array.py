# In this problem, you're presented with a nested array, matrix, which has two key characteristics:

# Each subarray in the matrix is sorted in ascending order.
# The first element of each subarray is larger than the final element of the preceding subarray.
# Your task is to determine whether a given integer, target, exists within this nested array.

# The time complexity of your solution should be O(log(M*N)).

# A
# binary search to find subarray
# left = 0, right = len(arr)
# while left < right:
# - get mid
# - if arr[mid][0] <= target <= arr[mid][-1]
#   return mid
# - if target > arr[mid][-1]:
#   - left = mid + 1
# - else
#   - right = mid - 1

# binary search of subarray to find element
# left = 0, right = len(subarray)
# while left < right:
# - get mid
# - if arr[mid] > target:
#   - right = mid - 1
# - else
#   - left = mid + 1

def find_subarray(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid][0] <= target <= arr[mid][-1]:
            return mid
        elif arr[mid][-1] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

def find_element(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

def find_in_nested_array(arr, target):
    subarray = find_subarray(arr, target)
    if subarray == None:
        return False

    element = find_element(arr[subarray], target)
    if element != None:
        return True

print(find_in_nested_array([[4, 8, 12], [16, 20, 24], [28, 32, 36]], 20) == True)
print(find_in_nested_array([[3, 6, 9], [12, 15, 18], [21, 24, 27]], 27) == True)
print(find_in_nested_array([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 19) == False)
print(find_in_nested_array([[10, 20, 30], [40, 50, 60], [70, 80, 90]], 10) == True)
print(find_in_nested_array([[15, 25, 35], [45, 55, 65], [75, 85, 95]], 5) == False)
