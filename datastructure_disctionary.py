my_dic={'color' : 'red', 'Name' : 'ridhaan', 'class' : 'nursery'}

print(my_dic)
print(type(my_dic))
print(my_dic['color'])

print(my_dic.get('Name'))

my_dic_2=my_dic.copy()
print(id(my_dic_2),id(my_dic))

print(my_dic_2.items())

#print(my_dic_2.pop())

print(my_dic_2.keys())

print(my_dic_2.values())

my_dic_2['three']=3
print(my_dic_2)

my_dic.update(my_dic_2)          
print(my_dic)
#-------------------------------------------------------------------------
my_dic_2.pop('three')
print(my_dic_2)
#-------------------------------------------------------------------------
my_dic_2.popitem()
print(my_dic_2)
#-------------------------------------------------------------------------
key=['a','s','c','f','v','b','g']

new_dic=dict.fromkeys(key)
new_dic['a']='first letter'
print(new_dic)

#------------------------------------------------------------------------
new_dic.setdefault('s','S')           # If value of key 's' present then ignore otherwise set to 'S'
print(new_dic)
#-----------------------------------------------------------------------
my_dic.clear()
print(my_dic)

