# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# A:
# target_idx = 0
# iterate over range(1, len(arr)) => idx
#   continue if arr[idx] == arr[target_idx]
#   else target_idx += 1
#   arr[target_idx] = arr[idx]
# return target_idx + 1

# Time: O(N)
# Space: O(1)

def remove_duplicates(arr):
    target_idx = 0

    for idx in range(1, len(arr)):
        if arr[idx] == arr[target_idx]:
            continue

        target_idx += 1
        arr[target_idx] = arr[idx]

    print(arr)
    return target_idx + 1

print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]) == 5)
