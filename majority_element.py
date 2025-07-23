# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

from typing import List 
class Solution:
    def majorityElement(self,nums:List[int]) -> int:

#### hashing   TC : O(N)  SC : O(N)
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num,0) + 1 
            if nums_dict[num] > len(nums)//2:
                return num

#### moore's voting algorithm TC : O(N)    SC : O(1)
# We vote for a candidate.
# If someone agrees → +1.
# If someone disagrees → -1.
# If votes become zero, we choose a new candidate.
# Even if you "cancel" one majority vote with one minority vote,
# Majority will survive at the end!

        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count +=1 
            else:
                count -=1 

        return candidate
        
