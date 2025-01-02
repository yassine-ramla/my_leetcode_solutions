from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def countNodes(self, root: Optional[TreeNode]) -> int:
    res = 0
    def rec(root):
      nonlocal res
      if root:
        res += 1
        rec(root.left)
        rec(root.right)
    rec(root)
    return res
  
  def countNodes(self, root: Optional[TreeNode]) -> int:
    pointers = [root]
    edge = pow(2, 0) - 1
    while any(pointers[edge:]):
      for pointer in pointers[edge:]:
        if pointer:
          pointers.append(pointer.left)
          pointers.append(pointer.right)
        else:
          pointers.append(None)
          pointers.append(None)
      edge = (edge + 1) * 2 - 1

    return sum([1 if pointer else 0 for pointer in pointers])
  
  def countNodes(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    res = 1
    pointers = [root]
    while pointers:
      pointer = pointers.pop()
      if pointer.left:
        res += 1
        pointers.append(pointer.left)
      if pointer.right:
        res += 1
        pointers.append(pointer.right)

    return res