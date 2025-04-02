# In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

# Create as many "shufflings" as you can!

# Examples:

# With input 'a':
# Your function should return: ['a']

# With input 'ab':
# Your function should return ['ab', 'ba']

# With input 'abc':
# Your function should return ['abc','acb','bac','bca','cab','cba']

# With input 'aabb':
# Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

s = 'abc'

def permutations(s):
    if len(s) == 1:
        return s

    recursive_perms = []
    for c in s:
        for perm in permutations(s.replace(c,'',1)):
            recursive_perms.append(c+perm)

    return set(recursive_perms)

print(permutations(s))