
# Programm to learn different type of exception handeling.

try:
    import new
    print(a)
    b=4/0
    open("file.txt","r")
except ModuleNotFoundError:
    print("Module not found and error is handeled by ModuleNotFoundError")
except NameError:
	print("name is not defined and handeled by NameError")
except ZeroDivisionError:
	print("division by zero and is handeled by ZeroDivisionError")
except FileNotFoundError:
	print("file not found and is handeled by FileNotFoundError")
except Exception as e:
	print(e)
finally:
	print("finally we are done")