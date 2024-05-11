# Write three different implementations of a function that finds the greatest number within an array. Write one function that is O(N2), one that is O(N log N), and one that is O(N).

def partition(array, left_pointer, right_pointer):
    # select last value in array as pivot
    pivot_index = right_pointer
    pivot_value = array[pivot_index]

    # reset right pointer to exclude pivot
    right_pointer -= 1

    while True:
        # advance left pointer until reaching value > pivot value
        while array[left_pointer] < pivot_value:
            left_pointer += 1

        # decrement right pointer until reaching value < pivot value
        while array[right_pointer] > pivot_value:
            right_pointer -= 1

        if left_pointer >= right_pointer:
            break
        else:
            array[left_pointer], array[right_pointer] = \
                array[right_pointer], array[left_pointer]
            left_pointer += 1

    array[left_pointer], array[pivot_index] = \
        array[pivot_index], array[left_pointer]

    return left_pointer


def quicksort(arr, left_index, right_index):
    # base case: right_index <= left_index
    # if right_index - left_index <= 0:
    if right_index <= left_index:
        return

    # partition to get pivot index
    pivot_index = partition(arr, left_index, right_index)

    quicksort(arr, left_index, pivot_index - 1)
    quicksort(arr, pivot_index + 1, right_index)

def greatest_number_n(arr):
    if not arr:
        return None

    # or could just use first value of array
    max = float('-inf')

    for val in arr:
        if val > max:
            max = val

    return max

def greatest_number_n2(arr):
    if not arr:
        return None

    for val in arr:
        if any([x for x in arr if x > val]):
            continue
        else:
            return val

def greatest_number_nlogn(arr):
    if not arr:
        return None

    quicksort(arr, 0, len(arr) - 1)

    return arr[-1]


my_arr = [8, 17, 1, 25, 456]

print(greatest_number_n(my_arr))
print(greatest_number_n2(my_arr))
print(greatest_number_nlogn(my_arr))
