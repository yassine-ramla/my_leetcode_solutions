from typing import List


class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    triangle = [[1]]

    for i in range(1, rowIndex + 1):
      row = [1] + [None] * (i - 1) + [1]
      for j in range(1, i):
        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
      triangle.append(row)

    return triangle[-1]
  
  def getRow(self, rowIndex: int) -> List[int]:
    def fact(n):
      if n < 2:
        return 1
      return fact(n - 1) * n

    row = []
    for i in range(rowIndex + 1):
      row.append(fact(rowIndex) // (fact(i) * fact(rowIndex - i)))
    return row
  
  def getRow(self, rowIndex: int) -> List[int]:
    def fact(n):
      res = 1
      for i in range(1, n + 1):
        res *= i

      return res

    row = []
    for i in range(rowIndex + 1):
      row.append(fact(rowIndex) // (fact(i) * fact(rowIndex - i)))
    return row
  
  def getRow(self, rowIndex: int) -> List[int]:
    row = []
    for i in range(rowIndex + 1):
      e1 = e2 = 1
      for j in range(rowIndex - i + 1, rowIndex + 1):
        e1 *= j
      for j in range(1, i + 1):
        e2 *= j
      row.append(e1 // e2)
    return row
  
  def getRow(self, rowIndex: int) -> List[int]:
    row = []
    for i in range(rowIndex + 1):
      e1 = 1
      for j in range(rowIndex - i + 1, rowIndex + 1):
        e1 *= j
      for j in range(1, i + 1):
        e1 //= j
      row.append(e1)
    return row

  def getRow(self, rowIndex: int) -> List[int]:
    row = []
    for i in range(rowIndex + 1):
      e1 = 1
      for j in range(rowIndex - i + 1, rowIndex + 1):
        e1 *= j / (j - rowIndex + i)
      row.append(round(e1))
    return row