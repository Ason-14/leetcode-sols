# 3. Longest Substring Without Repeating Characters

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = max_len = 0
        n = len(s)
        dictt = {}

        for R in range(n):
            dictt[s[R]] = dictt.get(s[R], 0) + 1
            while dictt[s[R]] > 1:
                dictt[s[L]] -= 1
                L += 1
            W = R - L + 1
            max_len = max(max_len, W)
        
        return max_len