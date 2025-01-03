from typing import List


class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    nums.sort(key=lambda x: x == 0)

  def moveZeroes(self, nums: List[int]) -> None:
    nums[:] = [num for num in nums if num != 0] + [0] * nums.count(0)

  def moveZeroes(self, nums: List[int]) -> None:
    nums_len = len(nums)
    arr = [num for num in nums if num != 0]
    nums.clear()
    for num in arr:
      nums.append(num)
    for _ in range(len(arr), nums_len):
      nums.append(0)

  def moveZeroes(self, nums: List[int]) -> None:
    nums_len = len(nums)
    nums[:] = [num for num in nums if num != 0]
    for _ in range(len(nums), nums_len):
      nums.append(0)

  def moveZeroes(self, nums: List[int]) -> None:
    nums_len = len(nums)
    nums[:] = [num for num in nums if num != 0]
    nums.extend([0] * (nums_len - len(nums)))

  def moveZeroes(self, nums: List[int]) -> None:
    nums_len = len(nums)
    nums[:] = [num for num in nums if num != 0]
    nums += [0] * (nums_len - len(nums))

  def moveZeroes(self, nums: List[int]) -> None:
    i = 0
    while any([num != 0 for num in nums[i:]]):
      if nums[i] == 0:
        nums.pop(i)
        nums.append(0)
      else:
        i += 1

  def moveZeroes(self, nums: List[int]) -> None:
    zeros = []
    while True:
      try:
        nums.remove(0)
        zeros.append(0)
      except:
        break
    nums.extend(zeros)