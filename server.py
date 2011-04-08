#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import os

print "Benchmark Server"
print "****************"

a = os.path.exists("server.cfg")
if a is True:
    f = open("server.cfg", "r")
    par = f.readlines()
    num = len(par)
    i,k = 0,0
    while i<(num):
        while k<(num):
		par[i]=par[i].strip()
		i=i+1
		par[k]=par[k].split(":")
		k=k+1
    
if a is False:
    print "Couldn't load config file."


HOST=[]
PORT=[]

i=0
for string in par:
	(host , port) = par[i]
	HOST.insert(i , host)
	PORT.insert(i , port)
	i=i+1

global use
global stat
global sync
global abort
global ftp
global http
global smb
global Help
global Quit

use=0
stat=0
sync=0
abort=0
ftp=0
http=0
smb=0
Help=0
Quit=0

def switch(command):
    global use
    global stat
    global sync
    global abort
    global ftp
    global http
    global smb
    global Help
    global Quit

    buf=command.split()
    if buf[0] == "use":
        if len(buf) == 1:
            print "1 argument"
        else:
            user = buf[1]
            print "1 argument",user

    if buf[0] == "stat":
        if len(buf) == 1:
            i=0
            while i<(num):
                print i+1,"-",HOST[i],":",PORT[i]
        else:
            print "Wrong command!"

    if buf[0] == "sync":
        if len(buf) == 1:
            print "1 argument"
        else:
            print "Wrong command!"

    if buf[0] == "abort":
        if len(buf) == 1:
            print "1 argument"
        else:
            print "Wrong command!"

    if buf[0] == "ftp":
        if len(buf) == 1:
            print "1 argument"
        else:
            print "Wrong command!"

    if buf[0] == "http":
        if len(buf) == 1:
            print "1 argument"
        else:
            print "Wrong command!"

    if buf[0] == "smb":
        if len(buf) == 1:
            print "1 argument"
        else:
            print "Wrong command!"

    if buf[0] == "Help":
        if len(buf) == 1:
            print "1 argument"
        else:
            print "Wrong command!"

    if buf[0] == "Quit":
        if len(buf) == 1:
            print "1 argument"
        else:
            print "Wrong command!"



            if int(clnum) <= (num) and int(clnum) > 0:
                print "Connecting..."
                i = int(clnum) - 1
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.connect((HOST[i],int(PORT[i])))


            povt=True
            while povt==True:
                command = raw_input(">>")
                switch(command)
                #if int(clnum) <= (num) and int(clnum) > 0:
                #print "Connecting..."
                #i = int(clnum) - 1
                #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                #s.connect((HOST[i],int(PORT[i]))


                if mes == "quit":
                    print "Quiting this session..."
                    s.send("DISCONNECT")
                    s.shutdown(2)
                    s.close()
                    print "-----------------------"
                    question=1
                    break


      

