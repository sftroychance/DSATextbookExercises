# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.  Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

# from demo:
# we will do a binary search on the subarray sizes; we get a mid value and try the subarrays of that size; if we don't meet the target value with subarrays of that size, we won't meet it with smaller subarrays, so then we do a binary search on the subarray sizes larger than mid (left = mid + 1); if we do meet the target value, we try the smaller subarray sizes (right = mid - 1) to try to get to the minimal size

# we can't consider a binary search on the nums array, since we have to maintain the order of the elements in the subarrays

# the question gives a clue that binary search is involved with O(NlogN) complexity suggested

# A
# left = 0
# right = max subarray size = len(arr)
# loop
# - get midpoint of range of subarray sizes
# - set that as the window size
# - iterate over array with sliding window of that size
#   - if you encounter a window with sum >= target
#       - set result to this window size
#       - look for a smaller subarray size that meets the target; set right to mid - 1
#   - else there is no smaller subarray size that will reach the target
#       - set left to mid + 1
# return result

# some solutions on Leetcode use prefix sums
# the idea:
# for each value in the nums array, you calculate the sum of all values up to that point
# to calculate the sum of a window, you subtract the prefix sum for the start value from the prefix sum for the end value; this prevents you from having to recalculate sums as you iterate over the array
# prefix_sum = [0]
# for n in nums:
#     prefix_sum.append(prefix_sum[-1] + n)
#

def min_subarr_len(target, nums):
    left = 0
    right = len(nums)

    result = 0

    while left <= right:
        window_size = (left + right) // 2

        start = 0
        end = window_size - 1

        current_sum = 0
        for i in range(window_size):
            current_sum += nums[i]

        if current_sum >= target:
            result = window_size
            right = window_size - 1
            continue

        while end < len(nums) - 1:
            end += 1
            current_sum += nums[end]
            current_sum -= nums[start]
            start += 1
            if current_sum >= target:
                break

        if current_sum >= target:
            result = window_size
            right = window_size - 1
        else:
            left = window_size + 1

    return result

target = 7
nums = [2,3,1,2,4,3]
print(min_subarr_len(target, nums) == 2)

target = 4
nums = [1, 4, 4]
print(min_subarr_len(target, nums) == 1)

target = 11
nums = [1, 1, 1, 1, 1, 1, 1]
print(min_subarr_len(target, nums) == 0)

target = 15
nums = [1,2,3,4,5]
print(min_subarr_len(target, nums) == 5)

target = 15
nums = [5,1,3,5,10,7,4,9,2,8]
print(min_subarr_len(target, nums) == 2)
