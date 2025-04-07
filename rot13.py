# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.

message = "test"

def rot13(message):
    rot13 = ""

    for letter in message:
        if 'a' <= letter <= 'z':
            # Shift by 13 positions
            rot13 += (chr(((ord(letter) - ord('a') + 13) % 26) + ord('a')))
        # Check if character is an uppercase letter
        elif 'A' <= letter <= 'Z':
            # Shift by 13 positions
            rot13 += (chr(((ord(letter) - ord('A') + 13) % 26) + ord('A')))
        else:
            # If it's not a letter, just append the character as is
            rot13 += (letter)
    
    return rot13

print(rot13(message))