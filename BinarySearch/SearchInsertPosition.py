# 35. Search Insert Position

from typing import List

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    n = len(nums)
    L = 0
    R = n-1

    while L <= R:
      M = L + ((R - L) // 2)
      if nums[M] == target:
        return M
      elif target < nums[M]:
        R = M - 1
      else:
        L = M + 1
      # print(f"L: {L}, R: {R}, M: {M}")
    
    # if L == M:
    #   return R
    # if R == M:
    #   return L
    return L
    
sol = Solution()
nums = [1, 3, 5, 6]
test1 = print(sol.searchInsert(nums, 5))
test2 = print(sol.searchInsert(nums, 2))
test3 = print(sol.searchInsert(nums, 7))
test3 = print(sol.searchInsert(nums, -1))
