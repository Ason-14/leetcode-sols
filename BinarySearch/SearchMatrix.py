# 74. Search a 2D Matrix

import math
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # rows
        n = len(matrix[0]) # columns
        total = m * n
        L = 0
        R = total - 1

        while L <= R:
            mid = L + ((R - L) // 2)
            mid_i = math.floor(mid // n)
            mid_j = mid % n
            print(f"{L}, {R}, {mid}")
            if matrix[mid_i][mid_j] < target:
                L = mid + 1
            elif matrix[mid_i][mid_j] > target:
                R = mid - 1
            else:
                return True
        
        return False

sol = Solution()
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(sol.searchMatrix(matrix1))