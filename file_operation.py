'''
# working with files

#Open and write content into it
file=open("new_file.txt", "w")
file.write("Hi Vikas")
file.close()

#Open and append the content into it
file=open("new_file.txt", "a")
file.write("\nHi Vikas\n")
file.close()


#Open and read the file
file=open("new_file.txt", "r")
data=file.read()
print(data)

# Check file permission
file=open("new_file.txt", "r")
print(file.writable())
print(file.readable())
'''
# Open and read the lines from the file
file=open("new_file.txt", "r")
content=file.readlines()
file.close()
for each in range(4):
	print(content[each])


	