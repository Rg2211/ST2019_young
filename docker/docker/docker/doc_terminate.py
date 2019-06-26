#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
data = cgi.FieldStorage()
doc_name = data.getvalue("s")
cmd = "sudo docker rm -f {}".format(doc_name)
x = sp.getoutput(cmd)
print("location: http://192.168.43.206/cgi-bin/playbook/doc_show.py")
print()
