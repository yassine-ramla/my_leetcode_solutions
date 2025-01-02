from typing import List

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    maj_len = len(nums) // 2
    for num in set(nums):
      if nums.count(num) > maj_len:
        return num
