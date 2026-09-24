#506. Relative Ranks

import heapq

class Solution:
    def findRelativeRanks(self, scores: list[int]) -> list[str]:
        heap = []
        
        for i, score in enumerate(scores):
            heapq.heappush_max(heap, (score, i))
        
        print(heap)

        answer = [""] * len(heap)

        for n in range(len(heap)):
            (score, i) = heapq.heappop_max(heap)

            rank = n + 1

            if rank == 1:
                answer[i] = "Gold Medal"
            elif rank == 2:
                answer[i] = "Silver Medal"
            elif rank == 3:
                answer[i] = "Bronze Medal"
            else:
                answer[i] = str(rank)

            # print(answer)

        return answer