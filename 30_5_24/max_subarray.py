def maxSubArray(nums):
    max_sum = nums[0]  
    current_sum = nums[0]  

    
    for num in nums[1:]:
        # Determine whether to continue the current subarray or start a new subarray
        current_sum = max(num, current_sum + num)
        
        # Update the maximum sum found so far
        max_sum = max(max_sum, current_sum)
    
    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum sum of a contiguous subarray:", maxSubArray(nums))
