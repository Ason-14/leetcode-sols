#2958. Length of longest subarray with max k frequency

from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_len, L, R = 0, 0, 0
        dictt = {}

        for R in range(n):
            dictt[nums[R]] = dictt.get(nums[R], 0) + 1

            while dictt[nums[R]] > k:
                dictt[nums[L]] -= 1
                L += 1
            
            W = R - L + 1
            max_len = max(max_len, W)

        return max_len