class Solution:
  nums_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
  }

  other_nums_dict = {
    'IV': 2,
    'IX': 2,
    'XL': 20,
    'XC': 20,
    'CD': 200,
    'CM': 200,
  }

  def romanToInt(self, s: str) -> int:
    s_val = 0
    for c in s:
      s_val += self.nums_dict[c]
    for num in self.other_nums_dict:
      if num in s:
        s_val -= self.other_nums_dict[num]

    return s_val
  
  other_nums_dict2 = {
          'IV': 4,
          'IX': 9,
          'XL': 40,
          'XC': 90,
          'CD': 400,
          'CM': 900,
    }

  def romanToInt(self, s: str) -> int:
    s_val = 0
    for num in self.other_nums_dict2:
      if num in s:
        s_val += self.other_nums_dict2[num]
        s = s.replace(num, '')
    for c in s:
      s_val += self.nums_dict[c]

    return s_val
  
  def romanToInt(self, s: str) -> int:
    nums_list = list(self.nums_dict)
    s_val = 0
    s_copy = s[::-1]
    j = 0
    i = nums_list.index(s_copy[0])
    while j < len(s_copy):
        if nums_list.index(s_copy[j]) < i:
            s_val -= self.nums_dict[s_copy[j]]
            j += 1
            if j == len(s_copy):
                break
            i = nums_list.index(s_copy[j])
        else:
            s_val += self.nums_dict[s_copy[j]]
            i = nums_list.index(s_copy[j])
            j += 1
        
    return s_val
  
  def romanToInt(self, s: str) -> int:
    s_val = 0
    for i, j in zip(s, s[1:]):
      if self.nums_dict[j] > self.nums_dict[i]:
        s_val -= self.nums_dict[i]
      else:
        s_val += self.nums_dict[i]

    return s_val + self.nums_dict[s[-1]]

  def romanToInt(self, s: str) -> int:
    s_val = 0
    for i, v in enumerate(s[:-1]):
      if self.nums_dict[s[i + 1]] > self.nums_dict[v]:
          s_val -= self.nums_dict[v]
      else:
          s_val += self.nums_dict[v]

    return s_val + self.nums_dict[s[-1]]