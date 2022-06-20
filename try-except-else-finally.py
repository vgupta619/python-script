x=3
y=3
try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
else:
        print("Yeah ! Your answer is :", result)
finally:
    print("change the value of x and y")