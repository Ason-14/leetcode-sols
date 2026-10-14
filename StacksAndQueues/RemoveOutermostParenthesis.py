#1021. Remove Outermost Parentheses

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        stack = []
        for char in s:
            if char == '(':
                if len(stack) > 0:
                    result.append(char)
                stack.append(char)
            else:
                if len(stack) > 1:
                    result.append(char)
                stack.pop()

        return "".join(result)