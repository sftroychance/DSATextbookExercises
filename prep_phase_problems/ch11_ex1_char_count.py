# Use recursion to write a function that accepts an array of strings and returns the total number of characters across all the strings. For example, if the input array is ["ab", "c", "def", "ghij"], the output should be 10 since there are ten characters in total.

def char_count(array):
    # if len(array) == 0:
    # better:
    if not array:
        return 0

    return len(array[0]) + char_count(array[1:])

print(char_count(["ab", "c", "def", "ghij"]) == 10)
