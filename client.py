#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import os

print "Benchmark Client"
print "****************"

a = os.path.exists("client.cfg")
if a is True:
    f = open("client.cfg", "r")
    par = f.readlines()
    i,k = 0,0
    if len(par)==1:
        while i<len(par):
            while k<len(par):
		par[i]=par[i].strip()
		i=i+1
		par[k]=par[k].split(":")
		k=k+1
    else:
        print "Wrong config file."
        sys.exit()
else:
    print "Couldn't load config file."
    sys.exit()

HOST=[]
PORT=[]

for string in par:
        (host, port) = par[0]
        HOST.insert(i , host)
        PORT.insert(i , port)

question=1
while question==1:
    print "Launch client? (y/n):"
    what = raw_input(">>")
    if what == "y":
        question=0

        print "Setting the address below for connections:"
        print HOST[0],":",PORT[0]

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST[0],int(PORT[0])))
        s.listen(5)
        print "Done! Waiting for connections..."
        print "--------------------------------"

        s, addr = s.accept()
        print "Connected by", addr

        povtor=1
        while povtor==1:

#где-то здесь будет командная строка для возможности выхода и ещё каких-либо вкусняшек        
            buf = s.recv(1024)

            if buf == "STAT":
                s.send("READY")

            if buf == "ABORT":
                print "Uploading aborted!"
                s.send("ABORTED")

            if buf == "FTPSTART":
                print "FTP started!"
                s.send("FTP STARTED")

            if buf == "HTTPSTART":
                print "HTTP started!"
                s.send("HTTP STARTED")

            if buf == "SMBSTART":
                print "SMB started!"
                s.send("SMB STARTED")

            if buf == "UPLOAD":
                print "Uploading started!"
                s.send("UPLOADING")

            if buf == "DISCONNECT": #не доделал выход на повторное прослушивание порта(дисконнект ведёт к краху клиента)
                print "Shutdowning connection..."
                s.shutdown(2)
                s.close()
                question=1
                break

    if what == "n":
        sys.exit()



