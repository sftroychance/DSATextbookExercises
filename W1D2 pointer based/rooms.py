# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# A:
# if not array return 0
# initialize groups array to contain last element of first subarray
# iterate range 1 to len(arr)
#   replaceFlag = False
#   iterate over groups array
#   - if first element of current arr >= group value
#       - replace group value with last value of current arr
#       - set replaceFlag = True
#   - if not replaceFlag
#       - groups array append last value of current arr
# return len of groups array

# time: O(NlogN) since we sort, N == size of array
# space: O(N)

def numberOfRooms(arr):
    if not arr:
        return 0

    arr.sort()

    groups = [arr[0][1]]

    for i in range(1, len(arr)):
        merged = False

        for j in range(len(groups)):
            if arr[i][0] >= groups[j]:
                groups[j] = arr[i][1]
                merged = True
                break

        if not merged:
            groups.append(arr[i][1])

    return len(groups)

print(numberOfRooms([[0, 30], [5, 10], [15, 20]]) == 2)
print(numberOfRooms([[7, 10], [2, 4]]) == 1)
print(numberOfRooms([[1, 2], [3, 4], [5, 6]]) == 1)
print(numberOfRooms([[1, 4], [2, 5], [3, 6]]) == 3)
print(numberOfRooms([[1, 3], [3, 6], [6, 8]]) == 1)
print(numberOfRooms([[1, 10]]) == 1)
print(numberOfRooms([[1, 3], [2, 4], [4, 6]]) == 2)
print(numberOfRooms([[1, 5], [2, 3], [4, 6], [5, 7]]) == 2)
print(numberOfRooms([[0, 5], [1, 3], [2, 6], [4, 7], [5, 9], [8, 10]]) == 3)
print(numberOfRooms([[1, 2], [2, 3], [3, 4], [4, 5]]) == 1)
print(numberOfRooms([[1, 20], [5, 10], [11, 15], [16, 18]]) == 2)
print(numberOfRooms([[1, 4], [1, 3], [1, 2], [1, 5]]) == 4)

