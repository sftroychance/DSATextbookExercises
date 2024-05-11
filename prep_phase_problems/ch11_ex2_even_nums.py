# Use recursion to write a function that accepts an array of numbers and returns a new array containing just the even numbers.
def get_evens(arr):
    if not arr:
        return []

    if arr[0] % 2 == 0:
        return [arr[0]] + get_evens(arr[1:])
    else:
        return get_evens(arr[1:])

my_arr = [1, 2, 3, 4, 5]
print(get_evens(my_arr) == [2, 4])
