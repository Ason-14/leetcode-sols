# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        p1 = 0
        p2 = len(s) - 1
        temp_str = ""
        while p1 < len(s)/2:
            temp_str = s[p1]
            s[p1] = s[p2]
            s[p2] = temp_str
            p1 += 1
            p2 -= 1
        print(s)

solution = Solution()
s = ["H", "a", "n", "", "n", " ",  "a", "h"]
solution.reverseString(s)