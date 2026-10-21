#387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dictt = {}
        for char in s:
            dictt[char] = dictt.get(char, 0) + 1
            
        for i, char in enumerate(s):
            if dictt[char] == 1:
                return i
            
        return -1