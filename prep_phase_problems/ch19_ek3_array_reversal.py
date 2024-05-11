def reverse_array(arr):
    left_pointer = 0
    right_pointer = len(arr) - 1

    while left_pointer < right_pointer:
        arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
        left_pointer += 1
        right_pointer -= 1

    return arr

print (reverse_array(['a', 'b', 'c', 'd', 'e']));
