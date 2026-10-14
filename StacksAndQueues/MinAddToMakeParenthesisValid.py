#921. Minimum Add to Make Parentheses Valid

from collections import deque

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = deque()
        for char in s:
            if char == '(':
                stack.append('(')
            elif char == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
        return len(stack)
