class Solution :
    
    def isPalindrome(self,nums) -> bool:
        if nums < 0:
            return False 
        original = nums 
        rev = 0
        while nums > 0:
            last_digit = nums % 10
            rev = rev*10 + last_digit 
            nums //= 10
            
        return rev == original 

    