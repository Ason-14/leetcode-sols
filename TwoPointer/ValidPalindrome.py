# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
# removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1
        print(s)
        while p1 < len(s):
            if s[p1].isalnum() and s[p2].isalnum():
                if s[p1].lower() != s[p2].lower():
                    return False
                else:
                    p1 += 1
                    p2 -= 1
            else:
                if not s[p1].isalnum():
                    p1 += 1
                if not s[p2].isalnum():
                    p2 -= 1
        return True

solution = Solution()
s = "Race a car"
print(solution.validPalindrome(s))