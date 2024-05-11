# Write a function that checks whether a given positive integer num is the result of an integer multiplied by itself, which is typically referred to as a square integer. The function should return true if num is a square integer, otherwise false. The implementation should not rely on any square root computation provided by built-in Math library.

def is_square_integer(num):
    left = 0
    right = num

    while left <= right:
        mid = (left + right) // 2

        squared = mid * mid

        if squared == num:
            return True
        elif squared < num:
            left = mid + 1
        else:
            right = mid - 1

    return False

print(is_square_integer(1) == True)
print(is_square_integer(4) == True)
print(is_square_integer(16) == True)
print(is_square_integer(14) == False)
print(is_square_integer(25) == True)
print(is_square_integer(26) == False)
