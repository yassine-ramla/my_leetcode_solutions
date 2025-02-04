from typing import List

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)
  
  def containsDuplicate(self, nums: List[int]) -> bool:
    nums_set = set()
    for num in nums:
      if num in nums_set:
        return True
      else:
        nums_set.add(num)
    return False