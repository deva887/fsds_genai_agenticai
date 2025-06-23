#creation of a list
list_1=[1,2,3,4,5,6,7]
list_2=['hello','world',False,True,2,3,4,5.0,3+4j]
print(list_1)
print(list_2)
#accessing elements
print(list_1[0])
print(list_1[1])
print(list_1[-1])
print(list_1[0:6:2])
print(list_1[0:3])
print(list_1[:6])#from 0 to 6 not 6th index is not printed
print(list_1[2:])#2nd index is not printed
#modifying element
list_2[8]=5+6j
list_2[0]='hi..hello'#add string in 0th index in list_21==manaki nacchin aplace lo modify cheyyali ante
print(list_2)
#adding elemets--append,insert,extend---------------------------------------------------------------
list_3=[0,1,2,3,4,6,7]
list_3.append(8)
list_3.insert(5,5)#at 5th index add 5
list_3.extend([9,10])# add more one elements at last
list_3[:0]=-2,-1
print(list_3)
#removing the elements in a list
list_4=[-2,-1,'list_4',0,1,1,2,3,4,5,6,7,8,8]
list_4.remove(1)#removes 1 which occurs at first
del list_4[0]
list_4.pop()
list_4.pop(1)#removes item at index 1
print(list_4)
list_4.clear()
print(list_4)
#list functions-len,min,max,sum
list_5=[0,1,2,3,4]
print(sum(list_5))#10
print(min(list_5))#0
print(max(list_5))#4
print(len(list_5))#5
