class Solution:
    def isRotatedString(self,s:str,goal:str)->bool:
        #brute force  TC : O(n²) and SC : 	O(n)
        # if len(s) != len(goal):
        #     return False
        
        # for i in range(len(s)):
        #     rotated = s[i:] + s[:i]
        #     if rotated == goal:
        #         return True
        # return False 
        
        # optimized 
        return len(s) == len(goal) and goal in (s+s)
    


if __name__ == '__main__':
    sol =Solution()
    s = "abcde"
    goal = "cdeab"
    print(sol.isRotatedString(s,goal))
    s = "abcde"
    goal = "abced"
    print(sol.isRotatedString(s,goal))





