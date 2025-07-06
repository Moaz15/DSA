from typing import List

class Solution:
    def twoSum(self,nums:List,target:int)-> List:
        # Brute Force 
        # TC : O(N*N) , SC : O(1) 
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return -1
        
        # Hash Map 
        # TC : O(N) , SC : O(N)

        # seen = {}
        # for i,num in enumerate(nums):
        #     comp = target - num 
        #     if comp in seen:
        #         return [seen[comp],i]
        #     seen[num] = i 
        # return -1 

        # if sorted Binary Search 

        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     left , right = i+1 , len(nums) -1 
        #     while left <= right:
        #         mid = (left + right)//2
        #         if nums[mid] == complement:
        #             return [i,mid]
        #         elif nums[mid] > complement:
        #              right = complement -1 
        #         else:
        #             left = complement +1 
        # return -1 

        





if __name__ == '__main__':
    sol =Solution()

    nums = [2,7,11,15] 
    target = 9
    print(sol.twoSum(nums,target))

    nums = [3,2,4] 
    target = 6
    print(sol.twoSum(nums,target))

    nums = [3,3] 
    target = 6
    print(sol.twoSum(nums,target))

    nums = [2,7,11,15] 
    target = 10
    print(sol.twoSum(nums,target))



