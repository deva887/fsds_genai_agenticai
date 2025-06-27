#dictionary creations
dict1=dict()
dict2={}
dictionary={'one':1,'two':2,'three':3,'four':4}
print(type(dictionary))
print(type(dict1))
print(type(dict2))
#creation of dictionary using dict()
dictionary_2=dict({'one':1,'two':2,'three':3,'four':4})
#dictionary with character keys
dict_char={'one':1,'two':2,'three':3,'four':4}
#dictionary with numeric keys
dict_num={1:'one',2:'two',3:'three',4:'four'}
#dictionary with mixed keys
dict_mix={'one':1,2:'two',3:'three'}
print(dict_num,dict_char,dict_mix)
#operations
print(dict_char.keys())
print(dict_num.keys())
print(dict_mix.values())
print(dict_char.items())
print(len(dict_char))
#accessing the dict
dict_acc={'Name':'Deva','Age':21,'Sex':'Male','Role':'Python_developer'}
print(dict_acc['Name'])#using key
print(dict_acc.get('Age'))#using get()
print(dict_acc.get('Role'))
dict_acc['Role']='Data_Scientist'
dict_acc_2={'Role':'SQL_developer'}
dict_acc.update(dict_acc_2)
dict_acc.pop('Role')#specific pair is removed
dict_acc.popitem()#random pair is removed
del[dict_acc['Age']]
del dict_acc#delete the entire dictionary
