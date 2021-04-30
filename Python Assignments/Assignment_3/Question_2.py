# Write List comprehensions to produce the following Lists

# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
letters = 'x y z'.split()
ans = [letter*i for letter in letters for i in range(1,5) ]
print("Part 1 : ",ans)

# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
letters = 'x y z'.split()
ans = [letter*i for i in range(1,5) for letter in letters]
print("Part 2 : ",ans)

# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] 
mylist = [2,3,4,5,6]
ans = [[item] for i in range(3) for item in mylist[i:i+3]]
print("Part 3 : ",ans)

# [[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]
mylist = list(range(2,9))
ans = [mylist[i:i+4] for i in range(4)]
print("Part 4 : ",ans)

# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
ans = [(j,i) for i in range(1,4) for j in range(1,4)]
print("Part 5 : ",ans)
