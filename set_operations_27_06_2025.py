#set operations
#union,intersection,difference,symmetric_difference
a={1,2,3,4,5,6,7,8}
b={4,5,7,9,10,11}
c={10,20,30,40,50}
print(a.union(b))#1,2,3,4,5,6,7,8,9,10,11
print(a.intersection(b))#4,5,7
print(a.difference(b))#1,2,3,6,8
print(a.symmetric_difference(b))#1,2,3,6,8,9,10,11
print(a.symmetric_difference_update(b))
print(a)
#advance operations
A={1,2,3,4,5,6,7,8}
B={4,5,6,7,8}
C={10,20,30,40,50,60}
print(A.issubset(B))
print(A.issuperset(B))
print(A.isdisjoint(c))
