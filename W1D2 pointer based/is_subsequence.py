# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# A
# two pointers, one on substring, one on string
# set sub_pointer = 0, set str_pointer = 0
# while sub_ptr < len(substr) and str_ptr < len(string):
#   - if substr[sub_ptr] = str[str_ptr]
#       - increment both pointers
#   - else
#       - increment str_ptr
# return sub_ptr == len(substr)

def isSubsequence(substr, str):
    str_ptr = 0
    substr_ptr = 0

    while substr_ptr < len(substr) and str_ptr < len(str):
        if substr[substr_ptr] == str[str_ptr]:
            substr_ptr += 1
            str_ptr += 1
        else:
            str_ptr += 1

    print(substr_ptr, str_ptr)

    return substr_ptr == len(substr)

print(isSubsequence('abc', 'ahbgdc') == True)
print(isSubsequence('axc', 'ahbgdc') == False)
