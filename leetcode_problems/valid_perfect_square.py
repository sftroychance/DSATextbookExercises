# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

# Comments
# we can do a binary search, and instead of seeking a target value, we can seek a value that will produce the given number when it is squared.  If we continue until the left and right pointers cross or are equal, we can check the final value.

# test this:
# 25
# 1 - 12 too high; right set at 11
# 2 - 6 too high: right set at 5
# 3 - 2 too low: left set at 3
# 4 - 4 too low: left set at 5
# 5 right and left indexes are equal, with value of 5

# A:
# set left to 0, right to N
# loop until left >= right
#   get midpoint => left + right / 2
#   if result too high, right = midpoint - 1
#   if result too low, left = midpoint + 1
# return right

# Time: O(logN)
# Space: O(1)

def isPerfectSquare(num):
    left = 0
    right = num
    iterations = 1

    while left < right:
        iterations += 1
        midpoint = (left + right) // 2
        squared = midpoint * midpoint
        if squared == num:
            return True
        if squared <= num:
            left = midpoint + 1
        else:
            right = midpoint - 1
    print(iterations)
    return right * right == num

print(isPerfectSquare(25) == True)
print(isPerfectSquare(100) == True)
print(isPerfectSquare(3999) == False)
print(isPerfectSquare(1764) == True)
print(isPerfectSquare(2147483647) == True)

