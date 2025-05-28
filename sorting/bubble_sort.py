# Pushes the maximum to the last of the array by adjacent swaps
class Solution:
    def bubbleSort(self,nums):
        n = len(nums)
        end = n-1
        while end > 0:
            swapped = False
            for i in range(end):
                if nums[i] > nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1],nums[i]
                    swapped = True
            if not swapped:
                break
        return nums


if __name__ == "__main__":
    test_cases = [
        [],
        [1],
        [2, 1],
        [3, 1, 2],
        [5, 2, 9, 1, 5, 6],
        [1, 2, 3, 4, 5]
    ]

    sol = Solution()
    for case in test_cases:
        print(f"Original: {case} -> Sorted: {sol.bubbleSort(case.copy())}")

    