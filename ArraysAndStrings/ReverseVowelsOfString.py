#345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        L = 0
        R = len(s) - 1
        vowels = set("AaEeIiOoUu")
        s_list = list(s)
        while L < R:
            if s_list[L] in vowels and s_list[R] in vowels:
                s_list[L], s_list[R] = s_list[R], s_list[L]
                L += 1
                R -= 1
            
            if s_list[L] not in vowels:
                L += 1
            if s_list[R] not in vowels:
                R -= 1
        return "".join(s_list)