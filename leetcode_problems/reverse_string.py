# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# A:
# split word into letters
# two pointers, left 0 and right len - 1
# while pointers are not crossed or ==
#   swap values at left and right indexes
#   left += 1
#   right -= 1
# return

# Time: O(N)
# Space: O(N), creating list from letters

def reverse_word(word):
    letters = list(word)

    left = 0
    right = len(letters) - 1

    while left < right:
        letters[left], letters[right] = letters[right], letters[left]
        left += 1
        right -= 1

    return ''.join(letters)

print(reverse_word('howdy') == 'ydwoh')
