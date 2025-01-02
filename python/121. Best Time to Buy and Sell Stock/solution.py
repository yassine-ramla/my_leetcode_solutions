from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    max_price = max(prices)
    max_index = len(prices) - 1 - prices[::-1].index(max_price)
    profits = [0]

    for index in range(len(prices) - 1):
      if index >= max_index:
        max_price = max(prices[index + 1:])
        max_index = len(prices) - 1 - prices[::-1].index(max_price)
      profits.append(max_price - prices[index])

    return max(profits)
  
  def maxProfit(self, prices: List[int]) -> int:
    last_day = len(prices) - 1
    if last_day == 0:
      return 0
    max_price = max(prices[1:])
    max_index = last_day - prices[::-1].index(max_price)
    min_index = 0
    profits = [0]

    while min_index < last_day:
      min_price = min(prices[min_index:max_index])
      profits.append(max_price - min_price)
      min_index = max_index + 1
      if min_index >= last_day:
        break
      max_price = max(prices[min_index + 1:])
      max_index = last_day - prices[::-1].index(max_price)
        
    return max(profits)