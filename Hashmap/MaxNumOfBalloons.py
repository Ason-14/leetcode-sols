# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:
# Input: text = "leetcode"
# Output: 0

from collections import defaultdict

class Solution:
    def maxBalloons(self, text: str) -> int:
        count = defaultdict(int)
        for char in text:
            count[char] += 1
        print(count)

        if all(char not in count for char in text):
            return 0
        else:
            return min(count['b'], count['a'], count['l']//2, count['o']//2, count['n'])    
        
solution = Solution()
text = "loonbalxballpoon"
print(solution.maxBalloons(text))