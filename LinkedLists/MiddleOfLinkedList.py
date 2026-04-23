from typing import Optional, List

class ListNode:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    curr = self
    result = []
    while curr:
      result.append(str(curr.val)) # turns the numbers into string type, so the list is full of strings
      curr = curr.next
    return ' -> '.join(result)

def list_to_linkedlist(items: List[int]):
  dummy = ListNode(None)
  curr = dummy
  for i in items:
    curr.next = ListNode(i)
    curr = curr.next
  return dummy.next

class Solution:
  def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    dummy = head
    while dummy and dummy.next:
      print(f"dummy: {dummy}")
      print(f"curr: {curr}")
      curr = curr.next
      dummy = dummy.next.next
    return curr
  
test = Solution()
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5, 6]
test1 = print(test.middleNode(list_to_linkedlist(list1)))
test2 = print(test.middleNode(list_to_linkedlist(list2)))