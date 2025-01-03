import math


class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    return n > 0 and n.bit_count() == 1
  
  def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0:
      return False
    n_copy = n
    while n_copy > 1:
      n_copy /= 2
    return n_copy == 1
  
  def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0:
      return False
    log2n = math.log2(n)
    return int(log2n) == log2n
  
  def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0:
      return False
    ones = 0
    while n and ones < 2:
      ones += n & 1
      n >>= 1
    return ones == 1
  
  def isPowerOfTwo(self, n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0