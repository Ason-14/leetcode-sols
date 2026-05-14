# 367. Valid Perfect Square

class Solution:
  def isPerfectSquare(self, num: int) -> bool:
    L = 1
    R = num

    while L <= R:
      M = L + ((R - L) // 2)

      if (M ** 2) == num:
        return True
      elif (M ** 2) >= num:
        R = M - 1
      elif (M ** 2) <= num:
        L = M + 1
    
    return False

sol = Solution()
test = sol.isPerfectSquare(8)
print(test)