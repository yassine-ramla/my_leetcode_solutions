from typing import List


class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for _ in range(n):
      nums1.pop()
    i = 0
    for num in nums2:
      while i != len(nums1) and nums1[i] < num:
        i += 1
      nums1.insert(i, num)

  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = 0
    for index, num in enumerate(nums2):
      while i != m + index and nums1[i] < num:
        i += 1
      nums1.pop()
      nums1.insert(i, num)

  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    for _ in range(n):
        nums1.pop()
    nums1.extend(nums2)
    nums1.sort()

  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if m == 0:
      # `nums1 = nums2` is supposed to work but it doesn't work when i submit on leetcode
      nums1.clear()
      for num in nums2:
        nums1.append(num)
    for _ in range(n):
      nums1.pop()
    for num2 in nums2:
      for index, num1 in enumerate(nums1):
        if num1 >= num2:
          nums1.insert(index, num2)
          break
        if index == len(nums1) - 1:
          nums1.insert(len(nums1), num2)
          break