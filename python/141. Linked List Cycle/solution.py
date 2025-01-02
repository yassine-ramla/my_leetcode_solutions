from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    h = head
    pointers = []
    while h:
      if h in pointers:
        return True
      pointers.append(h)
      h = h.next
    
    return False

  def hasCycle(self, head: Optional[ListNode]) -> bool:
    h1 = head
    while h1:
      h2 = head
      while h2:
        if h1.next == h2:
          return True
        if h1 == h2:
          break
        h2 = h2.next
      h1 = h1.next

    return False

  def hasCycle(self, head: Optional[ListNode]) -> bool:
    fast = slow = head
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
      if fast == slow:
        return True
    return False