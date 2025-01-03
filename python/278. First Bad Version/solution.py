# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
  return True or False

class Solution:
  def firstBadVersion(self, n: int) -> int:
    r = n
    l = 1
    mid = l + (r - l) // 2
    while True:
      if isBadVersion(mid):
        if isBadVersion(mid - 1):
          r = mid - 1
          mid = l + (r - l) // 2
        else:
          return mid
      else:
        if isBadVersion(mid + 1):
          return mid + 1
        else:
          l = mid + 1
          mid = l + (r - l) // 2
