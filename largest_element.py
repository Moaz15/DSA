from typing import List
class Solution:
    def largestElement(self, arr:List[int])-> int:
        largest_num = arr[0]
        for num in arr:
            if num > largest_num:
                largest_num = num
        return largest_num





