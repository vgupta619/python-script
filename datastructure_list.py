my_list_data=[1,2,3,'Python',2,4.3]

print(my_list_data)
print(my_list_data[1])
print(my_list_data[3][0])

print(my_list_data.index(2))
print(my_list_data.index(2,2))

print(my_list_data.count(2))
my_list_data.clear()             # clear the value from variables
print(my_list_data)
my_new   = my_list_data
my_new_1 = my_list_data.copy()   # refer the value for variable my_list_data into my_new_1 with diffrent memory id location
print(f"Memory ID location:{id(my_new),id(my_new_1)}")   # print ID location for variables
print(f"{my_list_data}")
print(my_list_data)
my_list_data[1]='40'
print(my_list_data)

