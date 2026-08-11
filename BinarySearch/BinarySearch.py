#704. Binary Search

from typing import List

class Solution:
    def binarySearch(self, nums = List[int], target = int) -> int:
        n = len(nums)
        L = 0
        R = n-1

        while (L <= R):
            M = L + ((R - L) // 2) # ALWAYS do this way to prevent integer overflow

            if target == nums[M]:
                return M
            elif target < nums[M]:
                R = M - 1
            else:
                L = M + 1

        return -1

sol = Solution()
arr1 = [-1, 0, 3, 5, 9, 12]
target1 = 9
arr2 = [-1, 0, 3, 5, 9, 12]
target2 = 2

test1 = print(sol.binarySearch(arr1, target1))
test2 = print(sol.binarySearch(arr2, target2))