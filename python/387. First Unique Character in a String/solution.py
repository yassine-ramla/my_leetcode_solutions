class Solution:
  def firstUniqChar(self, s: str) -> int:
    visited = []
    for i, c in enumerate(s):
      if c not in visited:
        if s.count(c) == 1:
          return i
        else:
          visited.append(c)

    return -1