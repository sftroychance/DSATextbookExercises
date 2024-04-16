def sort_temps(arr):
    lookup = {}

    for val in arr:
        lookup[val] = lookup.get(val, 0) + 1

    result = []

    for temp in range(95, 106):
        count = lookup.get(temp)

        if count:
            for i in range(count):
                result.append(temp)

    return result


print(sort_temps([98, 99, 95, 105, 104, 98, 101, 99, 100, 97]))
