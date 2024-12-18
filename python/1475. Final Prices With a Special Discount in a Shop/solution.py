from typing import List


class Solution:
  def finalPrices(self, prices: List[int]) -> List[int]:
    answer = []
    for index, price in enumerate(prices):
      current_discount = 0
      for discount in prices[index + 1:]:
        if discount <= price:
          current_discount = discount
          break
      answer.append(price - current_discount)
    return answer
  
  def finalPrices(self, prices: List[int]) -> List[int]:
    answer = prices.copy()
    prices_length = len(prices)
    for i in range(prices_length):
      for j in range(i + 1, prices_length):
        if answer[j] <= answer[i]:
          answer[i] -= answer[j]
          break
    return answer