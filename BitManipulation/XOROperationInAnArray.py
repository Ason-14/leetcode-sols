#1486. XOR Operation in an Array

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [None] * n
        result = 0
        for i in range(n):
            nums[i] = start + 2 * i
        for i in range(len(nums)):
            result = result ^ nums[i]
        return result