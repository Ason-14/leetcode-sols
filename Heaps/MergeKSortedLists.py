#23. Merge k Sorted Lists

from typing import List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = []

        for i, list_ in enumerate(lists):
            if list_:
                heapq.heappush(heap, (list_.val, i, list_))

        head = ListNode()
        curr = head

        while heap:
            val, row, node = heapq.heappop(heap)
            
            # old way: creating a new ListNode and copying the value
            # newNode = ListNode(val)
            # curr.next = newNode

            # new way: using the same nodes (the one that popped) and redirecting the arrows
            curr.next = node
            curr = node

            if node.next:
                heapq.heappush(heap, (node.next.val, row, node.next))

        return head.next