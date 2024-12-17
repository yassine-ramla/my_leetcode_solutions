from typing import List


class Solution:
  def maximumWealth1(self, accounts: List[List[int]]) -> int:
    return max([sum(arr) for arr in accounts])
  
  def maximumWealth2(self, accounts: List[List[int]]) -> int:
    maxWealth = 1
    for i in range(len(accounts)):
      customerWealth = 0
      for j in range(len(accounts[i])):
        customerWealth += accounts[i][j]
      if maxWealth < customerWealth:
        maxWealth = customerWealth
    return maxWealth