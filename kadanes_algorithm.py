# Given an integer array arr, find the contiguous subarray (containing at least one number) which
# has the largest sum and returns its sum and prints the subarray.

class Solution():
    def maxSubArray(self, nums:List[int])-> int:

#kadane's approach :

# Kadane's idea is used anywhere you have a continuous thing (sum, product, score) and 
# you want the "best streak" or "best continuous segment"!

        current_sum = 0
        max_sum = float('-inf')

        for num in nums:
            current_sum = max(num,current_sum + num)

            # At every step, two choices":
            # Start a new subarray from the current number (num).
            # Extend the previous subarray by adding the current number 
            # (current_sum + num).

            max_sum = max(max_sum,current_sum)
            # the best (largest) subarray sum seen anywhere up to now.

        return max_sum 


