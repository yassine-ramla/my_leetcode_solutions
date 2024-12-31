from typing import List


class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    triangle = [[1]]
    for i in range(numRows - 1):
      row = []
      for j in range(len(triangle[i]) + 1):
        row.append((triangle[i][j - 1] if j > 0 else 0) + (triangle[i][j] if j < len(triangle[i]) else 0))
      triangle.append(row)

    return triangle

  def generate(self, numRows: int) -> List[List[int]]:
    triangle = [[1], *[[1, 1] for _ in range(numRows - 1)]]

    for i in range(1, numRows):
      for j in range(1, i):
        triangle[i].insert(j, triangle[i - 1][j - 1] + triangle[i - 1][j])

    return triangle

  def generate(self, numRows: int) -> List[List[int]]:
    triangle = [[1], *[[1,*[None for _ in range(i)], 1] for i in range(numRows - 1)]]

    for i in range(1, numRows):
      for j in range(1, i):
        triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle

  def generate(self, numRows: int) -> List[List[int]]:
    triangle = [[1]]

    for i in range(1, numRows):
      row = [1] + [None] * (i - 1) + [1]
      for j in range(1, i):
          row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
      triangle.append(row)

    return triangle