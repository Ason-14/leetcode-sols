#1431. Kids With the Greatest Number of Candies

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx = max(candies)
        result = [maxx - item <= extraCandies for item in candies]
        return result