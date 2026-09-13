#605. Can Place Flowers

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        lenn = len(flowerbed)
        i = 0

        for i in range(lenn):
            left_empty = (i == 0 or flowerbed[i-1] == 0)
            right_empty = (i == lenn-1 or flowerbed[i+1] == 0)

            if flowerbed[i] == 0 and left_empty and right_empty:
                n -= 1
                flowerbed[i] = 1
            else:
                pass
        
        if n > 0:
            return False
        return True