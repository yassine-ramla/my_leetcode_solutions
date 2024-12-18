from collections import Counter

class Solution:
  def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
    ransomNote_list, ransomNote_set = list(ransomNote), set(ransomNote)
    magazine_list = list(magazine)

    for char in ransomNote_set:
      if ransomNote_list.count(char) > magazine_list.count(char):
        return False

    return True
  
  def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
    ransomNote_list, magazine_list = list(ransomNote), list(magazine)
    while ransomNote_list:
      char = ransomNote_list.pop()
      try:
        magazine_list.remove(char)
      except:
        return False
    return True
  
  def canConstruct3(self, ransomNote: str, magazine: str) -> bool:
    ransomNote_dict = dict.fromkeys(ransomNote, 0)
    magazine_dict = dict.fromkeys(magazine, 0)

    for char in ransomNote:
      ransomNote_dict[char] += 1

    for char in magazine:
      magazine_dict[char] += 1

    for key, value in ransomNote_dict.items():
      if key not in magazine_dict or magazine_dict.get(key, 0) < value:
        return False

    return True
  
  def canConstruct4(self, ransomNote: str, magazine: str) -> bool:
    ransomNote_counter, magazine_counter = Counter(ransomNote), Counter(magazine)
    return ransomNote_counter & magazine_counter == ransomNote_counter
  
  def canConstruct5(self, ransomNote: str, magazine: str) -> bool:
    for c in ransomNote:
      if not c in magazine:
        return False
      magazine = magazine.replace(c, '', 1)

    return True