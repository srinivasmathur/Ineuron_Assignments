# 1.2 Write a Python program to implement your own myfilter() function which 
# works exactly like Python's built-in function filter()


def my_filter(func,seq):
  my_list = []
  for i in seq:
    if func(i)==True:
      my_list.append(i)
  
  return my_list

print(my_filter(lambda x:x>1,[2,3,4,-1,0]))
print(list(filter(lambda x:x>1,[2,3,4,-1,0])))