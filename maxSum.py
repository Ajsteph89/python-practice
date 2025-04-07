# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def max_sequence(arr):
    if not arr:  # Check if the array is empty
        return 0
    
    current_sum = 0
    max_sum = 0
    
    for num in arr:
        current_sum = max(num, current_sum + num)  # Either start a new subarray or continue the current one
        max_sum = max(max_sum, current_sum)  # Update the max_sum if the current_sum is higher
    
    return max_sum

print(max_sequence(arr))