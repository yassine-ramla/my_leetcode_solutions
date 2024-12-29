from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    root = TreeNode()

    def rec(p, arr):
      arr_len = len(arr)
      if arr_len == 1:
        p.val = arr[0]
        return
      elif arr_len == 2:
        p.val = arr[1]
        p.left = TreeNode(val=arr[0])
        return
      mid = arr_len // 2
      p.val = arr[mid]
      p.left = TreeNode()
      p.right = TreeNode()
      rec(p.left, arr[:mid])
      rec(p.right, arr[mid + 1:])

    rec(root, nums)
    return root

  def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    root = TreeNode()
    pointers_obj = [{'root': root, 'arr': nums}]
    while pointers_obj:
      obj = pointers_obj.pop(0)
      arr = obj['arr']
      r = obj['root']
      mid = len(arr) // 2
      r.val = arr[mid]
      left_arr = arr[:mid]
      right_arr = arr[mid + 1:]
      if left_arr:
        r.left = TreeNode()
        pointers_obj.append({'root': r.left, 'arr': left_arr})
      if right_arr:
        r.right = TreeNode()
        pointers_obj.append({'root': r.right, 'arr': right_arr})
    return root
  
  def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    root = TreeNode()
    roots = [root]
    arrs = [nums]

    while roots:
      r = roots.pop(0)
      arr = arrs.pop(0)
      mid = len(arr) // 2
      r.val = arr[mid]
      left_arr = arr[:mid]
      right_arr = arr[mid + 1:]
      if left_arr:
        r.left = TreeNode()
        roots.append(r.left)
        arrs.append(left_arr)
      if right_arr:
        r.right = TreeNode()
        roots.append(r.right)
        arrs.append(right_arr)
    return root

  def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    root = TreeNode()
    roots = deque([root])
    arrs = deque([nums])
    while roots:
      r = roots.popleft()
      arr = arrs.popleft()
      mid = len(arr) // 2
      r.val = arr[mid]
      left_arr = arr[:mid]
      right_arr = arr[mid + 1:]
      if left_arr:
        r.left = TreeNode()
        roots.append(r.left)
        arrs.append(left_arr)
      if right_arr:
        r.right = TreeNode()
        roots.append(r.right)
        arrs.append(right_arr)
    return root