# Given an array of positive numbers, write a function that returns the greatest product of any three numbers. The approach of using three nested loops would clock in at O(N3), which is very slow. Use sorting to implement the function in a way that it computes at O(N log N) speed. (Some other implementations are even faster, but we’re focusing on using sorting as a technique to make code faster.)

# The greatest product of any three numbers would be the product of the three largest numbers, so sorting would make sense here. The nested loop solution would ostensibly be nested iterations over the same array. The Quicksort algorithm would give us O(NlogN) time efficiency.

def greatest_product(arr):
    quicksort(arr, 0, len(arr) - 1)

    factors = arr[-3:]

    product = 1
    for factor in factors:
        product *= factor

    return product

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

my_arr = [3, 10, 1, 2, 4]
print(greatest_product(my_arr))


