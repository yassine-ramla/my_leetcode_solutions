class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    mappings_s = {}
    mappings_t = {}
    for i, c in enumerate(s):
      if not c in mappings_s:
        mappings_s[c] = t[i]
      else:
        if mappings_s[c] != t[i]:
          return False

    for i, c in enumerate(t):
      if not c in mappings_t:
        mappings_t[c] = s[i]
      else:
        if mappings_t[c] != s[i]:
          return False

    return True
  
  def isIsomorphic(self, s: str, t: str) -> bool:
    s_chars = []
    t_chars = []
    for a, b in set(zip(s, t)):
      s_chars.append(a)
      t_chars.append(b)
    
    return len(set(s_chars)) == len(s_chars) and len(set(t_chars)) == len(t_chars)
  
  def isIsomorphic(self, s: str, t: str) -> bool:
    s_chars, t_chars = zip(*set(zip(s, t)))
    return len(set(s_chars)) == len(s_chars) and len(set(t_chars)) == len(t_chars)