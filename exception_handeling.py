my_list=["vikas",1,2,3]


try:
	print(my_list[4])
except:
	print("index value not present in the list")

# OR

try:
	print(my_list[4])
except Exception as e:
	print(e)