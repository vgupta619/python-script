	import os

cmd="ls"
cmd_python=os.system(cmd)

if cmd_python==0:
	print(f"Command executed: \n {cmd_python}")
else:
	print(f"command got failed: \n {cmd_python}")
