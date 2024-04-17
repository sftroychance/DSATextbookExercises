# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

# A:
# array to hash lookup
# iterate over array => val
#   return true if lookup.get(val * 2)
# return false

# Time: O(N) (iterate over array twice)
# Space: O(N) (hash lookup)

def n_and_double_exist(arr):
    lookup = {val: True for val in arr}

    for val in arr:
        if lookup.get(val * 2):
            return True

    return False


print(n_and_double_exist([10, 2, 5, 3]) == True)
print(n_and_double_exist([3, 1, 7, 11]) == False)
