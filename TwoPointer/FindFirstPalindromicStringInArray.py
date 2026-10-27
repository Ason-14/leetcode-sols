#2108. Find First Palindromic String in the Array

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        
        for word in words:
            l = 0
            r = len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    break
                else:
                    l += 1
                    r -= 1
            if l >= r:
                return word

        return ""