from typing import List

class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    for i in range(len(nums) - 1):
      if nums[i] in nums[i + 1:i + k + 1]:
        return True
    return False
  
  # the same solution as the first one, we just check if there is a possibility first here
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    if 1 < len(set(nums)) == len(nums):
      return False
    for i in range(len(nums) - 1):
      if nums[i] in nums[i + 1:i + k + 1]:
        return True
    return False