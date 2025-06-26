text="   hello world   "
print(text)
print(text.lstrip())
#list-24-06-2025
#list is orderd sequence of items
l=[]
print(l)
print(type(l))
list_1=[-3,-2,-1,0,1,2,3]#list of integers
list_2=[1.0,2.3,3.4,5.6]#list of float numbers
list_3=['hi','hello','world']#list of strings
list_4=['hello',[10,20],[30,40]]#nested list
list_5=['mixed_list',1,2.3,4+5j,True]#mixed list
print(len(list_1))
#indexing or accessing the list
print(list_1[0])
print(list_1[-1])
print(list_1[-3])
print(list_4[0][0])
print(list_4[2][1])
#list slicing
# list_1=[-3,-2,-1,0,1,2,3]--list of integers
print(list_1[0:3])
print(list_1[0:])
print(list_1[:6])
print(list_1[:10])
print(list_1[:3])
print(list_1[0:-1])
print(list_1[-7:-6])
list_2=[1,1,2,3,4,5,6,6.1]
list_2.remove(1)
del list_2[6]
print(list_2)
list_2[0]='one'
print(list_2)
list_2.pop()
list_2.pop(0)
print(list_2)
list_2.extend([6,7,8])
list_2.insert(0,1)
list_2.append(9)
print(list_2)
list_z=[1,2]
list_z.clear()
print(list_z)
l23=[1,2,3,4]
l24=l23.copy()
print(l24)
print(id(l23)==id(l24))
l23=l24
print(id(l23)==id(l24))
#joining the list
list_one=[1,2,3,4]
list_two=[5,6,7,8]
list_three=[list_one+list_two]
print(list_three)