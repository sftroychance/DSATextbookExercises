# The following function finds the missing number from an array of integers; that is, the array is expected to have all integers from 0 up to the array’s length, but one is missing. As examples, the array [5, 2, 4, 1, 0] is missing the number 3, and the array [9, 3, 2, 5, 6, 7, 1, 0, 4] is missing the number 8. Here’s an implementation that is O(N2) (the clause if number not in array is itself already O(N), since the computer needs to search the entire array to find number):

# Use sorting to write a new implementation of this function that only takes O(N log N). (Some other implementations are even faster, but we’re focusing on using sorting as a technique to make code faster.)

# orig_function
def find_missing_number(array):
    for number in range(len(array) + 1):
        if number not in array: # not in array is by itself O(N) since the array has to be searched
            return number

    return None

def rev_find_missing_number(array):
    # sort the array
    quicksort(array, 0, len(array) - 1)

    for idx, val in enumerate(array):
        if idx != val:
            return idx

# quicksort/partition copied from previous assignment
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

my_arr = [3, 2, 4, 9, 0]

print(find_missing_number(my_arr))
print(rev_find_missing_number(my_arr))
