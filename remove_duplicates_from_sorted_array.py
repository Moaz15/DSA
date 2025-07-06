from typing import List 
# Given a sorted array nums, remove the duplicates in-place so that each unique element appears only once.
# Return the new length k (number of unique elements).

# Concept : 
# "Use two pointers to move unique elements forward because duplicates are adjacent in sorted array."

class Solution :
    def removeDuplicates(self, nums:List[int])-> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i +=1 
                nums[i] = nums[j]
        return i + 1 
    
