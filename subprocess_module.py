import subprocess
cmd="echo $HOME"
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
print(out)
print(err)