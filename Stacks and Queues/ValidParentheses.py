# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        # implement stack as dynamic array
        stack = []
        if len(stack) == 1:
            return False
        try:
            for i in range(len(s)):
                if (s[i] == '(') or (s[i] == '[') or (s[i] == '{'):
                    stack.append(s[i])
                elif (s[i] == ')' and stack[-1] == '(') or (s[i] == ']' and stack[-1] == '[') or (s[i] == '}' and stack[-1] == '{'):
                    stack.pop()
                    continue
                else:
                    return False
        except:
            return False
        if len(stack) != 0:
            return False
        return True

# TESTING PURPOSES
solution = Solution()
ex1 = "(){}}{"
ex2 = "()[]{}"
ex3 = "(]"
ex4 = "([])"
print(solution.isValid(ex1))
print(solution.isValid(ex2))
print(solution.isValid(ex3))
print(solution.isValid(ex4))