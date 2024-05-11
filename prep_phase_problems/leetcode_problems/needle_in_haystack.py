# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# A:
# iterate over range 0 to (len(haystack) - len(needle)) => idx
#   if haystack[idx] == needle => return idx
# return -1

# Time: O(N) one iteration over string
# Space: O(1)


def needleInHaystack(haystack, needle):
    needle_size = len(needle)

    for idx in range(len(haystack) - needle_size + 1):
        if haystack[idx:idx + needle_size] == needle:
            return idx

    return -1

print(needleInHaystack('sadbutsad', 'sad') == 0)
print(needleInHaystack('howdy', 'dy') == 3)
