def is_vowel(char):
  vowel = 'a e i o u'.split()
  if char in vowel:
    return True
  else:
    return False

print(is_vowel('a'))