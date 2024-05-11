# In this provided, you're given an array of numbers nums, and a specific integer k. Your objective is to compute the average value of each contiguous subarray of length k within the given array.

# Requirements:

# The input will be an array of numbers and an integer k.
# You need to find the average of every contiguous subarray of size k in the array.
# The output should be an array containing these averages.

# A
# two-pointer
# start = 0, end = start + window - 1
# calculate initial running sum
# calculate initial average and add to averages array (result)
# while true:
# - decrement start value from running sum (action accompanying increment start)
# - increment start
# - increment end
# - break if end >= len(arr)
# - add end value to running sum
# - calculate new average and append to result (action accompanying decrement end)
# return averages


def find_averages(arr, window):
    start = 0
    end = window - 1

    running_sum = 0
    for i in range(window):
        running_sum += arr[i]

    averages = [running_sum / window]

    while end < len(arr) - 1:
        running_sum -= arr[start]
        start += 1
        end += 1
        running_sum += arr[end]

        averages.append(running_sum / window)

    return averages

print(find_averages([1, 2, 3, 4, 5, 6], 3) == [ 2, 3, 4, 5 ])
print(find_averages([1, 2, 3, 4, 5], 2) == [1.5, 2.5, 3.5, 4.5])
print(find_averages([10, 20, 30, 40, 50], 4) == [ 25, 35 ])
print(find_averages([5, 5, 5, 5, 5], 1) == [ 5, 5, 5, 5, 5 ])
print(find_averages([1, 3, 2, 6, -1, 4, 1, 8, 2], 5) == [2.2, 2.8, 2.4, 3.6, 2.8])
