#2798. Number of Employees Who Met the Target

from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for hour in hours:
            if hour >= target: 
                count += 1
        return count