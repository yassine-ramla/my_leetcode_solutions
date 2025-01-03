from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    res = []
    def rec(root, prev_path):
      prev_path.append(root.val)
      if root.left:
        rec(root.left, prev_path.copy())
      if root.right:
        rec(root.right, prev_path.copy())
      if not root.left and not root.right:
        path = str(prev_path[0])
        for val in prev_path[1:]:
          path += f'->{val}'
        res.append(path)
    rec(root, [])
    return res

  def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    res = []
    def rec(root, path):
      if not path:
        path = str(root.val)
      else:
        path += f'->{root.val}'
      if root.left:
        rec(root.left, path)
      if root.right:
        rec(root.right, path)
      if not root.left and not root.right:
        res.append(path)
    rec(root, '')
    return res