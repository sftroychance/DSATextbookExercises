# A peak element is an element that is strictly greater than its neighbors. (strictly greater just means not >=, only >).

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

def find_peak_element(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if mid == 0:
            pre_value = float('-inf')
        else:
            pre_value = arr[mid - 1]

        if mid == len(arr) - 1:
            post_value = float('-inf')
        else:
            post_value = arr[mid + 1]

        if pre_value < arr[mid] and post_value < arr [mid]:
            return mid
        elif pre_value < arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return None

print(find_peak_element([1,2,3,1]) == 2)
print(find_peak_element([1,2,1,3,5,6,4]) == 5)
