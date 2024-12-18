class Solution:
  def numberOfSteps1(self, num: int) -> int:
    steps = 0
    while num > 0:
      if num % 2 == 0:
        num /= 2
      else:
        num -= 1
      steps += 1
    return steps

  # using bitwise operators
  def numberOfSteps2(self, num: int) -> int:
    steps = 0
    while num > 0:
      if num & 1 == 0:
        num >>= 1
      else: 
        num -= 1
      steps += 1
    return steps
    
  def numberOfSteps3(self, num: int) -> int:
    if num == 0:
      return 0
    if num % 2 == 0:
      return self.numberOfSteps(num / 2) + 1
    return self.numberOfSteps(num - 1) + 1

  # num.bit_count() return how many 1s are in the binary representation of num, ex: (5).bit_count == 2
  # num.bit_length() return how many bits are in the binary representation of num, ex: (5).bit_length == 3
  # each 1 in the binary representation of num requires us 2 steps to get rid of it except for the last one (one step)
  # each 0 in the binary representation of num requires us 1 step to get rid of it except for the last one (zero steps)
  # we need zero steps to make 0 a 0
  def numberOfSteps(self, num: int) -> int:
    if num == 0:
      return 0
    return num.bit_count() + num.bit_length() - 1
            