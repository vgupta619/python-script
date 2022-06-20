import os
from os import walk

path="/Volumes/GoogleDrive/My Drive/DevOps/Python/python-script"

print(list(os.walk(path)))
'''
for a,b,c in os.walk(path):
	print(a)
	for eac_file in c:
		print(os.path.join(a,eac_file))
'''