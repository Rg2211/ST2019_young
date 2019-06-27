#!/usr/bin/python36

print("content-type: text/html")
print()

import cgi
import subprocess as sp

data = cgi.FieldStorage()
master_ip = data.getvalue("master_ip")
folder = data.getvalue("folder")
cmd = "sudo ansible-playbook ./playbook/jt.yml --extra-vars 'master_ip={} jt_ip={}'".format(master_ip,folder)
#print(sp.getoutput(cmd))
if sp.getstatusoutput(cmd) == 0:
        print("<h1>jobtracker  created")
else:
        print("<h1>Something get error")
