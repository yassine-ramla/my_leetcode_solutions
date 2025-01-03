from collections import Counter


class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    for c in set(s):
      if s.count(c) != t.count(c):
        return False
    return True
  
  def isAnagram(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
  
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    for c in s:
      t = t.replace(c, '', 1)

    return t == ''
  
  def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)