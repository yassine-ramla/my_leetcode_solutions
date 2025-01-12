class Solution:
  def reverseVowels(self, s: str) -> str:
    s_copy = s
    vowels = [c for c in s_copy if c.lower() in {'a', 'e', 'i', 'o', 'u'}]
    for i, c in enumerate(s_copy):
      if c.lower() in ['a', 'e', 'i', 'o', 'u']:
        v = vowels.pop()
        s_copy = s_copy[:i] + v + s_copy[i + 1:]

    return s_copy

  def reverseVowels(self, s: str) -> str:
    vowels = [c for c in s if c.lower() in {'a', 'e', 'i', 'o', 'u'}]
    for i, c in enumerate(s):
      if c.lower() in {'a', 'e', 'i', 'o', 'u'}:
        v = vowels.pop()
        s = s[:i] + v + s[i + 1:]

    return s
  
  def reverseVowels(self, s: str) -> str:
    vowels = [c for c in s if c.lower() in {'a', 'e', 'i', 'o', 'u'}]
    res = ''
    for c in s:
      if c.lower() in {'a', 'e', 'i', 'o', 'u'}:
        res += vowels.pop()
      else:
        res += c
    return res