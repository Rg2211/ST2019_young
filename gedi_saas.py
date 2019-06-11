import subprocess as sp
cmd   =  "ssh -X roop@192.168.43.144 gedit"
x = sp.getoutput(cmd)
print(x)
