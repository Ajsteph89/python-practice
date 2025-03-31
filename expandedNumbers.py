# You will be given a number and you will need to return it as a string in Expanded Form. For example:

#    12 --> "10 + 2"
#    45 --> "40 + 5"
# 70304 --> "70000 + 300 + 4"
# NOTE: All numbers will be whole numbers greater than 0.

num = 70304

def expanded_form(num):
    num_str = str(num)  # Convert number to string
    length = len(num_str)
    
    expanded = []
    
    for i, digit in enumerate(num_str):
        if digit != '0':  # Only expand if digit is non-zero
            place_value = int(digit) * (10 ** (length - i - 1))
            expanded.append(str(place_value))  # Add to result list
    
    return " + ".join(expanded)  # Join all parts with " + "

print(expanded_form(num))    

# alternate solution

def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

print(expanded_form(num))    
