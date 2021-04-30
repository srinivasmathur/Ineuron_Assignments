
# 1.1 Write a Python Program to implement your own myreduce() function which 
# works exactly like Python's built-in function reduce()

from functools import reduce

def my_reduce(func,seq):
  n = len(seq)
  temp = seq[0]
  for i in range(n-1):
    temp = func(temp,seq[i+1])
  
  return temp

print("My_reduce : ",my_reduce(lambda a,b: a+b,['a','b','c']))
print("Built-in reduce : ",reduce(lambda a,b: a+b,['a','b','c']))