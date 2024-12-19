class Solution:
  def isValid(self, s: str) -> bool:
    par_dict = {
      ')': '(',
      '}': '{',
      ']': '['
    }
    par_stack = []
    for c in s:
      if c in par_dict:
        par_stack.append(c)
      else:
        if len(par_stack) == 0 or par_dict[c] != par_stack[-1]:
          return False
        else:
          par_stack.pop()

    return len(par_stack) == 0
  
  def isValid(self, s: str) -> bool:
    par_dict = {
      ')': '(',
      '}': '{',
      ']': '['
    }
    s_copy = s
    i = 0
    while i < len(s_copy):
      if s_copy[i] in par_dict:
        i += 1
      else:
        if i == 0 or s_copy[i - 1] != par_dict[s_copy[i]]:
          return False
        else:
          s_copy = s_copy[:i - 1] + s_copy[i + 1:]
          i -= 1
    return len(s_copy) == 0
        