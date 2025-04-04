# In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.

# The string has the following conditions to be alphanumeric:

# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces / underscore

password = "alpha centari"

def alphanumeric(password):
    return password.isalnum()

print(alphanumeric(password))


# alternate solution

def alphanumeric2(string):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'
    for i in string:
        if i not in abc and i.lower() not in abc and i not in num:
            return False
    return True


print(alphanumeric2(password))
