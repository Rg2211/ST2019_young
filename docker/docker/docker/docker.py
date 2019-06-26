#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print()
x = sp.getoutput("sudo docker images")
print("<from action='http://192.168.43.206/cgi-bin/playbook/docker.py'>")
print("enter your docker name:")
print("<input name='n' />")
print("<br />")
print("enter your image name: ")
print("<select name='img'>")
for i in x.split("\n")[1:]:
	j = i.split()
	print("<option" + j[0] + ":" + j[1] + "</option>")

print("</select>")
print("<input type='submit' />")
print("</form>")

