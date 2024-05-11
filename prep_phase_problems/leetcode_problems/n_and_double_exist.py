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
    # solution does not account for [0, 0] and [0]
    # lookup = {val: True for val in arr}

    # for val in arr:
    #     if lookup.get(val * 2):
    #         return True

    # return False

    # lookup = {}

    # for idx, val in enumerate(arr):
    #     lookup[val] = lookup.get(val, [])
    #     lookup[val].append(idx)

    # for idx, val in enumerate(arr):
    #     if (val * 2) in lookup:
    #         if idx in lookup[val * 2]:
    #             if len(lookup[val * 2]) > 1:
    #                 return True
    #         else:
    #             return True

    # return False

    # O(N^2) here -- iterating over array, and in the loop iterating over array again
    # 'in' is O(N)
    for i in range(len(arr)):
        double = arr[i] * 2

        if double in arr[:i] or double in arr[i + 1:]:
            return True

    return False


print(n_and_double_exist([10, 2, 5, 3]) == True)
print(n_and_double_exist([3, 1, 7, 11]) == False)
print(n_and_double_exist([0, 0]) == True)
print(n_and_double_exist([0]) == False)
