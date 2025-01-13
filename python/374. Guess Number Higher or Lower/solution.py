# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
def guess(n: int):
  return -1 or 1 or 0

class Solution:
  def guessNumber(self, n: int) -> int:
    l = 1
    r = n + 1
    mid = l + (r - l) // 2
    while l < r:
      g = guess(mid)
      if g == 0:
        return mid
      if g == -1:
        r = mid
      else:
        l = mid
      mid = l + (r - l) // 2 
