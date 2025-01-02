from collections import deque
from typing import List


class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    for num in nums:
      if nums.count(num) == 1:
        return num

  def singleNumber(self, nums: List[int]) -> int:
    for num in set(nums):
      if nums.count(num) == 1:
        return num 

  def singleNumber(self, nums: List[int]) -> int:
    for num in set(nums):
      nums.remove(num)
      if num in nums:
        nums.remove(num)
      else:
        return num

  def singleNumber(self, nums: List[int]) -> int:
    nums_copy = deque(nums)
    while nums_copy:
      num = nums_copy.popleft()
      if num in nums_copy:
        nums_copy.remove(num)
      else:
        return num

  def singleNumber(self, nums: List[int]) -> int:
    while nums:
      num = nums.pop()
      if num in nums:
        nums.remove(num)
      else:
        return num