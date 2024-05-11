# Use recursion to write a function that accepts a string and returns the first index that contains the character “x”. For example, the string, "abcdefghijklmnopqrstuvwxyz" has an “x” at index 23. To keep things simple, assume the string definitely has at least one “x”.

# def first_x(str, idx = 0):
#     if not str:
#         return 0

#     if str[0] == 'x':
#         return idx
#     else:
#         return first_x(str[1:], idx + 1)

# Without needing idx param:
# with each letter, add 1 to the return value if not x
# if x, return 0
def first_x(str):
    if str[0] == 'x':
        return 0

    return first_x(str[1:]) + 1

print(first_x('abcdefghijklmnopqrstuvwxyz') == 23)
