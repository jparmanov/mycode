#!/usr/bin/python3

import paramiko
import os

t=paramiko.Transport("10.10.2.3", 22)
t.connect(username="bender", password="alta3")

sftp=paramiko.SFTPClient.from_transport(t)

for x in os.listdir("/home/student//mycode/filestocopy/"):
    if not os.path.isdir("/home/student/mycode/filestocopy/"+x):
        sftp.put("/home/student/mycode/filestocopy/"+x, "/tmp/"+x)

sftp.close()
