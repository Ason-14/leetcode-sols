#1337. The K Weakest Rows in a Matrix

import heapq

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        heap = []

        for i, row in enumerate(mat):
            # soldier_count = sum(row)

            # optimise using binary search
            L = 0
            R = len(row)
            while L < R:
                M = L + (R - L) // 2
                if row[M] == 0:
                    R = M
                else:
                    L = M + 1

            heapq.heappush(heap, (L, i))
            print(i, row)
        print(heap)

        result = []

        for _ in range(k):
            (soldier_count, row_index) = heapq.heappop(heap)
            result.append(row_index)

        return result