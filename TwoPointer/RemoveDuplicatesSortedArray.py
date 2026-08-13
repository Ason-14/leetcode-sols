#26. Remove Duplicates from Sorted Array

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0
        R = 1
        # n = len(nums)
        
        while R < len(nums):
            if nums[R] != nums[L]:
                L += 1
                nums[L] = nums[R]
            R += 1
        
        return L + 1
