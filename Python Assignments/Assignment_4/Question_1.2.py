def filter_long_words(word_list,n):
  result = []
  for word in word_list:
    if len(word)>n:
      result.append(word)
  
  return result

word_list = ['dcfhbvfh','dcbh','hvubvyubu','jf']
print(filter_long_words(word_list,3))