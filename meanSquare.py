# Complete the function that

# accepts two integer arrays of equal length
# compares the value each member in one array to the corresponding member in the other
# squares the absolute value difference between those two values
# and returns the average of those squared absolute value difference between each member pair.
# Examples
# [1, 2, 3], [4, 5, 6]              -->   9   because (9 + 9 + 9) / 3
# [10, 20, 10, 2], [10, 25, 5, -2]  -->  16.5 because (0 + 25 + 25 + 16) / 4
# [-1, 0], [0, -1]                  -->   1   because (1 + 1) / 2


array_a = [1, 2, 3]
array_b = [4, 5, 6]

def solution(array_a, array_b):
    total = 0

    for x,y in zip(array_a, array_b):
        total += (abs(x-y))**2
    
    return total / len(array_a)


print(solution(array_a, array_b))


# alternate solution

a = [1, 2, 3]
b = [4, 5, 6]

def solution(a, b):
    return sum((x - y)**2 for x, y in zip(a, b)) / len(a)

print(solution(a, b))