from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if not head:
      return None
    while head.val == val:
      if not head.next:
        return None
      head = head.next
    h = head
    while h and h.next:
      if h.next.val == val:
        h.next = h.next.next
      else:
        h = h.next
    return head
