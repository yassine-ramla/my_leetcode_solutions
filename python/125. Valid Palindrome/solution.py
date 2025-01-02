import re


class Solution:
  def isPalindrome(self, s: str) -> bool:
    clean_s = re.sub('[^a-z0-9]', '', s.lower())
    return clean_s == clean_s[::-1]
  
  def isPalindrome(self, s: str) -> bool:
    clean_s = ''.join([c for c in s.lower() if c.isalnum()])
    return clean_s == clean_s[::-1]
  
  def isPalindrome(self, s: str) -> bool:
    clean_s = ''
    for c in s.lower():
      if c.isalnum():
        clean_s += c
    return clean_s == clean_s[::-1]
  
  def isPalindrome(self, s: str) -> bool:
    clean_s = ''
    for c in s.lower():
      if c in 'abcdefghijklmnopqrstuvwxyz0123456789':
        clean_s += c
    return clean_s == clean_s[::-1]
  
  def isPalindrome(self, s: str) -> bool:
    clean_s = ''
    for c in s.lower():
      if c in 'abcdefghijklmnopqrstuvwxyz0123456789':
        clean_s += c
    l = 0
    r = len(clean_s) - 1
    while l < r:
      if clean_s[l] != clean_s[r]:
        return False
      l += 1
      r -= 1
    return True