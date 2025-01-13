class Solution:
  def isPerfectSquare(self, num: int) -> bool:
    sqrt = num ** 0.5
    # sqrt = math.sqrt(num)
    return int(sqrt) == sqrt
  
  def isPerfectSquare(self, num: int) -> bool:
    i = 0
    while i * i <= num:
      if i * i == num:
        return True
      i += 1

    return False
  
  def isPerfectSquare(self, num: int) -> bool:
    i = 0
    while i * i < num:
      i += 1

    return i * i == num