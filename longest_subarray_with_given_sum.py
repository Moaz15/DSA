from typing import List

class Solution:
    def longestSubarrayWithSumK(self, nums:List[int], target: int) ->int:
        """
        Brute Force Approach 
        TC: O(n²), SC: O(1)
        """

        max_len = 0
        n = len(nums)
        
        for i in range(n):
            current_sum = 0
            for j in range(i,n):
                current_sum += nums[j]
                if current_sum == target:
                    max_len = max(max_len, j-i+1)
                    
        return max_len
    


if __name__ == '__main__':
    sol =Solution()
    nums = [10, 5, 2, 7, 1, 9]  
    k=15
    print(sol.longestSubarray(nums,k))






