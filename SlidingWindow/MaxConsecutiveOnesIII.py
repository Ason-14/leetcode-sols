#1004. max Consecutive Ones III

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        L = K = max_len = 0
        n = len(nums)

        for R in range(n):
            if nums[R] == 0:
                K += 1
            while K > k:
                if nums[L] == 0:
                    K -= 1
                L += 1
            
            W = R - L + 1
            max_len = max(max_len, W)
            # print(W, L, R)
        
        return max_len
