# Given a binary array nums, find the maximum number of consecutive 1s in the array.

class Solution :
    def maxConsecutiveNums(self, nums: List[int])-> int:
        max_count = 0
        current_count = 0
        for num in nums:
            if num == 1 :
                current_count +=1
                max_count = max(max_count,current_count)
            else: 
                current_count = 0 
        return max_count

            