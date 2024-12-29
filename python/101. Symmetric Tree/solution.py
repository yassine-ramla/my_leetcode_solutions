from typing import Optional
# Definition for a binary tree node.

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    stack = [(root.left, root.right)]

    while len(stack):
      left, right = stack.pop()
      if (left == None) ^ (right == None) or left and right and left.val != right.val:
        return False
      if left and right:
        stack.append((left.left, right.right))
        stack.append((left.right, right.left))
    return True
  
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def rec(left, right):
      if (left == None) ^ (right == None) or left and right and left.val != right.val:
        return False
      if not left and not right:
        return True
      return rec(left.left, right.right) and rec(left.right, right.left)
    
    return rec(root.left, root.right)