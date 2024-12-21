class Solution:
  # one liner
  def lengthOfLastWord(self, s: str) -> int:
    return len(s.split()[-1])

  def lengthOfLastWord(self, s: str) -> int:
    s_reversed = s[::-1]
    i = 0
    while s_reversed[i] == ' ':
      i += 1
    
    j = 0
    s_len = len(s_reversed)
    while i < s_len and s_reversed[i] != ' ':
      j += 1
      i += 1

    return j
  
  def lengthOfLastWord(self, s: str) -> int:
    end = len(s) - 1
    while s[end] == ' ':
      end -= 1
    
    start = end
    while start >= 0 and s[start] != ' ':
      start -= 1
    return end - start
  
  def lengthOfLastWord(self, s: str) -> int:
    i = len(s) - 1
    while s[i] == ' ':
      i -= 1
    
    j = 0
    while i >= 0 and s[i] != ' ':
      i -= 1 
      j += 1
    return j
  
  def lengthOfLastWord(self, s: str) -> int:
    rstripped = s.rstrip()
    try:
      return len(rstripped[rstripped.rindex(' ') + 1:])
    except:
      return len(rstripped)
    
  def lengthOfLastWord(self, s: str) -> int:
    w_len = 0
    w_started = False
    for char in s[::-1]:
      if char != ' ':
        w_len += 1
        w_started = True
      else:
        if w_started:
          break
    return w_len

  def lengthOfLastWord(self, s: str) -> int:
    w_len = 0
    w_started = False
    i = len(s) - 1
    while i >= 0:
      if s[i] != ' ':
        w_len += 1
        w_started = True
      else:
        if w_started:
          break
      i -= 1
    return w_len