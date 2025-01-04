from math import log


class Solution:
  def isPowerOfFour(self, n: int) -> bool:
    while n > 1:
      n /= 4
    return n == 1
  
  def isPowerOfFour(self, n: int) -> bool:
    if n < 1:
      return False
    while n % 4 == 0:
      n //= 4
    return n == 1
  
  def isPowerOfFour(self, n: int) -> bool:
    p = 1
    while p < n:
      p *= 4
    return p == n
  
  def isPowerOfFour(self, n: int) -> bool:
    if n < 1:
      return False
    if n == 1:
      return True
    return n % 4 == 0 and self.isPowerOfFour(n // 4)
  
  def isPowerOfFour(self, n: int) -> bool:
    return n >= n.bit_count() == n.bit_length() % 2 == 1

  def isPowerOfFour(self, n: int) -> bool:
    return n > 0 and (2 ** 16) % (n ** .5) == 0
  
  def isPowerOfFour(self, n: int) -> bool:
    return n > 0 and log(n, 4).is_integer()