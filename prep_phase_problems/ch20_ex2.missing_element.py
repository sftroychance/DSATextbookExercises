def missing_element(arr):
    lookup = {}

    for num in arr:
        lookup[num] = True

    for val in range(len(arr)):
        if not lookup.get(val, 0):
            return val

print(missing_element([8, 2, 3, 9, 4, 7, 5, 0, 6]))
print(missing_element([2, 3, 0, 6, 1, 5]))
