class Solution:
  def hammingWeight(self, n: int) -> int:
    return n.bit_count()

  def hammingWeight(self, n: int) -> int:
    n_copy = n
    res = 0
    for _ in range(n_copy.bit_length()):
      res += n_copy & 1
      n_copy = n_copy >> 1

    return res

  def hammingWeight(self, n: int) -> int:
    n_copy = n
    res = 0
    for _ in range(31):
      res += n_copy & 1
      n_copy = n_copy >> 1

    return res

  def hammingWeight(self, n: int) -> int:
    res = 0
    for i in range(n.bit_length()):
      res += bool(n & pow(2, i))

    return res
  
  def hammingWeight(self, n: int) -> int:
    res = 0
    for i in range(31):
      res += bool(n & pow(2, i))

    return res