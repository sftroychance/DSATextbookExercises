# Given a roman numeral, convert it to an integer.

# A:
# const lookup for letter values
# map letters to list of values from lookup
# map values with index
#   if val[index + 1] > val[index], val[index] *= -1, else val[index]
# return sum of array values

# Time: O(N) iterate over string twice
# Space: O(N) lookup hash

def roman_to_int(str):
    ROMAN_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    values = [ROMAN_VALUES[letter] for letter in str]

    for idx in range(0, len(values) - 1):
        if values[idx] < values[idx + 1]:
            values[idx] *= -1

    return sum(values)

print(roman_to_int('MCMXCIV') == 1994)
print(roman_to_int('III') == 3)
print(roman_to_int('LVIII') == 58)
