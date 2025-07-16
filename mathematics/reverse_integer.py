
class Solution:

    def reverseInteger(self,nums) -> int:
        
        sign = -1 if nums < 0 else 1 
        rev = 0
        nums = abs(nums)

        while nums > 0:
            last_digit = nums%10
            rev = rev*10 + last_digit
            nums //= 10

        rev *= sign
        return rev 

            
