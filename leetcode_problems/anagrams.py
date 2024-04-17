# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case? casefold is the Unicode standard for case-insensitive comparison


# A:
# - casefold both strings
# - get hash tally of s
# - get hash tally of t
# return True if hash tallies are equal

# Time: O(N + M) (different word sizes) => O(N)
# Space: O(N + M) (two hashes) => O(N)

def isAnagram(s, t):
    word1 = s.casefold()
    word2 = t.casefold()
    lookup1 = {}
    lookup2 = {}

    for letter in word1:
        lookup1[letter] = lookup1.get(letter, 0) + 1

    for letter in word2:
        lookup2[letter] = lookup2.get(letter, 0) + 1

    return lookup1 == lookup2

print(isAnagram('rat', 'car') == False)
print(isAnagram('anagram', 'nagaram') == True)
