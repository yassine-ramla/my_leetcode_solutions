from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
      return None
    pointers = []
    h = head
    while h:
      pointers.append(h)
      h = h.next

    for i in range(len(pointers) - 1, 0, -1):
      pointers[i].next = pointers[i - 1]

    pointers[0].next = None

    return pointers[-1]