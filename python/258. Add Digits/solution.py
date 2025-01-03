class Solution:
  def addDigits(self, num: int) -> int:
    str_num = str(num)
    while len(str_num) > 1:
      str_num = str(sum([int(d) for d in str_num]))

    return int(str_num)
  
  def addDigits(self, num: int) -> int:
    str_num = str(num)
    if len(str_num) == 1:
      return int(str_num)
    return self.addDigits(sum([int(d) for d in str_num]))

  def addDigits(self, num: int) -> int:
    num_copy = num
    while num_copy > 9:
      n = 0
      while num_copy > 0:
        n += num_copy % 10
        num_copy //= 10
      num_copy = n
    return num_copy
  
  def addDigits(self, num: int) -> int:
    if num == 0:
      return 0

    return num % 9 or 9
  
  def addDigits(self, num: int) -> int:
    return 0 if num == 0 else num % 9 or 9