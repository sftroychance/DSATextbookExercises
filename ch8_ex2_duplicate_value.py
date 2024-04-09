# Write a function that accepts an array of strings and returns the first duplicate value it finds. For example, if the array is ['a', 'b', 'c', 'd', 'c', 'e', 'f'], the function should return 'c', since it’s duplicated within the array. (You can assume that there’s one pair of duplicates within the array.)

def first_duplicate(arr):
    lookup = {}

    for item in arr:
        if lookup.get(item):
            return item
        else:
            lookup[item] = True

    return None

array = ['a', 'b', 'c', 'd', 'c', 'e', 'f']
print(first_duplicate(array) == 'c')
