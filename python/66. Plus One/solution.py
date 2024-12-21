from typing import List


class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    i = len(digits) - 1
    while i >= 0:
      if digits[i] == 9:
        digits[i] = 0
        i -= 1
      else:
        digits[i] = digits[i] + 1
        return digits
    return [1, *digits]
  
  # one liner
  def plusOne(self, digits: List[int]) -> List[int]:
    return [int(c) for c in str(int(''.join([str(n) for n in digits])) + 1)]