# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-2): # better to use a for loop than a while loop
            if i > 0 and nums[i] == nums[i-1]:
                continue # skips the iteration if the value of i is a duplicate and skips to the next unique value

            # initialising the pointers at the start of each loop
            p1 = i + 1
            p2 = len(nums) - 1

            while p1 < p2:
                sum = nums[i] + nums[p1] + nums[p2]
                if sum == 0:
                    result.append([nums[i], nums[p1], nums[p2]])
                    # skip duplicates
                    while p1 < p2 and nums[p1] == nums[p1+1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2-1]:
                        p2 -= 1
                    # increment/decrement both pointers after finding a sum=0
                    # you move both because, disregarding duplicates, if you move p1 + 1 then the sum will be larger than 1 and vice versa with p2
                    p1 += 1
                    p2 -= 1
                elif sum < 0:
                    p1 += 1
                else:
                    p2 -= 1
        
        return result

solution = Solution()
nums = [-1,0,1,2,-1,-4]
print(solution.threeSum(nums))