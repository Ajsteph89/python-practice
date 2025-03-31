# Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.

# Modern Roman numerals are written by expressing each digit separately starting with the leftmost digit and skipping any digit with a value of zero. There cannot be more than 3 identical symbols in a row.

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

n= 1666

def convert(n):
    roman_numerals = [
        (1000, "M"), 
        (900, "CM"), 
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"), 
        (9, "IX"), 
        (5, "V"), 
        (4, "IV"),
        (1, "I")
    ]
    
    result = ""

    for x, y in roman_numerals:
        # While num is larger than or equal to the current value, append the symbol and decrease num
        while n >= x:
            result += y
            n -= x

    return result

print(convert(n))