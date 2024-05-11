# You are given a sentence represented by a string str. Your objective is to reverse all the characters in each word of the sentence while ensuring that the case of each character remains unchanged. The spaces between words should be preserved as they are, and the overall order of the words in the sentence must not be altered.

# A
# two-pointer start and end
# split sentence into words
# map words to arrays
# for each word_array
# - set start to 0 and end to len(word_array) - 1
# - while start < end
# -  swap values at start and end
# -  increment start and decrement end
# join word arrays into words
# join words into sentence
#

# time: O(sentence length)
# space: O(sentence length) => creating three data structures: words array, reversed words array, and letters array -> O(3*sentence length) => O(sentence length)

def reverse_word(word):
    letters = list(word)

    start = 0
    end = len(word) - 1

    while start < end:
        letters[start], letters[end] = letters[end], letters[start]
        start += 1
        end -= 1

    return ''.join(letters)

def reverse_words(sentence):
    words = sentence.split()

    reversed_words = map(reverse_word, words)

    return ' '.join(reversed_words)


print(reverse_words("Hello World") == "olleH dlroW")
print(reverse_words("JavaScript is fun") == "tpircSavaJ si nuf")
print(reverse_words("Coding in the sun") == "gnidoC ni eht nus")
print(reverse_words("Launch School") == "hcnuaL loohcS")
