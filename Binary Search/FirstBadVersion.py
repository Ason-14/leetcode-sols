# 278. First Bad Version

# predefined isBadVersion API:
# def isBadVersion(version: int) -> bool:

class Solution:
  def firstBadVersion(self, n: int) -> int:
    R = n
    L = 1
    M = L + ((L-R) // 2)

    while L < R:
      if isBadVersion(M) is False:
        L = M + 1
      else:
        R = M

    return R