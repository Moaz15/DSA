
class Solution():
    def secondLargestElement(self, nums:list[int])->int:
        if len(nums) < 2:
            return -1 
        largest_element = second_largest_element =  float('-inf')
        for num in nums:
            if num > largest_element:
                second_largest_element = largest_element 
                largest_element = num
            elif num > second_largest_element and num != largest_element :
                second_largest_element = num
        if second_largest_element == float('-inf'):
            return -1
        return second_largest_element
    

    
    


        
    


















