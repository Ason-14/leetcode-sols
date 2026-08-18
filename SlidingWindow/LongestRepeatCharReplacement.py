# 424. Longest Repeating Character Replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = L = 0
        n = len(s)
        dictt = {}
        for R in range(n):
            dictt[s[R]] = dictt.get(s[R], 0) + 1
            K = sum(dictt.values()) - max(dictt.values())
            while K > k:
                dictt[s[L]] = dictt.get(s[L]) - 1
                L += 1
                K = sum(dictt.values()) - max(dictt.values())
            W = R - L + 1
            max_len = max(max_len, W)
            # print(L, R, max_len, dictt)
        return max_len