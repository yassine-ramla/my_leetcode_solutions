# Definition for a binary tree node.
from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if (p != None) ^ (q != None):
      return False
    if  not p and not q:
      return True
    return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
    pointersp = [p]
    pointersq = [q]

    for i in range(12):
      edge = pow(2, i) - 1
      for pointerp in pointersp[edge:]:
        if pointerp:
          pointersp.append(pointerp.left)
          pointersp.append(pointerp.right)
        else:
          pointersp.append(None)
          pointersp.append(None)

      for pointerq in pointersq[edge:]:
        if pointerq:
          pointersq.append(pointerq.left)
          pointersq.append(pointerq.right)
        else:
          pointersq.append(None)
          pointersq.append(None)

    pvals = [pointer.val if pointer else None for pointer in pointersp] 
    qvals = [pointer.val if pointer else None for pointer in pointersq] 
    
    return pvals == qvals

  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
    pointersp = [p]
    pointersq = [q]

    i = 0
    edge = 0

    while not (all([pointer == None for pointer in pointersp[edge:]]) or all([pointer == None for pointer in pointersq[edge:]])):
      for pointerp in pointersp[edge:]:
        if pointerp:
          pointersp.append(pointerp.left)
          pointersp.append(pointerp.right)
        else:
          pointersp.append(None)
          pointersp.append(None)

      for pointerq in pointersq[edge:]:
        if pointerq:
          pointersq.append(pointerq.left)
          pointersq.append(pointerq.right)
        else:
          pointersq.append(None)
          pointersq.append(None)
      i += 1
      edge = pow(2, i) - 1

    pvals = [pointer.val if pointer else None for pointer in pointersp] 
    qvals = [pointer.val if pointer else None for pointer in pointersq] 
    
    return pvals == qvals
  
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
    pointers = [(p, q)]
    while len(pointers):
      first, second = pointers.pop()
      if (first == None) ^ (second == None) or (first and second and first.val != second.val):
        return False
      if first and second:
        pointers.append((first.left, second.left))
        pointers.append((first.right, second.right))

    return True
  
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
    pointersp = [p]
    pointersq = [q]

    i = 0
    edge = 0
    flag = True

    while flag:
      flag = False
      for j in range(edge, edge + pow(2, i)):
        pp, pq = pointersp[j], pointersq[j]
        if (pp == None) ^ (pq == None) or pp and pq and pp.val != pq.val:
          return False
        if pp and pq:
          flag = True        

      for pointerp in pointersp[edge:]:
        if pointerp:
          pointersp.append(pointerp.left)
          pointersp.append(pointerp.right)
        else:
          pointersp.append(None)
          pointersp.append(None)

      for pointerq in pointersq[edge:]:
        if pointerq:
          pointersq.append(pointerq.left)
          pointersq.append(pointerq.right)
        else:
          pointersq.append(None)
          pointersq.append(None)
      i += 1
      edge = pow(2, i) - 1
    
    return True