# Given a string s, find the length of the longest substring without repeating characters.

# anchor/runner
# if not string: return 0
# set anchor 0 and runner 0
# char_set = set()
# runner = 0
# count = 0
# max_count = 0
# loop until runner >= len(string)
# - if string[runner] not in char_set:
#   - add to char_set
#   - count += 1
#   - if count > max_count: max_count = count
# - else
#   anchor += 1
#   while string[char] != string[runner]:
#       char_set.remove(string[char])
#       count -= 1
#       anchor += 1
#   anchor += 1
#   runner += 1
#
# patterns:
# two-pointer anchor/runner

# time: O(N) => N = string length
# space: O(N) (for char_set)

def lengthOfLongestSubstring(string):
    if not string:
        return 0

    anchor = 0
    runner = 0
    count = 0
    max_count = 0

    char_set = set()

    while runner < len(string):
        if string[runner] not in char_set:
            char_set.add(string[runner])
            count += 1
            if count > max_count:
                max_count = count
        else:
            while string[anchor] != string[runner]:
                char_set.remove(string[anchor])
                count -= 1
                anchor += 1

            anchor += 1
        runner += 1

    return max_count


string = 'abcabcbb'
print(lengthOfLongestSubstring(string))

string = 'pwwkew'
print(lengthOfLongestSubstring(string))
