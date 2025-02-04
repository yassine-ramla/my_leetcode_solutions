from typing import List


class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    res = []
    for num in nums1:
      if num in nums2:
        res.append(num)
        nums2.remove(num)

    return res