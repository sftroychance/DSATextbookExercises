# You are given a list of songs where the ith song has a duration of time[i] seconds.

# Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

# Input: time = [30,20,150,100,40] sorted: [20, 30, 40, 100, 150]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:

# options:

# add a data structure
# create a lookup hash for the times given
# iterate over the values and see if there is a value in the lookup where current value + lookup value % 60 == 0
# -> bad solution - you would have to iterate over the entire lookup table to test %60

# two-pointer
# left = 0
# right = 0
# -> you would still have to do nested iteration essentially

# get the two highest values of the array to get the maximum total time
# integer divide by 60 to get the max total value we will encounter => max_mins
# place all the values in a lookup hash with a tally
# iterate over the values in the array:
# - iterate 1 to max_mins
#   - does lookup have a value i * 60 - current value?
#     - is the value equal to the current_value?
#       - is there an index in the lookup greater than current index?
#         - increment pairs result
#       - increment pairs result

# result: did not pass all tests, but not sure why, but it is overcomplicated in any case

# demo solution:
#


def numPairsDivisibleBy60(time_arr):
    # obtain total of maximum two values in the array and // 60
    # this gives us the maximum number of minutes (multiples of 60) in the array
    highest_max = 0
    lowest_max = 0

    for time in time_arr:
        if time > highest_max:
            lowest_max = highest_max
            highest_max = time
        elif time > lowest_max:
            lowest_max = time

    max_total = highest_max + lowest_max
    max_mins = max_total // 60

    # create a lookup table; key is the array value, value is an array of indexes containing that value
    lookup = {}
    for idx, time in enumerate(time_arr):
        lookup[time] = lookup.get(time, [])
        lookup[time].append(idx)

    # iterate over array
    # for each value, iterate over the multiples of 60 to see if there is a corresponding value in the lookup to meet the total sum
    # if the target value is equal to the current time, count how many indexes in the lookup table are greater than the current index (to prevent i ==j and to prevent duplication of a pair already found)
    pairs = 0
    for idx, time in enumerate(time_arr):
        for i in range(1, max_mins + 1):
            hash_target = (60 * i) - time
            if hash_target <= 0 or hash_target > highest_max:
                continue
            if hash_target == time:
                if max(lookup[hash_target]) > idx:
                # count how many indexes are greater than current index
                    higher_idx_count = 0
                    for j in lookup[hash_target]:
                        if j > idx:
                            higher_idx_count += 1

                    pairs += higher_idx_count
            elif hash_target in lookup and max(lookup[hash_target]) > idx:
                pairs += 1

    return pairs




time = [30,20,150,100,40]
print(numPairsDivisibleBy60(time))# == 3)

time = [60,60,60]
print(numPairsDivisibleBy60(time))# == 3)

time = [269,230,318,468,171,158,350,60,287,27,11,384,332,267,412,478,280,303,242,378,129,131,164,467,345,146,264,332,276,479,284,433,117,197,430,203,100,280,145,287,91,157,5,475,288,146,370,199,81,428,278,2,400,23,470,242,411,470,330,144,189,204,62,318,475,24,457,83,204,322,250,478,186,467,350,171,119,245,399,112,252,201,324,317,293,44,295,14,379,382,137,280,265,78,38,323,347,499,238,110,18,224,473,289,198,106,256,279,275,349,210,498,201,175,472,461,116,144,9,221,473]
print(numPairsDivisibleBy60(time))# == 105)
