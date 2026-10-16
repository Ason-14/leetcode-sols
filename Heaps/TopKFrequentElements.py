#347. Top K Frequent Elements

import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dictt = {}
        result = []
        for num in nums:
            dictt[num] = dictt.get(num, 0) + 1
        # print(dictt)
        for num, freq in dictt.items():
            heapq.heappush(result, (freq, num))
            if len(result) > k:
                heapq.heappop(result)

        return [tup[1] for tup in result]