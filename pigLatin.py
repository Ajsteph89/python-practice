# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
 # igPay atinlay siay oolcay
text = 'Quis custodiet ipsos custodes ?'

def pig_it(text):
    words = text.split(' ')

    pLatin = []
    for word in words:
        if word.isalpha(): 
            pLatin.append(word[1:] + word[0] + 'ay')
        else:
            pLatin.append(word)

    latinStrng = " ".join(str(x) for x in pLatin)
    print(latinStrng)
print(pig_it(text))

# alternate solution:
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

print(pig_it(text))