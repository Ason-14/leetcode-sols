# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

from typing import List

# since cannot divide, use prefix[i] * suffix[i]
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    l_mult = 1
    r_mult = 1
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n

    for i in range(n):
      j = (-i) - 1 # this makes the j a reverse iterator
      prefix[i] = l_mult
      suffix[i] = r_mult
      l_mult *= nums[i]
      r_mult *= nums[j]

    return [l*r for l,r in zip(prefix, suffix)]

test = Solution()
nums1 = [1, 2, 3, 4] # output = [24, 12, 8, 6]
nums2 = [-1, 1, 0, -3, 3] # output = [0, 0, 9, 0, 0]
test1 = test.productExceptSelf(nums1)
test1 = test.productExceptSelf(nums2)