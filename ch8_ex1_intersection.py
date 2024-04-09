# Write a function that returns the intersection of two arrays. The intersection is a third array that contains all values contained within the first two arrays. For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8] is [2, 4].

# A:
# initialize lookup table
# populate lookup with larger array
# iterate over smaller array and select elements that also appear in the lookup table (comprehension)

def intersection(arr1, arr2):
    smaller, larger = sorted([arr1, arr2], key=len)

    lookup = {}

    for item in larger:
        lookup[item] = True

    return [val for val in smaller if lookup.get(val)]

array1 = [1, 2, 3, 4, 5, 24]
array2 = [0, 2, 4, 6, 8]
print(intersection(array1, array2) == [2, 4])
