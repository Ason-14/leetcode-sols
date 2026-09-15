#1046. Last Stone Weight

import heapq 
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        
        # max heap
        heapq.heapify_max(stones)
        print(stones)

        while len(stones) >= 2:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            # new_stone = y - x
            if x == y:
                pass
            else:
                new_stone = y - x
                heapq.heappush_max(stones, new_stone)

        if stones:
            return stones[0]
        return 0