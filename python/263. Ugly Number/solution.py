class Solution:
  def isUgly(self, n: int) -> bool:
    if n < 2:
      return n == 1
    while n % 2 == 0:
      n //= 2

    while n % 3 == 0:
      n //= 3
    
    while n % 5 == 0:
      n //= 5
    return n == 1
  
  def isUgly(self, n: int) -> bool:
    if n < 2:
      return n == 1
    for p in 2, 3, 5:
      while n % p == 0:
        n //= p
    return n == 1