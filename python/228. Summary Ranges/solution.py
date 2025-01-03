from typing import List


class Solution:
  def summaryRanges(self, nums: List[int]) -> List[str]:
    if len(nums) == 0:
      return []

    res = []

    n1 = n2 = nums[0]
    for num in nums[1:]:
      if num == n2 + 1:
        n2 += 1
      else:
        if n1 == n2:
          res.append(str(n1))
        else:
          res.append(f'{n1}->{n2}')
        n1 = n2 = num
    if n1 == n2:
      res.append(str(n1))
    else:
      res.append(f'{n1}->{n2}')
    return res