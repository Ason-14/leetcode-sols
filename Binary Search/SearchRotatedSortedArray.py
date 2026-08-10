#33. Search in Rotated Sorted Array

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        L = 0
        R = n - 1

        # find min index
        while L < R:
            M = L + ((R - L) // 2)
            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M

        min_i = L # or R since they both point to the same thing

        # if nums is not rotated
        if min_i == 0:
            l = 0
            r = n - 1

        # if nums[0] <= target < nums[min_i]
        elif nums[0] <= target <= nums[min_i - 1]:
            l = 0
            r = min_i - 1

        # if nums right side
        else:
            l = min_i
            r = n - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1