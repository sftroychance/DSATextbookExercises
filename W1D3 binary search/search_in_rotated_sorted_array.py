# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# A
# as with minimum in rotated array, when we select a mid index and check the value at that index and compare it to the value at the right index, we know which way to go
# if nums[mid] > nums[right] and target < nums[right] search right left = mid + 1
# else search left right = mid - 1

def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        before = mid - 1
        after = mid + 1

        # if nums[left] <= target < nums[mid]:
        #     right = before
        if nums[right] >= target > nums[mid]:
            left = after
        elif nums[right] < nums[mid] and (target > nums[mid] or target <= nums[right]):
            left = after
        else:
            right = before

    return -1

nums = [4,5,6,7,8,1,2,3]
target = 8
print(search(nums, target) == 4)

nums = [3, 1]
target = 1
print(search(nums, target) == 1)

nums = [3,5,1]
target = 3
print(search(nums, target) == 0)

nums = [1,3]
target = 3
print(search(nums, target) == 1)

nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target) == 4)

nums = [4,5,6,7,0,1,2]
target = 3
print(search(nums, target) == -1)

nums = [1]
target = 0
print(search(nums, target) == -1)

