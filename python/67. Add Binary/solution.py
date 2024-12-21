class Solution:
  # one liner
  def addBinary(self, a: str, b: str) -> str:
    return f'{(int(a, 2) + int(b, 2)):b}'

  def addBinary(self, a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]
  
  def addBinary(self, a: str, b: str) -> str:
    return format(int(a, 2) + int(b, 2), 'b')
  
  @staticmethod
  def addTwoBinary(a:str, b: str, rem: str):
    if rem == '0':
      if a == '1':
        if b == '1':
          return ('0', '1')
        return ('1', '0')
      if b == '1':
        return ('1', '0')
      return ('0', '0')
    if a == '1':
      if b == '1':
        return ('1', '1')
      return ('0', '1')
    if b == '1':
      return ('0', '1')
    return ('1', '0')

  def addBinary(self, a: str, b: str) -> str:
    i = 2
    res, rem = self.addTwoBinary(a[-1], b[-1], '0')
    answer = res
    while i <= len(a) or i <= len(b):
      a1 = a[-i: -i + 1]
      b1 = b[-i: -i + 1]
      res, rem = self.addTwoBinary(a1 if a1 else '0', b1 if b1 else '0', rem)
      answer = res + answer
      i += 1
    if rem == '1':
      answer = rem + answer
    return answer
  
  def addBinary(self, a: str, b: str) -> str:
    answer = ''
    max_len = max(len(a), len(b))
    rem = '0'
    padded_a, padded_b = a.rjust(max_len, '0'), b.rjust(max_len, '0')
    for i in range(max_len - 1, -1, -1):
      res, rem = self.addTwoBinary(padded_a[i], padded_b[i], rem)
      answer = res + answer
    if rem == '1':
      answer = rem + answer
    return answer
  
  @staticmethod
  def fromBinary(a: str):
    result = 0
    for i, d in enumerate(a[::-1]):
      if d == '1':
        result += pow(2, i)
    return result

  def addBinary(self, a: str, b: str) -> str:
    decimal_a = self.fromBinary(a)
    decimal_b = self.fromBinary(b) 
    result = decimal_a + decimal_b
    return format(result, 'b')
  
  @staticmethod
  def fromBinary(a: str):
    result = 0
    for i, d in enumerate(a[::-1]):
      if d == '1':
        result += pow(2, i)
    return result

  @staticmethod
  def toBinary(a: int):
    result = ''
    a_copy = a
    while a_copy != 0:
      result = str(a_copy % 2) + result
      a_copy = a_copy // 2
    return result or '0'


  def addBinary(self, a: str, b: str) -> str:
    decimal_a = self.fromBinary(a)
    decimal_b = self.fromBinary(b) 
    result = decimal_a + decimal_b
    return self.toBinary(result)