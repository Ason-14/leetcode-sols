# 643. Maximum Average Subarray I

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        total = 0
        avg = 0
        max_avg = float('-inf')

        i = 0
        while i < k:
            total += nums[i]
            i += 1
        avg = total / k
        # if avg > max_avg:
        #     max_avg = avg
        max_avg = max(max_avg, avg)

        while i < n:
            total += nums[i]
            total -= nums[i - k]
            avg = total / k
            max_avg = max(max_avg, avg)
            i += 1
            
        return max_avg