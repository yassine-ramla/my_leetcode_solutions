class Solution:
  def isHappy(self, n: int) -> bool:
    squares = [n]
    while True:
      n_sum = 0
      for d in str(squares[-1]):
        n_sum += int(d) ** 2
      if n_sum == 1:
        return True
      if n_sum in squares:
        return False
      squares.append(n_sum)