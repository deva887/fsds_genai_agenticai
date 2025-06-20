#Strings
a='hello'#string should be quoted with ''(single quotes)
A="hello"# ""(double quotes)
ye='''hello'''#(triple quotes)
string1='I don\'t drink alcohol' # \' is used to escape the quote
string2="I don\'t think"
print(a)
print(A)
print(ye)
print(string1)
print(3*'un'+'ium')#strings can be concatenated or added by + and repeated by *
#Indexing
a='1234567890'
print(a[0])# starts from 0 if going from left to right
print(a[-1])#starts from -1 if moving from right to left
print(a[-9])
print(a[-10])
print(a[-0])#negtaive 0 is same as 0
print(a[0:3])#from 0 (included) to 3 (excluded)