# 3718. Smallest Missing Multiple of K

from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dictt = {}
        mult = 0
        for i in range(n):
            if nums[i] % k == 0:
                dictt[nums[i]] = dictt.get(nums[i], 0) + 1
        print(dictt)

        while True:
            mult += k
            result = dictt.get(mult)
            if result == None:
                return mult