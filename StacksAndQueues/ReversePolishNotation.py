# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

from typing import List

class Solution:
    def evalRPN(self, s: List[str]) -> int:
        # create empty stack (dynamic array)
        stack = []

        # iterate through string array
        for i in range(len(s)):
            # try and store the number (in int form) in the stack
            try:
                stack.append(int(s[i]))
            # if s[i] is not a number, perform the following
            except:
                # if string is an operand, calculate result using top 2 ints then pop them and replace them with the result
                # also check if there is index error
                # while len(stack) > 1:
                if (s[i] == '+'):
                    result = stack[-2] + stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(result)
                elif (s[i] == '-'):
                    result = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(result)
                elif (s[i] == '*'):
                    result = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(result)
                elif (s[i] == '/'):
                    # result = abs(stack[-2]) // abs(stack[-1])
                    # if (stack[-2] < 0 and stack[-1] > 0) or (stack[-2] > 0 and stack[-1] < 0):
                    #     result = result*-1
                    result = int(stack[-2] / stack[-1]) # truncates towards zero
                    stack.pop()
                    stack.pop()
                    stack.append(result)
                # else if string is not acceptable, return an error message
                else:
                    print("Not an acceptable string")
                    break            
    
                    # return the top of the stack
            # print(stack)
        if len(stack) > 1:
            print("Not an acceptable string")
        return stack[0]

test = Solution()
s1 = ["2","1","+","3","*"]
s2 = ["4","13","5","/","+"]
s3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(test.evalRPN(s1))
print(test.evalRPN(s2))
print(test.evalRPN(s3))