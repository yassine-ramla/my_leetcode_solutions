import math

class Solution:
  # based on the newton-raphson low xn+1​=2/1​(xn​+S/xn) where S is the number we need the square root for
  def mySqrt(self, x: int) -> int:
    xn = x
    while xn * xn > x:
      xn = math.floor(0.5 * (xn + x / xn))
    return xn
  
  # brute force
  def mySqrt(self, x: int) -> int:
    i = 0
    while i * i <= x:
      i += 1

    return i - 1