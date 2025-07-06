# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.


class Solution : 
    def missingNum(self,nums : List[int])-> List :
        n = len(nums)
        original_sum = n*(n+1)//2 
        sum_nums = 0 
        for num in nums:
            sum_nums  += num 

        return original_sum - sum_nums
