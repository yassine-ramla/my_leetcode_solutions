from typing import List


class Solution:
  def fizzBuzz1(self, n: int) -> List[str]:
    answer = []
    for i in range(1, n + 1):
      if i % 3 == 0 and i % 5 == 0:
        answer.append('FizzBuzz')
      elif i % 3 == 0:
        answer.append('Fizz')
      elif i % 5 == 0:
        answer.append('Buzz')
      else:
        answer.append(str(i))
    return answer
  
  def fizzBuzz2(self, n: int) -> List[str]:
    answer = []
    for i in range(1, n + 1):
      temp = ''
      if i % 3 == 0:
        temp = 'Fizz'
      if i % 5 == 0:
        temp += 'Buzz'
      if i % 3 != 0 and i % 5 != 0:
        temp = str(i)
      answer.append(temp)
    return answer

  