# You have an ordered array nums consisting of integers. Your task is to determine whether there are any two distinct elements in the array where one element is exactly three times the value of the other element. The time complexity of the solution should be O(N).

# Restrictions:

# You should not use built-in methods like filter, map, reduce, or find.
# Do not use the includes method for checking existence in the array.
# Avoid using indexOf or lastIndexOf.

# P
# this is a pointer exercise, but my initial solution is to use a lookup hash
# this is still O(N)
# create lookup hash with each value
# iterate over array
# - is there a target in the lookup hash that is 3 * current value?
#   - return True
# return False

# note, only noticed on result: 0 is not considered valid for 3 * 0

# revise to two-pointer problem
# anchor/runner
# anchor = 0
# runner = 1
# pairs = 0# while runner < len(arr)
# - if runner value is 3* anchor value, return true
# - else if runner value is > 3 * value, increment anchor
# - else if runner value is < 3 * value, increment runner
# return False

# time: O(length of nums array); two-pointer is more efficient within same Big O; lookup method requires two iterations, while two-pointer requires just one
# space: two-pointer: O(1), lookup: O(length of nums array)

def check_triple_match(nums):
    # lookup = {}

    # for num in nums:
    #     lookup[num] = True

    # for num in nums:
    #     if num == 0:
    #         continue

    #     if num * 3 in lookup:
    #         return True

    # return False

    # revision to two-pointer
    anchor = 0
    runner = 1

    while runner < len(nums):
        if nums[runner] == 3 * nums[anchor]:
            return True
        elif nums[runner] < 3 * nums[anchor]:
            runner += 1
        else:
            anchor += 1

    return False


print(check_triple_match([1, 3, 9, 28]) == True)
print(check_triple_match([1, 2, 4, 10, 11, 12]) == True)
print(check_triple_match([0, 5, 7, 55]) == False)
print(check_triple_match([4, 5, 7, 9, 13, 15, 17]) == True)
print(check_triple_match([2, 6, 13, 54]) == True)
print(check_triple_match([1, 5, 17, 51]) == True)
print(check_triple_match([1, 2, 4, 8]) == False)
