# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {letter: s.count(letter) for letter in set(s)}
        t_dict = {letter: t.count(letter) for letter in set(t)}
        if s_dict == t_dict:
            return True
        return False

solution = Solution()
s = "anagrams"
t = "nagaram"
solution.isAnagram(s, t)