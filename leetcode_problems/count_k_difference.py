# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

# A:
# lookup:
#   iterate over array, lookup[val] = [idx1, idx2, idx3]
# pairs = 0
# iterate over array with idx, val
#   if lookup(k - val), iterate over values array for target_idx > idx, pairs += 1
# return pairs

# revised:
# pairs = 0
# iterate over array in reverse
#   count = lookup[arr[idx] + k] + lookup[arr[idx] - k]
#   pairs += count
# return count

# Time: O(N), populating lookup and checking for pairs in one iteration
# Space: O(N), lookup hash

def count_k_difference(arr, diff):
    lookup = {}
    pairs = 0

    for idx in range(len(arr) - 1, -1, -1):
        current_value = arr[idx]
        lookup[current_value] = lookup.get(current_value, 0) + 1
        count = lookup.get(current_value + diff, 0) + lookup.get(current_value - diff, 0)
        pairs += count

    return pairs

print(count_k_difference([1,2,2,1], 1) == 4)
print(count_k_difference([3,2,1,5,4], 2) == 3)
print(count_k_difference([1, 3, 3], 2) == 2)
