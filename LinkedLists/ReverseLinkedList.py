# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

#----------

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        curr = self
        result = [] # create a list (dynamic array) which will be printed using the .join() method
        while curr:
            result.append(str(curr.val))
            curr = curr.next
        return " -> ".join(result)
        
def list_to_linkedlist(items: List[int]):
    dummy = ListNode() #initialise an empty listNode as the dummy node (before the head)
    curr = dummy
    for i in items:
        curr.next = ListNode(i)
        curr = curr.next
    return dummy.next # return head (so the newly created linked list)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return head

test = Solution()
# dynamic array. must convert to linked list first before passing into function
t1 = list_to_linkedlist([1,2,3,4,5])
t2 = list_to_linkedlist([1,2])
t3 = list_to_linkedlist([])
print(test.reverseList(t1))
print(test.reverseList(t2))
print(test.reverseList(t3))