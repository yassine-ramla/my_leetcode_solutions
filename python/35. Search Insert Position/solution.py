from typing import List


class Solution:
  # the description says that i should write a O(log n) algorithm, i think this is a O(n) 'in the worst case' but it was accepted
  def searchInsert(self, nums: List[int], target: int) -> int:
    for i in range(len(nums)):
      if nums[i] >= target:
        return i
    return len(nums)