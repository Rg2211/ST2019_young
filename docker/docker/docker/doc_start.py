#!/usr/bin/python36
import subprocess as sp
import cgi
print("conten-type text/html")
data = cgi.FieldStorage()
c_name = data.getvalue("s")
cmd = "sudo docker start {} " .format(c_name)

con = sp.getoutput(cmd)
print("location: http://192.168.43.206/cgi-bin/doc_show.py")
print()
