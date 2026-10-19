#692. Top K Frequent Words

import heapq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        dictt = {}
        heap = []
        result = []

        for word in words:
            dictt[word] = dictt.get(word, 0) + 1
        
        for word,count in dictt.items():
            heapq.heappush(heap, (-count, word))
        
        for _ in range(k):
            count, word = heapq.heappop(heap)
            result.append(word)
        
        # print(heap)
        return result