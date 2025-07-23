# Move all 0's to the end of the array while maintaining the relative order of the non-zero elements.
# in-place 

# concept :
# One pointer(insert_pos) tracks where the next non-zero element should be placed.
# The other pointer (num in the loop) iterates over each element in the array.
# This avoids unnecessary shifting and keeps the relative order of non-zero elements.

from typing import List
class Solution : 
    def moveZeroes(self, nums: List[int])-> List:

        # Two pass solution
    
        # insert_position = 0
        # for num in nums:
        #     if num != 0:
        #         num[insert_position] = num
        #         insert_position +=1 

        # while insert_position < len(nums):
        #     nums[insert_position] = 0
        #     insert_position +=1 

        # return num 

        # one pass solution 

        # insert_position = 0
        # for current in range(len(nums)):
        #     if nums[current] != 0:
        #         nums[insert_position], nums[current] = nums[current],nums[insert_position]
        #         insert_position  +=1 

        # return nums



            


                
            




