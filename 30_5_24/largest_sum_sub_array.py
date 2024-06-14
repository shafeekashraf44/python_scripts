def SUM(a, size):
    # Initialize max_far to the smallest possible value
    max_far = float('-inf')
    
    # Initialize max_ending to 0
    max_ending = 0
    
    # Iterate through the array
    for i in range(0, size):
        # Add the current element to max_ending
        max_ending = max_ending + a[i]
        
        # Update max_far if max_ending is greater
        if max_far < max_ending:
            max_far = max_ending
        
        # Reset max_ending to 0 if it becomes negative
        if max_ending < 0:
            max_ending = 0
    
    # Return the maximum subarray sum found
    return max_far

# Test the function with an example array
array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(SUM(array, len(array)))
