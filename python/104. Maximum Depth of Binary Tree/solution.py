from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
  
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    depth = 0
    pointers = [root]

    while any(pointers):
      for _ in range(len(pointers)):
        pointer = pointers.pop(0)
        left, right = pointer.left, pointer.right
        if left:
          pointers.append(left)
        if right:
          pointers.append(right)
      depth += 1

    return depth