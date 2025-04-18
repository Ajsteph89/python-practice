# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

walk = ['n','s','n','s','n','s','n','s','n','s']

def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    directions = {
        'n':1,
        's':-1,
        'e':1,
        'w':-1
    }

    x,y = 0,0

    for d in walk:
        if d == 'n' or d == 's':
            x += directions[d]
        else:
            y += directions[d]

    return x == 0 and y == 0


print(is_valid_walk(walk))


# alternate solution:

def isValidWalk2(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

print(isValidWalk2(walk))