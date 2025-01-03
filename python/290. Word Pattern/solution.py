class Solution:
  def wordPattern(self, pattern: str, s: str) -> bool:
    if len(pattern) != len(s.split()):
      return False
    mappings = set(zip(pattern, s.split()))
    letters, words = zip(*mappings)
    return len(set(letters)) == len(set(words)) == len(mappings)