from typing import List


class Solution:
  def longestCommonPrefix1(self, strs: List[str]) -> str:
    longest_prefix = strs[0]
    for s in strs[1:]:
      if len(longest_prefix) > len(s):
        longest_prefix = s
    while len(longest_prefix) != 0:
      if all([word.startswith(longest_prefix) for word in strs]):
        return longest_prefix
      longest_prefix = longest_prefix[:-1]
    return ''
  
  def longestCommonPrefix2(self, strs: List[str]) -> str:
    sorted_strs = sorted(strs)
    first, last = sorted_strs[0], sorted_strs[-1]
    longest_prefix = ''
    for a, b in zip(first, last):
      if a != b:
        return longest_prefix
      longest_prefix += a
    return longest_prefix