from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    l1 = headA
    l2 = headB
    a_pointers = []
    b_pointers = []

    while l1:
      a_pointers.append(l1)
      l1 = l1.next

    while l2:
      b_pointers.append(l2)
      l2 = l2.next

    for pointer in a_pointers:
      if pointer in b_pointers:
        return pointer
    
    return None
  
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    l1 = headA
    a_pointers = []

    while l1:
      a_pointers.append(l1)
      l1 = l1.next

    l2 = headB
    while l2:
      if l2 in a_pointers:
        return l2
      l2 = l2.next

    return None