from typing import List


class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
    i = 0
    while i < len(nums):
      if nums[i] == val:
        nums.pop(i)
      else:
        i += 1
    return i

  def removeElement(self, nums: List[int], val: int) -> int:
    k = 0
    for i in range(len(nums   )):
      if nums[i] != val:
        nums[k] = nums[i]
        k += 1 
    return k

  def removeElement(self, nums: List[int], val: int) -> int:
    while val in nums:
      nums.remove(val)

    return len(nums)
  