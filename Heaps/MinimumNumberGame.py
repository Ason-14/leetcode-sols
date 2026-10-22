#2974. Minimum Number Game

import heapq
from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        arr = []
        while nums:
            number1 = heapq.heappop(nums)
            number2 = heapq.heappop(nums)
            arr.append(number2)
            arr.append(number1)
        return arr