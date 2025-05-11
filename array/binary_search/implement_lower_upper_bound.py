from typing import List 
class Solution:

    def upperBoundBinarySearch(self,nums:List[int],x:int)-> int:
        n = len(nums)
        low , high= 0 , n-1
        ans = n

        while low <= high:
            mid = (high+low)//2
            if nums[mid] > x:
                ans = mid 
                high = mid - 1 
            else:
                low = mid +1 
        return ans 

    def lowerBound(self,nums:List[int],target:int)->int:
        n = len(nums)
        low = 0
        high = n-1 
        ans = n                         # default if target is greater than all elements
        while low <= high:
            mid = (low+high)//2
            if nums[mid] >= target:
                ans = mid             # possible answer 
                high = mid -1 
            else:
                low = mid +1
        return ans








     



    



 

    

