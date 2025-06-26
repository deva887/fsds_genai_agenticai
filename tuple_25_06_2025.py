tuple_1=()#empty tuple
print(tuple_1)
print(type(tuple_1))
tuple_2=(1,2,3,4,5,6,7)#tuple with integers
tuple_3=(1.0,2.0,3.0,4.0,5.0,6.0)#tuple with float
tuple_4=(True,False,True,True,False,False)#tuple with boolean values
tuple_5=(1+2j,3+4j,5+6j,7+8j)#tuple with complex tuple
tuple_6=(1,2.0,3+4j,True,False)#tuple with mixed values
tuple_7=(1,2,(3,4),5,6,(7+8j,True))#nested tuple
print(tuple_1)
print(tuple_2)
print(tuple_3)
print(tuple_4)
print(tuple_5)
print(tuple_6)
print(tuple_7)
#operations on list
print(len(tuple_1))
tuple_index=(1,2,3,4,5,6,7)
print(tuple_index[0])#indexing is allowed in tuple
print(tuple_index[-1])
tuple_nested=(1,2,(3,2),4,(5,6,7),'nit')
print(tuple_nested[5][0])#nested tuple indexing
#tuple_slicing
tuple_slicing=(1,2,3,4,5,6,7,8,9,10)
print(tuple_slicing[:])#1,2,3,4,5,6,7,8,9,10
print(tuple_slicing[0:])#1,2,3,4,5,6,7,8,9,10
print(tuple_slicing[:9])#1,2,3,4,5,6,7,8,9
print(tuple_slicing[:10])#1,2,3,4,5,6,7,8,9,10
print(tuple_slicing[:11])#1,2,3,4,5,6,7,8,9,10
print(tuple_slicing[1:5])#2,3,4,5
print(tuple_slicing[-1:5])#()
print(tuple_slicing[-1:-5:-1])#10,9,8,7
print(tuple_slicing[-5:])#6,7,8,9,10
#remove and change
#tuple is immutable
#del option is not there in tuple but deleting the entire tuple is possible
del(tuple_slicing)#tuple is deleted
#print(tuple_slicing)--error
#---------------------------
#membership
tuple_membership=(1,2,3,'one','two','three')
print(23 in tuple_membership)#False
print('one' in tuple_membership)#True
# -------------------------
#index_position --.index() is used
tuple_pos=(1,2,3,4,5)
print(tuple_pos.index(1))
print(tuple_pos.index(5))
#sorting
tuple_sort=(9,5,10,3,1)
sorted_tuple=tuple(sorted(tuple_sort))
print(sorted_tuple)
rev_tuple=tuple(sorted(tuple_sort,reverse=True))#reversed tuple with sorting
print(rev_tuple)


