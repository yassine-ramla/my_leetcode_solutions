from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def rec(root):
      if root:
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
    rec(root)
    return root
  
  # or just like this
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root:
      root.left, root.right = root.right, root.left
      self.invertTree(root.left)
      self.invertTree(root.right)
    return root