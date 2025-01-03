from typing import Optional
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    l1 = head
    s = ''
    while l1:
      s += str(l1.val)
      l1 = l1.next

    return s == s[::-1]