# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = {letter: magazine.count(letter) for letter in set(magazine)} # dictionary comprehension. Pay attention to the count() function
        for letter in ransomNote:
            if letter in magazine_count:
                magazine_count[letter] -= 1
            else:
                print("False")
                return False
        for letter in set(magazine):
            if magazine_count[letter] < 0:
                print("False")
                return False
        print("True")
        return True
    
# Testing purposes
solution = Solution() # Creating an instance of the solution class so that I can use the canConstruct method
ransomNote = "aabb"
magazine = "aabb"
solution.canConstruct(ransomNote, magazine)

# Time Complexity: O(n+m)
# Space Complexity: O(n+m)