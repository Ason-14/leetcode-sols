# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days 
# you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]

from typing import List

class Solution:
    def dailyTemp(self, temps: List[int]) -> List[int]:
        # create empty stack (dynamic array)
        stack = []
        # create output zero array with same length as temps
        array = [0] * len(temps)
        # iterate through temperatures
        for i in range(len(temps)): # be careful for index error when i=0
            while len(stack) > 0 and temps[i] > temps[stack[-1]]:
                array[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
            print(stack)
        return array

test = Solution()
temp1 = [73, 74, 75, 71, 69, 72, 76, 73]
print(test.dailyTemp(temp1))
        