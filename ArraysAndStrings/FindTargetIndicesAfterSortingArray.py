#2089. Find Target Indices After Sorting Array

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if nums[i] == target:
                result.append(i)
        return result