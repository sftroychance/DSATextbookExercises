# In this problem, you are provided with an ascending order array of integers, nums. Your task is to count the number of pairs in this array whose sum is greater than a given target value, target.

# Constraints:

# The array nums is sorted in ascending order.
# No duplicate pairs should be counted. For instance, if nums contains [1, 2] and target is 2, then (1, 2) is a valid pair since 1 + 2 > 2. You shouldn't include (2, 1)

# A
# start/end pointers
# start = 0, end = len(nums) - 1
# loop until pointers are equal or cross
# when start + end > target, all the values between start and end can form a pair with end; the output below shows the pairs, but we don't need to list the actual pairs, just return the count
# - we count the pairs by (end - start)
# - then we decrement end
# if start + end <= target: increment start
# return pairs

def count_pairs(nums, target_value):
    start = 0
    end = len(nums) - 1

    pairs = 0

    while start < end:
        if nums[start] + nums[end] > target_value:
            pairs += (end - start)
            end -= 1
        else:
            start += 1

    return pairs


print(count_pairs([1, 2, 3, 4, 5], 6) == 4)
# Pairs: (2, 5), (3, 4), (3, 5), (4, 5)

print(count_pairs([1, 2, 3, 4, 5], 8) == 1)
# Pair: (4, 5)

print(count_pairs([1, 3, 5, 7], 6) == 4)
# Pairs: (1, 7), (3, 5), (3, 7), (5, 7)

print(count_pairs([1, 2, 3, 4], 5) == 2)
# Pairs: (2, 4), (3, 4)

print(count_pairs([1, 2, 3, 4, 5], 10) == 0)
# No pairs
