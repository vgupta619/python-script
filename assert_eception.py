age=20

try:
	assert age>30
	print("valid age")
except AssertionError:
	print("Raised with assert beacuse age is lessthan 30")
except:
	print("Exeption occured")