import subprocess as sp
cmd1 = "docker start Vlc2"
sp.getoutput(cmd1)
cmd2 = "ssh -X root@172.17.0.2 vlc"
sp.getoutput(cmd2)

