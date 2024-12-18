from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
  def middleNode1(self, head: Optional[ListNode]) -> Optional[ListNode]:
    list_length = 0
    p = head
    while p != None:
      list_length += 1
      p = p.next
    mid_length = list_length // 2
    p = head
    for _ in range(mid_length):
      p = p.next
    return p

  def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast != None and fast.next != None:
      slow = slow.next
      fast = fast.next.next
    return slow
  
  def middleNode3(self, head: Optional[ListNode]) -> Optional[ListNode]:
    arr = []
    p = head
    while p != None:
      arr.append(p)
      p = p.next
    return arr[len(arr) // 2]
  