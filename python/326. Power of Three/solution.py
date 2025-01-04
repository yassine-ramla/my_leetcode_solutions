class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    while n > 1:
      n /= 3
    return n == 1
  
  def isPowerOfThree(self, n: int) -> bool:
    p = 1
    while p < n:
      p *= 3
    return p == n

  def isPowerOfThree(self, n: int) -> bool:
    if n < 1:
      return False
    if n == 1:
      return True
    return self.isPowerOfThree(n / 3)

  def isPowerOfThree(self, n: int) -> bool:
    # 19 because n <= 2^31
    return n > 0 and 3 ** 19 % n == 0