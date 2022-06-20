import os
import datetime
import sys

req_path=input("Enter the valid path: ")

if not os.path.exists(req_path):
	print("Please provide a valid path.")
	sys.exit()

if os.path.isfile(req_path):
	print("Please provide a directory path")
	sys.exit()
	
for each_file in os.listdir():
	if os.path.isfile(each_file):
	   ab_path=os.path.join(req_path,each_file)
	   print(ab_path)

#old_day=eval(input("How much older file ? input in days: "))

	