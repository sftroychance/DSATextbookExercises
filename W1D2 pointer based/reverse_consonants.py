# Given a string str, reverse only all the consonants in the string and return it. Consonants are all alphabetic characters except for the vowels 'a', 'e', 'i', 'o', and 'u', which can appear in both lower and upper cases. The consonants can appear more than once in the string.

# A
# two-pointer start and end
# convert string to list
# initialize start to 0, end to len(str) - 1
# while start pointer is less than end pointer:
#   - compare values, if both consonants
#       - swap
#       - increment start, decrement end
#   - else
#       - while str[start] in 'aeiouAEIOU':
#           increment start
#       - while str[end] in 'aeiouAEIOU':
#           decrement end
#   return joined list

def reverseConsonants(str):
    if not str:
        return ''

    if len(str) == 1:
        return str

    VOWELS = 'aeiouAEIOU'
    chars = list(str)

    start = 0
    end = len(str) - 1

    while start < end:
        if chars[start] not in VOWELS and chars[end] not in VOWELS:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1
            continue

        while chars[start] in VOWELS:
            start += 1

        while chars[end] in VOWELS:
            end -= 1

    return ''.join(chars)



print(reverseConsonants("") == "")
print(reverseConsonants("s") == "s")
print(reverseConsonants("hello") == "lelho")
print(reverseConsonants("leetcode") == "deectole")
print(reverseConsonants("example") == "elapmxe")
print(reverseConsonants("Consonants") == "sotnonasnC")
