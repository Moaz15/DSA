from typing import List
class Solution:
    def binarySearchAsc(self,nums:List[int],target:int)->int :

        n = len(nums)
        low = 0
        high = n-1
        while low <=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid 
            elif target > nums[mid]:
                low = mid + 1 
            else:
                high = mid - 1 
        return -1 
    
    def binarySearchRecursion(self, nums: List[int], target: int, low: int, high: int) -> int:
        # Recursive binary search
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.binarySearchRecursion(nums, target, mid + 1, high)
        else:
            return self.binarySearchRecursion(nums, target, low, mid - 1)






            

















    
    
