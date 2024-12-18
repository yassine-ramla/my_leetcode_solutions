class Solution:
  def isPalindrome1(self, x: int) -> bool:
    str_x = str(x)
    return str_x == str_x[::-1]

  def isPalindrome2(self, x: int) -> bool:
    if x < 0:
      return False
    digits = []
    y = x
    while y > 0:
      digits.append(y % 10)
      y //= 10
    return digits == digits[::-1]
  
  def isPalindrome2(self, x: int) -> bool:
    x_copy = x
    x_reversed = 0
    while x_copy > 0:
      x_reversed = x_reversed * 10 + x_copy % 10
      x_copy //= 10

    return x == x_reversed