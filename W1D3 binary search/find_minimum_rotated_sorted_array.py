# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.


# after doing the peak exercise:
# we are looking for the peak in the array and returning the element after the peak
# if the peak is the last value, we are returning the first value
# however: trends don't work the same way; there is increasing and there is peak
# also, we know there is only one peak, not multiple possible peaks

# at each step we want to save the value of mid if less than our current min
# if we look at the left and right values when we pick our mid value:
# - if the mid value is greater than the right value, we want to search the right half
# - if the mid value is less than the right value, we want to search the left side

# A
# set minimum to -inf
# while left < right:
# calculate mid
# if arr[mid - 1] > arr[mid]:
#   return arr[mid]
#
# if arr[right] > arr[mid]:
#   set mid to minimum value (if less than existing minimum)
#   right = mid - 1
# else
#   check if right is < minimum and swap if it is
#   left = mid + 1

def find_min(arr):
    if arr[0] <= arr[-1]:
        return arr[0]

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # if (mid == 0 and arr[mid] < arr[-1]) or arr[mid - 1] > arr[mid]:
        if arr[mid - 1] > arr[mid]:
            return arr[mid]

        if arr[right] > arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

print(find_min([3,4,5,1,2]) == 1)
print(find_min([4,5,6,7,0,1,2]) == 0)
print(find_min([11,13,15,17]) == 11)
print(find_min([1]) == 1)
print(find_min([5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4]) == 1)
