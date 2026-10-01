#151. Reverse Words in a String

from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        stack = deque()
        word = ""
        result = []

        for char in s:
            if char != ' ':
                word += char
            else:
                if word:
                    stack.append(word)
                    word = ""
        if word:
            stack.append(word)
        
        while stack:
            result.append(stack.pop())

        return " ".join(result)
