# Write a function that accepts a string that contains all the letters of the alphabet except one and returns the missing letter. For example, the string, "the quick brown box jumps over a lazy dog" contains all the letters of the alphabet except the letter "f".

def missing_letter(text):
    # a non-hash solution
    # alpha = 'abcdefghijklmnopqrstuvwxyz'

    # for letter in text:
    #     alpha = alpha.replace(letter, '')

    # return alpha

    # hash solution
    lookup = {}
    for letter in text:
        lookup[letter] = True

    for letter in alpha:
        if not lookup.get(letter):
            return letter

text = 'the quick brown box jumps over a lazy dog'
print(missing_letter(text) = 'f')
