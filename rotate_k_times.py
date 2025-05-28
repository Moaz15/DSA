# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Left rotate an array by one place 

class Solution :
    def leftRotateOnePlace(self, nums:List[int])-> List:
        n = len(nums)
        start = 0
        end = 1
        while  end <= n -1:
            nums[start],nums[end] = nums[end],nums[start]
            start +=1 
            end +=1 

        return nums 



[1,2,3,4,5,6,7]
        
[2,3,4,5,6,7,1]
