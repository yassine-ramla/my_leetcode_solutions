# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    l1, l2 = list1, list2
    l = p = ListNode()
    while l1 and l2:
      if l1.val < l2.val:
        p.next = l1
        l1 = l1.next
      else:
        p.next = l2
        l2 = l2.next
      p = p.next
    if l1:
      p.next = l1
    elif l2:
      p.next = l2
    return l.next

  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
      return list2
    if not list2:
      return list1
    l1, l2 = list1, list2
    l = p = ListNode()
    while l1 and l2:
      if l1.val < l2.val:
        p.val = l1.val
        l1 = l1.next
      else:
        p.val = l2.val
        l2 = l2.next
      p.next = ListNode()
      p = p.next
    if l1:
      p.val = l1.val
      p.next = l1.next
    elif l2:
      p.val = l2.val
      p.next = l2.next
    return l

  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 == None:
      return list2
    if list2 == None:
      return list1
    l1 = list1
    while l1.next != None:
      l1 = l1.next
    l1.next = list2
    l1 = list1
    while l1.next != None:
      p = l1
      l2 = l1.next
      while l2 != None:
        if l2.val < p.val:
          p = l2
        l2 = l2.next
      temp = l1.val
      l1.val = p.val
      p.val = temp
      l1 = l1.next
    return list1
  
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 == None:
      return list2
    if list2 == None:
      return list1
    l1 = list1
    while l1.next != None:
      l1 = l1.next
    l1.next = list2
    l1 = list1
    while l1.next != None:
      l2 = list1
      while l2.next != None:
        if l2.val > l2.next.val:
          temp = l2.val
          l2.val = l2.next.val
          l2.next.val = temp
        l2 = l2.next
      l1 = l1.next
    return list1
  
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 == None:
      return list2
    if list2 == None:
      return list1
    list_len = 0
    l1 = list1
    while l1.next != None:
      list_len += 1
      l1 = l1.next
    list_len += 1
    l1.next = list2
    l2 = list2
    while l2 != None:
      list_len += 1
      l2 = l2.next
    l1 = list1
    for i in range(list_len - 1):
      l2 = list1
      for _ in range(list_len - i - 1):
        if l2.val > l2.next.val:
          temp = l2.val
          l2.val = l2.next.val
          l2.next.val = temp
        l2 = l2.next
      l1 = l1.next
    return list1
  
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    l1, l2 = list1, list2
    arr = []
    while l1 != None:
      arr.append(l1.val)
      l1 = l1.next
    while l2 != None:
      arr.append(l2.val)
      l2 = l2.next
    if len(arr):
      arr = sorted(arr)
      l = p = ListNode()
      for val in arr[:-1]:
        p.val = val
        p.next = ListNode()
        p = p.next
      p.val = arr[-1]
      return l
    return None