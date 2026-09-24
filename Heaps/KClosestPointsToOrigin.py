#973. K Closest Points to Origin

import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        result = []
        heap = []

        for point in points:
            dist_squared = point[0]**2 + point[1]**2
            heapq.heappush(heap, (dist_squared, point))
        
        for i in range(k):
            (dist_squared, point) = heapq.heappop(heap)
            result.append(point)

        return result