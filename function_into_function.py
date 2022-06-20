def math(x,y):
	a=x+y      # This is local variable
	print(a)
	return None

def diplay():
	math(3,4)
	return None
b=10          # This is global variables
diplay()
