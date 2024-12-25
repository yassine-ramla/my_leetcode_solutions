# Definition for singly-linked list.
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
      return head
    h1 = h2 = head
    while h2:
      if h2.val != h1.val:
        h1.next = h1 = h2
      h2 = h2.next
    h1.next = None
    return head

  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    h1 = h2 = head
    while h2:
      if h2.val != h1.val:
        h1.next = h1 = h2
      h2 = h2.next
      h1.next = None
    return head
  
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    h = head
    while h and h.next:
      if h.val == h.next.val:
        h.next = h.next.next
      else:
        h = h.next
    return head