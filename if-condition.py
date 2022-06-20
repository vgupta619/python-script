numbers=[1,2,3,4,5,6,7,8,9]
user_num=eval(input("Enter the Number: "))
if user_num in numbers:
   print("Your number is present")
else:
   print("Your number is not present")

#-------------------------------------------------------

string=("THis Strings is NOT defaineD PROperly")
str_con=input("Do you want to convert the string to lower: Press y ? to conver n ? to not: ")
if str_con=='y':
  print(f"Actual String:{string}")
  print(f"Coverted String:{string.lower()}")

#------------------------------------------------------
print("What Does Your Favorite Color Say About You? \n")
#colors=['red', 'green', 'blue', 'yellow']
choice=input("What is your favorite color: ")

if choice == 'red':
   print("\nYou have drive and determination, and you prefer action and risk-taking behaviors. Your biggest need is for physical fulfillment and fitness.")
if choice == 'green':
   print("\nYou are loyal and very frank with others, and you consider your reputation a very important part of your life.")
if choice == 'blue':
   print("\nYou want to find inner peace and absolute truth, and you always make an effort to think of others and their needs.")
if choice == 'yellow':
   print("\nYou enjoy learning and sharing knowledge with others, and you feel a need to always express your individuality.")

