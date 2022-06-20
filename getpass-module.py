import getpass

print(f"User Name is: {getpass.getuser()}")

#print(getpass.io())
#print(getpass.warnings())
#print(getpass.msvcrt())
#print(getpass.os())
#print(getpass.sys())

my_pass = getpass.getpass(prompt="Enter your 6 digit passowrd:")

print(f"password you entered is: {my_pass}")


