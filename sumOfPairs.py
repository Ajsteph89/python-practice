# Sum of Pairs
# Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

# If there are two or more pairs with the required sum, the pair whose second element has the smallest index is the solution.

ints = [10, 5, 2, 3, 7, 5]
s = 10

def sum_pairs(ints, s):
    seen = set()

    for num in ints:
        complement = s - num
        if complement in seen:  
            return [complement, num]
        seen.add(num)
    
    return None


print(sum_pairs(ints, s))