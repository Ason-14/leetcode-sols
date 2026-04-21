# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list. 

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# ----------------------------------------------
from typing import Optional, List

# Definition for singly-linked list.
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
        
def list_to_linkedlist(items: List[int]): # this just turns the dynamic array to linked list with pointers
    dummy = ListNode() #initialise an empty listNode as the dummy node (before the head)
    curr = dummy
    for i in items:
        curr.next = ListNode(i)
        curr = curr.next
    return dummy.next # return head (so the newly created linked list)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        return dummy.next
    
test = Solution()
list1 = list_to_linkedlist([1, 2, 4])
list2 = list_to_linkedlist([1, 3, 4])
print(test.mergeTwoLists(list1, list2))