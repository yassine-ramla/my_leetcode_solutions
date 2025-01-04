from typing import List


class Solution:
  def countBits(self, n: int) -> List[int]:
    return [i.bit_count() for i in range(n + 1)]

  class Solution:
    def countBits(self, n: int) -> List[int]:
      arr = [0]
      while len(arr) < n + 1:
        arr.extend([num + 1 for num in arr])
      
      return arr[:n + 1]