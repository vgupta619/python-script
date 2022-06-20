import os
import time
from os import path

path="/Volumes/GoogleDrive/My Drive/DevOps/Python/python-script"
path1='vikas'

print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.join(path,path1))
print(os.path.split(path))
print(os.path.getsize(path))
print(os.path.exists(path))
print(os.path.isfile(path))
print(os.path.isdir(path))
print(os.path.islink(path))

print(os.path.getatime(path))
print(os.path.getctime(path))
print(os.path.getmtime(path))

