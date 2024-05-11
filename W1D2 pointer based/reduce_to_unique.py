# Given an array of integers nums, sorted in ascending order (where elements are equal to or increase as you move through the array), your task is to implement a function reduceToUnique. This function should modify the array in-place ensuring that it starts with a sequence of unique elements each following their original order in the array. After these modifications, return the count of these unique elements.

# The elements in the latter part of the array, after the unique ones, are not important. The key requirement is that the array should remain the same object as the input and should be modified to reflect the changes.

# A
# two-pointer: anchor and runner
# if not array return 0
# set anchor to 0
# set runner to 1
# set count to 1
# while runner < length of array:
# - while arr[runner] == arr[anchor]
#   - runner += 1
# - anchor += 1
# - arr[anchor] = arr[runner]
# - count += 1
# return count

def reduce_to_unique(arr):
    if not arr:
        return 0

    anchor = 0

    for runner in range(1, len(arr)):
        if arr[runner] != arr[anchor]:
            anchor += 1
            arr[anchor] = arr[runner]
    # runner = 1

    # while True:
    #     while runner < len(arr) and arr[runner] == arr[anchor]:
    #         runner += 1

    #     if runner >= len(arr):
    #         break

    #     anchor += 1
    #     arr[anchor] = arr[runner]

    return anchor + 1

print(reduce_to_unique([3, 3, 5, 7, 7, 8]) == 4)
print(reduce_to_unique([1, 1, 2, 2, 2, 3, 4, 4, 5]) == 5)
print(reduce_to_unique([0]) == 1)
print(reduce_to_unique([-5, -3, -3, -1, 0, 0, 0, 1]) == 5)
print(reduce_to_unique([6, 6, 6, 6, 6, 6, 6]) == 1)
