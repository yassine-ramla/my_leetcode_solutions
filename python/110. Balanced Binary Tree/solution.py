from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  @staticmethod
  def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    return max(Solution.maxDepth(root.left), Solution.maxDepth(root.right)) + 1

  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    if not root:
      return True
    return abs(Solution.maxDepth(root.left) - Solution.maxDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)