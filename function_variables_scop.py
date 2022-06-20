def addition(a,b):
	c=a+b
	print("Addition of two number:",c)

def multiplication(a,b):
	c=a*b
	print("multiplication of two number:",c)

def division(a,b):
	c=a/b
	print("Division of two number:",c)

def main():
	a=eval(input("Enter the value of a: "))
	b=eval(input("Enter the value of b: "))	
	ops=input("Select the operation: '+' or '*' or '/' =")
	if ops=="+":
		addition(a,b)
	elif ops=="*":
		multiplication(a,b)
	elif ops=="/":
		division(a,b)
	else:
		print("You choice is wrong!!!")
main()