# 278. First Bad Version

# predefined isBadVersion API:
def isBadVersion(version: int) -> bool:
  return version >= bad

class Solution:
  def firstBadVersion(self, n: int) -> int:
    R = n
    L = 1

    while L < R:
      M = L + ((R-L) // 2)
      if isBadVersion(M) is False:
        L = M + 1
      else:
        R = M

    return R

sol = Solution()
n = 10
bad = 5
test1 = print(sol.firstBadVersion(n))