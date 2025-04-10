# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

from typing import List

class Solution:
    def SqrOfSortedArray(self, nums: List[int]) -> List[int]:
        p1 = 0
        p2 = len(nums) - 1
        result = [None] * len(nums)
        for i in range(len(nums)):
            if abs(nums[p2]) > abs(nums[p1]):
                result[(len(nums)-1) - i] = nums[p2] ** 2
                p2 -= 1
            else:
                result[(len(nums)-1) - i] = nums[p1] ** 2
                p1 += 1
        return result
    
solution = Solution()
nums = [-4, -1, 0, 3, 10]
print(solution.SqrOfSortedArray(nums))