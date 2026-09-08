#1071. Greatest Common Divisor of Strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # x has to concatenate with itself one or more times to produce str1, str2
        n = len(str1)
        m = len(str2)
        
        # same repeating pattern
        if str1 + str2 != str2 + str1:
            return ""
        # length
        if n > m:
            while m != 0:
                remainder = n % m
                n = m
                m = remainder
            return str1[:n]
        else:
            while n != 0:
                remainder = m % n
                m = n
                n = remainder
            return str1[:m]