#373. Find K Pairs with Smallest Sums

import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        heap = []
        result = []
        
        for i in range(min(k, len(nums1))):
            tuple_ = (nums1[i] + nums2[0], i, 0)
            heap.append(tuple_)
        
        heapq.heapify(heap)
        
        for _ in range(k):
            
            sum_, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])

            if j < len(nums2) - 1:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))

        return result
