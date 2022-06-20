import sys

if len(sys.argv) != 3:
	print(f'expected Input:\n{sys.argv[0]} <some string> <upper|lower|title>')
	sys.exit()

str_set=sys.argv[1]
str_ops=sys.argv[2]

if str_ops=='upper':
	print(str_set.upper())
elif str_ops=='lower':
	print(str_set.lower())
elif str_ops=='title':
	print(str_set.title())
else:
	print("Your choice is wrong")





'''
str_set=input("Enter your string: ")
str_ops=input("Enter you choice (upper|lower|title): ")

if str_ops=='upper':
	print(str_set.upper())
elif str_ops=='lower':
	print(str_set.lower())
elif str_ops=='title':
	print(str_set.title())
else:
	print("Your choice is wrong")

#print(sys.argv)
#print(sys.argv[1])

'''