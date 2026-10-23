#378. Kth Smallest Element in a Sorted Matrix

import heapq

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        heap = []
        result = []

        for i in range(len(matrix)):
            tuple_ = (matrix[i][0], i, 0)
            heap.append(tuple_)
        
        heapq.heapify(heap)

        for _ in range(k):
            num, row, col = heapq.heappop(heap)
            result.append(num)
            if col + 1 < len(matrix[row]):
                heapq.heappush(heap, (matrix[row][col+1], row, col+1))
        
        return num