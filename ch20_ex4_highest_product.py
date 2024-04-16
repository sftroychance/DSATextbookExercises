def highest_product(arr):
    highest_high = float('-inf')
    lowest_high = float('-inf')
    lowest_low = float('inf')
    highest_low = float('inf')

    for num in arr:
        if num > highest_high:
            lowest_high = highest_high
            highest_high = num
        elif num > lowest_high:
            lowest_high = num

        if num < lowest_low:
            highest_low = lowest_low
            lowest_low = num
        elif num < highest_low:
            highest_low = num

    return max(
        highest_high * lowest_high,
        lowest_low * highest_low
    )


print(highest_product([5, -10, -6, 9, 4]))
