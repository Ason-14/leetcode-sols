#3069. Distribute Elements into Two Arrays I

from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        n = len(nums)
        for i in range(2, n):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        result = arr1 + arr2
        return result