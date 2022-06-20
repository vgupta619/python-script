import os

print(os.sep)                         # get separator used for directory (/)
print(os.getcwd())                    # get the current path of directory
#print(os.listdir())    
if 'vikas' in os.listdir():           # get the list directory
	os.removedirs("vikas/gupta")
                    # make directory in the path
os.makedirs("vikas/gupta")            # Recursively create directories
#os.mkdir('gupta')
#os.remove('vikas/gupta')             # remove directory
#os.rmdir('vikas')                    # Also use to remove dir
if 'gupta' in os.listdir():
    os.rename('gupta','gupta1')       # rename file
if 'gupta1' in os.listdir():
	os.rename('gupta1','gupta')

if 'gupta' not in os.listdir():
    os.mkdir('gupta')       # rename file

os.environ                            # list environment variables
os.getuid()                           # get user ID
os.getpid()                           # get process ip