#!/usr/bin/python36
import subprocess as sp
print("content-type: text/html")
print()
 
cmd = "sudo docker ps -a"
out = sp.getoutput(cmd)
con_list = out.split("\n")
print("<ifname width='100%' name='console'></ifname>")
print("""
<table border='5' width='100%'>
<tr>
<th>container Name</th>
<th>iamge Name</th>
<th>status</th>
<th>start</th>
<th>stop</th>
<th>Terminate</th>
<th>Console</th>
</tr>""")
for doc in con_list[1:]:
	if "Up" in con:
                 status = "running"
	elif "Existed" in con:
 		status = "stopped"
	else:
		status  = "unknown docker_state"
	details = con.split()
	doc_name  = details[-1]
	image_name = details[1]
	print("""
	
	<tr>
	<td>{}</td>
	<td>{}</td>
	<td>()</td>
	<td><a href="http://192.168.43.206/cgi-bin/doc_start.py?s={}start</a></td>
	
	<td><a href="http://192.168.43.206/cgi-bin/doc_stop.py?s={}stop</a></td>
	<td><a href="http://192.168.43.206/cgi-bin/doc_terminate.py?s={}terminate</a></td>
	<td><a href="http://192.168.43.206/cgi-bin/doc_console.py?s={}console</a></td>
	</tr>
	""".format(doc_name,image_name,status,doc_name,doc_name,doc_name))
print("</table>")
