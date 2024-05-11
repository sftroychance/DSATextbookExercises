# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# A:
# two-pointer
# area is end - start * min(end, start)
# start = 0
# end = len - 1
# set max area to current area
# while end < start:
# - if value at start <= value at end, increment start, else decrement end
#   - increment/decrement until you reach a value that is higher than the current
# - get area and compare to max
# return max area

# when to increment start: increment start while next value is greater
# when to decrement end: decrement end when previous value is greater
# which to try first: the one with the minimum value
# =>
# pick smaller value of end and start (which you used when calculating area)
# save current value at that index
# increment/decrement that one until new value > current value
# get area and check against max
# repeat

def max_area(heights):
    start = 0
    end = len(heights) - 1
    max_area = (end - start) * min(heights[end], heights[start])

    while start < end:
        if heights[start] < heights[end]:
            current_value = heights[start]
            while start < end and heights[start] <= current_value:
                start += 1
        elif heights[start] > heights[end]:
            current_value = heights[end]
            while end > start and heights[end] <= current_value:
                end -= 1
        else:
            start += 1
            end -= 1

        area = (end - start) * min(heights[start], heights[end])
        print(start, end, area)
        if area > max_area:
            max_area = area

    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(max_area(height) == 49)

height = [1, 1]
print(max_area(height) == 1)


