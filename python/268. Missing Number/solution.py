from typing import List


class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    return (set(range(len(nums) + 1)) - set(nums)).pop()
  
  def missingNumber(self, nums: List[int]) -> int:
    return (len(nums) * (len(nums) + 1) // 2) - sum(nums)
  
  def missingNumber(self, nums: List[int]) -> int:
    for index, num in enumerate(sorted(nums)):
      if num != index:
        return index
    return len(nums)
  
  def missingNumber(self, nums: List[int]) -> int:
    i = 0
    for num in sorted(nums):
      if num == i:
        i += 1
      else:
        return i
    return len(nums)

  def missingNumber(self, nums: List[int]) -> int:
    for num in range(len(nums) + 1):
      try:
        nums.remove(num)
      except:
        return num

  def missingNumber(self, nums: List[int]) -> int:
    for num in range(len(nums) + 1):
      if num not in nums:
        return num

  def missingNumber(self, nums: List[int]) -> int:
    for num in range(len(nums) + 1):
      try:
        nums.index(num)
      except:
        return num