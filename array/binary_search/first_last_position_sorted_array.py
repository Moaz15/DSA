from typing import List 
class Solution:
    def first_last_position(self,nums:List[int],target:int)->List[int]:
        # target_list = []                    # Solution 1 , TC : O(N), SC : O(N)
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         target_list.append(i)
        # return [target_list[0],target_list[-1]] if target_list else [-1,-1]
 
        # start , end  = -1, -1             # Solution 2 , TC : O(N) , SC : O(1)
        # for i,num in enumerate(nums):
        #     if num == target:
        #         if start == -1:          # first time seeing target
        #             start = i
        #         end = i                  # keep updating last
        # return [start,end]

        def findFirst():
            low ,high = 0, len(nums)-1 
            index = -1 
            while low <= high:
                mid = (low+high)//2
                if nums[mid] == target:
                    index = mid 
                    high = mid -1    # look left 
                elif nums[mid] > target:
                    high = mid -1 
                else:
                    low = mid + 1
            return index 
        
        def findLast():
            low ,high = 0, len(nums)-1 
            index = -1
            while low <= high:
                mid = (low+high)//2
                if nums[mid] == target:
                    index = mid
                    low = mid +1        # look right 
                elif nums[mid] > target:
                    high = mid -1
                else:
                    low = mid +1
            return index
        first = findFirst()
        return[first,findLast()] if first != -1 else [-1,-1]

        





    


