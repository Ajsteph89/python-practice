text = 'Hello World'
def alphabet_position(text):
    d = {} #empty dictionary
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(26):
        d[alpha[i]] = i+1 

    letters = ''.join(filter(str.isalpha, text.lower()))

    numbers = []
    for letter in letters:
        numbers.append(d.get(letter))

    num_strng = ",".join(str(x) for x in numbers)


    print(num_strng)
print(alphabet_position(text))
