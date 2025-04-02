# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

seconds = 359999

def make_readable(seconds):
    hours = seconds // 3600

    seconds = seconds - (hours*3600)
    
    minutes = seconds // 60
    
    seconds = seconds - (minutes*60)

    return f"{hours:02}:{minutes:02}:{seconds:02}"

print(make_readable(seconds))    


# alternate solution

def make_readable2(n):
    return f'{n//3600:02d}:{(n%3600)//60:02d}:{n%60:02d}'

print(make_readable2(seconds)) 