# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

#--------------------------------------------------------------------------------------------

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    # constructor
    def __init__(self, val=0, next=None): # inside the brackets are the inital values if there are none inputted when initialised
        self.val = val
        self.next = next
    
    # to print
    def __str__(self):
        curr = self
        result = []
        while curr:
            result.append(str(curr.val))
            curr = curr.next
        return " -> ".join(result)

# Local Functions
def listToLinkedList(items: List[int]):
    dummy = ListNode()
    curr = dummy
    for i in items:
        curr.next = ListNode(i)
        curr = curr.next
    return dummy.next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next == curr.next.next
            else:
                curr = curr.next
        return head

test = Solution()
ex1 = [1, 1, 2]
ex2 = [1, 1, 2, 3, 3]
print(test.deleteDuplicates(listToLinkedList(ex1)))
print(test.deleteDuplicates(listToLinkedList(ex2)))