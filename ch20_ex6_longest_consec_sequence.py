def longest_consec_sequence(arr):
    lookup = {}
    max_length = 0

    for val in arr:
        lookup[val] = True

    for val in arr:
        if lookup.get(val - 1):
            continue

        seq_length = 1
        running_val = val
        while lookup.get(running_val + 1):
            seq_length += 1
            running_val += 1

        if seq_length > max_length:
            max_length = seq_length

    return max_length

print(longest_consec_sequence([19, 13, 15, 12, 18, 14, 17, 11]))
print(longest_consec_sequence([10, 5, 12, 3, 55, 30, 4, 11, 2]))
