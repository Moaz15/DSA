# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, 
# return the index where it would be if it were inserted in order.
from typing import List
class Solution:
    def searchInsert(self,nums:List[int],target)->int:
        low = 0
        high = len(nums) -1 
        ans = len(nums)
        while low <= high:
            mid = (low+high)//2
            if nums[mid] >= target:
                ans = mid
                high = mid -1 
            else:
                low = mid +1 
        return ans
            
