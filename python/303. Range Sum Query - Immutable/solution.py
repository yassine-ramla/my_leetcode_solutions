from typing import List


class NumArray:

  def __init__(self, nums: List[int]):
    self.nums = nums

  def sumRange(self, left: int, right: int) -> int:
    return sum(self.nums[left:right + 1])
  
class NumArray:

  def __init__(self, nums: List[int]):
    self.nums = nums
    for i in range(1, len(nums)):
      self.nums[i] += nums[i - 1]

  def sumRange(self, left: int, right: int) -> int:
    if left == 0:
      return self.nums[right]
    return self.nums[right] - self.nums[left - 1]
  
class NumArray:

  def __init__(self, nums: List[int]):
    self.nums = nums
    for i in range(1, len(nums)):
      self.nums[i] += nums[i - 1]
    self.nums = [0] + self.nums

  def sumRange(self, left: int, right: int) -> int:
    return self.nums[right + 1] - self.nums[left]