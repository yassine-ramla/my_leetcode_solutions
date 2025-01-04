from typing import List


class Solution:
  def reverseString(self, s: List[str]) -> None:
    for i in range(1, len(s)):
      s.insert(0, s.pop(i))

  def reverseString(self, s: List[str]) -> None:
    s.reverse()

  def reverseString(self, s: List[str]) -> None:
    s[:] = s[::-1]

  def reverseString(self, s: List[str]) -> None:
    l, r = 0, len(s) - 1
    while l < r:
      s[l], s[r] = s[r], s[l]
      l += 1
      r -= 1

  def reverseString(self, s: List[str]) -> None:
    for i in range(len(s) // 2):
      s[i], s[~i] = s[~i], s[i]