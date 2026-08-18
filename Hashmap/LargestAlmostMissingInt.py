#3471. Find the Largest Almost Missing Integer

from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dictt = {} # dictionary to store frequency
        for i in range(n):
            dictt[nums[i]] = dictt.get(nums[i], 0) + 1
        print(dictt)
        if k == n:
            return max(nums)
        elif k == 1:
            return max((k for (k, v) in dictt.items() if v == 1), default = -1)
        else:
            # max(candidates, key=function)
            candidates = []

            if dictt[nums[0]] == 1:
                candidates.append(nums[0])         
            if dictt[nums[n - 1]] == 1:
                candidates.append(nums[n - 1])

            return max(candidates, default = -1)    