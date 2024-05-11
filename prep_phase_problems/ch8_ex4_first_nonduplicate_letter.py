# Write a function that returns the first non-duplicated character in a string. For example, the string, "minimum" has two characters that only exist once—the "n" and the "u", so your function should return the "n", since it occurs first.

# A:
# iterate over letters
# place each in hash - value is True on first find, 'x' subsequently
# iterate over letters
# if value for key is True, it was found only once

def first_nonduplicated(word):
    lookup = {}

    for letter in word:
        lookup[letter] = lookup.get(letter, 0) + 1

    for letter in word:
        if lookup.get(letter) == 1:
            return letter

print(first_nonduplicated('minimum') == 'n')
