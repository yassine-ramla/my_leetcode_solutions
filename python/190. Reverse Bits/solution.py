class Solution:
  # @param n, an integer
  # @return an integer
  def reverseBits(self, n):
    return int(format(n, '032b')[::-1], 2)

  def reverseBits(self, n):
    res = 0
    n_copy = n
    for n in range(32):
      res = res << 1
      res += (n_copy & 1)
      n_copy = n_copy >> 1

    return res