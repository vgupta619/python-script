import os
import sys

for i in range(1, 11):
	if i==10:
		print(f"\t{i}  {i+10}  {i+20}  {i+30}  {i+40}  {i+50}  {i+60}  {i+70}  {i+80}  {i+90}")
	else:
	    print(f"\t{i}   {i+10}  {i+20}  {i+30}  {i+40}  {i+50}  {i+60}  {i+70}  {i+80}  {i+90}")

	
# for loop to understand tuple

for i,j in ((1,2),(3,4),(5,6)):
	print(j)
	print(i)

# for loop to understand dictionary 

disc = {'a':1, 'b':2, 'c':4}

for i in disc.keys():
  print(i)	

for i in disc.values():
  print(i)	

for i in disc.items():
	print(i)