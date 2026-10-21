#258. Add Digits

class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            summ = sum(int(digit) for digit in str(abs(num)))
            num = summ
        return num