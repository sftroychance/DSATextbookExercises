# iterate over each value in array
# call 2sum for the differnce between 0 and the current value
# have 2sum return the two values or None
# when you call 2sum, send the current index as invalid for the returned values

# two-sum with avoid_idx
# sort array
# start = 0
# end = len(arr) - 1
# result = []
# while true
# - continue if start or end is the avoid_idx
# - if arr[start] + arr[end] == target_sum
#   - append [start, end] to result
#   - start += 1
#   - end -= 1
# - else if arr[start] + arr[end] < target
#   - start += 1
# - else
#   - end -= 1
# - break if start >= end
# return result

# too slow for test cases

# alt approach:
# sort array
# result = [] -> had to change to set or it would timeout
# set three pointers i, j, k
# iterate over range 0 to len(arr) - 2
# iterate over array => i => idx
#   j = i + 1
#   k = len(arr) - 1
#   while j < k:
#   sum = arr[i] + arr[j] + arr[k]
#   - if sum == 0
#     - result.append(arr[i], arr[j], arr[k])
#   - elif sum > 0
#     - k -= 1
#   - else
#     - j += 1
# remove duplicates from result
# return result

# patterns:
# - three-pointer start and mid and end

# time: O(NlogN for sort and outer iteration) * N for inner iteration -> O(N^2) where N = array size
# space: O(N) for triplets set

def three_sum(arr):
    arr.sort()
    triplets = set()

    for i in range(len(arr) - 2):
        j = i + 1
        k = len(arr) - 1

        while j < k:
            sum = arr[i] + arr[j] + arr[k]
            if sum == 0:
                triplets.add((arr[i], arr[j], arr[k]))
                j += 1
            elif sum > 0:
                k -= 1
            else:
                j += 1

    if not triplets:
        return []

    result = []

    for triplet in triplets:
        result.append(list(triplet))

    return result

# def two_sum(arr, target_sum, avoid_idx):
#     start = 0
#     end = len(arr) - 1

#     result = []

#     while start < end:
#         if start == avoid_idx:
#             start += 1
#             continue
#         elif end == avoid_idx:
#             end -= 1
#             continue

#         if arr[start] + arr[end] == target_sum:
#             result.append([arr[start], arr[end]])
#             start += 1
#             end -= 1
#         elif arr[start] + arr[end] < target_sum:
#             start += 1
#         else:
#             end -= 1

#     return result

# def three_sum(arr):
#     arr.sort()
#     triples = []

#     for idx, num in enumerate(arr):
#         if num == 0:
#             continue
#         target_value = 0 - num
#         complements = two_sum(arr, target_value, idx)
#         for complement in complements:
#             triple = [num] + complement
#             triple.sort()
#             triples.append(triple)

#     # remove duplicates
#     triples.sort()
#     if not triples:
#         return []
#     result = [triples[0]]
#     for i in range(1, len(triples)):
#         if triples[i] != triples[i - 1]:
#             result.append(triples[i])

#     return result

print(three_sum([-1,0,1,2,-1,-4]))# == [[-1,-1,2], [-1,0,1]])
