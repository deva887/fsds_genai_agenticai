# set is immutable
#we can only pass one arg at ones
#set allows all data types
#set is ordered
myset_1=set()
print(myset_1)
myset_1.add(21)
myset_1.add('deva')
myset_1.add(6+11j)
myset_1.add(True)
myset_1.add(8.2)
myset_1.add('okay')
print(myset_1)
#set operations
#1.remove
myset_1.remove('okay')
myset_1.pop()
print(myset_1)
#2.discard
myset_1.discard(234)
print(myset_1)
#3.union
a={1,2,3,4,5}
b={4,5,6,7,8}
c={8,9,10}
print(a.union(b))#1,2,3,4,5,6,7,8
print(a.intersection(b))#4,5
print(a.difference(b))#1,2,3