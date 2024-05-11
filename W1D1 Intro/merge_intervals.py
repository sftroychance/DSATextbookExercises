# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# define groups array
# populate groups array with one subarray containing first element of intervals
# initialize index for groups array to 0
# loop remaining intervals array (1 to end):
# - if the interval overlaps with the interval in the current group, merge the new interval with the group interval
# - else append a new array containing the interval to groups and increment the groups index
# return groups array

def merge_two(arr1, arr2):
    return [min(arr1[0], arr2[0]), max(arr1[1], arr2[1])]

def merge(intervals):
    intervals.sort()

    groups = [intervals[0]]

    for idx in range(1, len(intervals)):
        if intervals[idx][0] <= groups[-1][1]:
            groups[-1] = merge_two(intervals[idx], groups[-1])
        else:
            groups.append(intervals[idx])

    return groups

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals) == [[1,6],[8,10],[15,18]])

intervals = [[1,4], [4,5]]
print(merge(intervals) == [[1, 5]])

intervals = [[1,4],[0,2],[3,5]]
print(merge(intervals) == [[0, 5]])

intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
print(merge(intervals) == [[1, 10]])
