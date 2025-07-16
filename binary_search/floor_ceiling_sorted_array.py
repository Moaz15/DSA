# Flooring
# In the context of a sorted array, the floor of a number x is:
# The greatest element in the array that is less than or equal to x.

#Ceiling
# The ceiling of a number x in a sorted array is:
# The smallest element in the array that is greater than or equal to x.

from typing import List 
class Solution:
    def floor_sorted_array(self,nums:List[int],target:int)->int:
        n = len(nums)
        low ,high = 0, n-1 
        ans = -1    # default to no floor 

        while low <= high :
            mid = (low + high)//2
            if nums[mid] <= target:
                ans = mid           # possible floor
                low = mid +1        # try to find a bigger one
            else:
                high = mid -1 
        return nums[ans] if ans != -1 else -1 
    
    def ceiling_sorted_array(self,nums:List[int],target:int)-> int:
        n = len(nums)
        low , high = 0, n-1
        ans = n
        while low <= high:
            mid = (low + high)//2
            if nums[mid] >= target:
                ans = mid 
                high  = mid -1  
            else:
                low = mid +1 
        return nums[ans] if ans != n else -1 
        
s = Solution()
print(s.ceiling_sorted_array([1, 3, 5, 7], 6))  # Output: 7
print(s.ceiling_sorted_array([1, 3, 5, 7], 8))  # Output: -1

            







