# original code
def greatest_number(array):
    if not array:
        return None

    for i in array:
        # Assume for now that i is the greatest:
        is_i_the_greatest = True

        for j in array:
            # If we find another value that is greater than i,
            # i is not the greatest:
            if j > i:
                is_i_the_greatest = False

        # If, by the time we checked all the other numbers, i
        # is still the greatest, it means that i is the greatest number:
        if is_i_the_greatest:
            return i

print(greatest_number([15, 251, 1, 81]))

# revised to O(N)
def greatest_number_revision(arr):
    # set max to negative infinity
    # the array might have negative numbers, so 0 would not work
    max = -float('inf')

    for item in arr:
        if item > max:
            max = item

    return max

print(greatest_number_revision([15, -5, 251, 81]))

