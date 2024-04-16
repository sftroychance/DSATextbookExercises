def max_profit(arr):
    left = 0
    right = len(arr) - 1
    min = arr[left]
    max = arr[right]

    while left < right and arr[left] > arr[left + 1]:
        left += 1
        min = arr[left]

    while left < right and arr[right - 1] > arr[right]:
        right -= 1
        max = arr[right]

    while left < right:
        left += 1
        if arr[left] < min:
            min = arr[left];

        right -= 1
        if arr[right] > max:
            max = arr[right]

    if max > min:
        return max - min
    else:
        return 0


print(max_profit([10, 7, 5, 8, 11, 2, 6]))
print(max_profit([10, 7, 2, 8, 11, 5, 24]))
print(max_profit([9, 8, 7, 6, 5]))
print(max_profit([1, 2, 1, 4, 3]))
