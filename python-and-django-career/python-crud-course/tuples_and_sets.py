a = 1, 2, 3
print(type(a))

a = (1, 2, 3)
print(type(a))

print(a[0])
print(a[1])
# print(a[3]) #index error

a = (1, 1, 1, 2, 3 ,4)
print(dir(a))

print(a.count(1))
print(a.count(2))
print(a.index(1))
print(a.index(3))


#####
#set 
a = set([1, 2, 3])
b = {3, 4, 5}

print(type(a))
print(type(b))

# a[1] # error indexing
# a.add(3) # error dont repeat item
print(a)
print(b)
print('intersection')
print(a.intersection(b))
print('union')
print(a.union(b))
print('difference a - b')
print(a.difference(b))
print('difference b - a')
print(b.difference(a))

a.remove(1)
print('remove a')
print(a)
print('properties sets')
print(dir(a))

