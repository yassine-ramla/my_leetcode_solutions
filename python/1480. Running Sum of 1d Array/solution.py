from typing import List


class Solution:
  def runningSum1(self, nums: List[int]) -> List[int]:
    result = []
    for i in range(len(nums)):
      sum = 0
      for j in range(i + 1):
        sum += nums[j]
      result.append(sum)
    return result

  def runningSum2(self, nums: List[int]) -> List[int]:
    result = [nums[0]]
    for i in range(1, len(nums)):
      result.append(result[i - 1] + nums[i])
    return result

  def runningSum3(self, nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
      nums[i] += nums[i - 1]
    return nums
  
  def runningSum(self, nums: List[int]) -> List[int]:
    return [sum(nums[:i + 1]) for i in range(len(nums))]