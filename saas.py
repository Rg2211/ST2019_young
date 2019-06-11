import subprocess  as sp
cmd = "ssh -X rahul@192.168.43.144 firefox")
x = sp.getoutput(cmd)
print(x)

