#2520. Count the Digits That Divide a Number

class Solution:
    def countDigits(self, num: int) -> int:
        num_str = str(num)
        count = 0
        for c in num_str:
            if num % int(c) == 0:
                count += 1
        return count