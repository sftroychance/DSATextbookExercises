# A
# partition step
# select pivot and swap that value with value at last index
# start is beginning of array, end is last index - 1 (to ignore pivot), pivot index is last index in array
# loop
# - increment left index until we reach a value > pivot
# - decrement right index until we reach a value < pivot
# - break if left index >= right index (pointers have met or crossed)
# - swap elements at left index and right index
# swap value at left index and pivot index
# return left index

# quicksort
# base case: if left index >= right index, return
# partition the array to get pivot index
# recursively call quicksort for left index to pivot - 1 and pivot + 1 to right index

def partition(arr, left_ptr, right_ptr):
    # select midpoint of array as pivot value
    mid_index = (left_ptr + right_ptr) // 2
    arr[right_ptr], arr[mid_index] = arr[mid_index], arr[right_ptr]

    pivot_idx = right_ptr
    right_ptr -= 1

    while True:
        while arr[left_ptr] < arr[pivot_idx]:
            left_ptr += 1

        while arr[right_ptr] > arr[pivot_idx]:
            right_ptr -= 1

        if left_ptr >= right_ptr:
            break

        arr[left_ptr], arr[right_ptr] = arr[right_ptr], arr[left_ptr]

    arr[left_ptr], arr[pivot_idx] = arr[pivot_idx], arr[left_ptr]

    return left_ptr

def quicksort(arr):

    def recurse(arr, start = 0, end = len(arr) - 1):
        if start >= end:
            return


        pivot = partition(arr, start, end)
        print(arr[pivot], arr)
        recurse(arr, start, pivot - 1)
        recurse(arr, pivot + 1, end)

    recurse(arr)

my_arr = [5, 4, 3, 8, 2, 1]
print(my_arr)
quicksort(my_arr)
print(my_arr)
