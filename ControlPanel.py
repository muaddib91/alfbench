#!/usr/bin/python 

import socket
import sys
import os

global use
use = str('all')  # Global variable for understanding with which host we work now
#--------------Start of Switch function-----------------	
def switch(command, host , port):
	global use
	flag = 0
	i = 0 
	buf = command.split()
        #----------Change all big letter to low letters---
	while i<len(buf):
		buf[i] = buf[i].lower()
		i = i + 1
	#----------'Use' command-----------------                 
	if buf[0] == 'use':
		flag =1	
		if len(buf) == 1:
			if use == 'all':
				print 'User ID:' , use
			else: 
				print  'User ID:' , use +1
			
		else :
			if buf[1] == '0':
				use = 'all'
			else:
				use =int( buf[1])-1
	#------------'exit' command---------------
	if buf[0] == 'quit' and len(buf) == 1:
		flag = 1
		sys.exit()
	#-------------'stat' command--------------
	if buf[0] == 'stat' and len(buf) == 1:
		flag = 1
		print '{0:2} {1:16} {2:6} {3:6}'.format('ID','IP address','Port','Status') 
		num = len(host)
		i = 0
		while i<num:
			s = socket.socket()
			if s.connect_ex((host[i], int(port[i]))) == 0:
				s.send('STATUS')
				stat = s.recv(1024)
				s.close()
				
			else:
				stat = 'down'
				s.close()
			i = i + 1
			print '{0:2} {1:16} {2:6} {3:6}'.format(i,host[i-1],port[i-1],stat)
	#-----------------'help' command------------------
	if buf[0] == 'help' and len(buf) ==  1:
		flag = 1
		print '---------------------------------------------'
        	print 'This program supports the following commands:'
        	print '---------------------------------------------'
        	print '"use" - Chooses the client for connecting'
        	print '        (type "use" for connecting to all clients or'
        	print '        "use <number>" for connecting to a surtain client)'
        	print '\n'
        	print '"stat" - Shows the status-list of all clients'
        	print '\n'
        	print '"sync" - Starts synchronization between control panel and chosen clients'
        	print '\n'
        	print '"ftp" - Starts the FTP-attack for chosen clients'
        	print '\n'
        	print '"http" - Starts the HTTP-attack for chosen clients'
        	print '\n'
        	print '"smb" - Starts the SMB-attack for chosen clients'
        	print '\n'
        	print '"abort" - Aborts current action of chosen clients'
        	print '\n'
        	print '"quit" - Quits the program'
        	print '---------------------------------------------'

	#-----------------'http' command-------------------
	if buf[0] == 'http':
		flag = 1
		SenderResiver('STHTTP' , host , port , use)
	#----------------'abort' command-------------------
	if buf[0] == 'abort':
		flag = 1
		SenderResiver('ABORT' , host , port , use)
	#-----------------'smb' command--------------------
	if buf[0] == 'smb':
		flag = 1
		SenderResiver('STSMB' , host , port , use)
	#-----------------'ftp' command--------------------
	if buf[0] == 'ftp':
		flag = 1
		SenderResiver('STFTP' , host , port , use)
	#-----------------'exit' command-------------------
	if buf[0] == 'exit':
		flag = 1
		SenderResiver('EXIT' , host , port , use)		
	#-----------------Incorrect command----------------		
	if flag == 0 :
		print 'Incorrect command, please try again'
#-----------------End of switch function---------------------------

#-----------------SenderReciver Function---------------------------
def SenderResiver(mes , host , port , use):
	if use == 'all':
		i = 0
		print len(host)
		while i < len(host):
			s = socket.socket()
			i = i + 1
			if s.connect_ex((host[i-1],int(port[i-1])))==0:
				s.send(mes)
				recvdata = s.recv(1024)
				s.close()
				print 'Recived message from {}:{} is {}'.format(host[i-1] , port[i-1] , recvdata)
			else: 
				print 'Can not connerct to {}:{}'.format(host[i-1] , port[i-1])
				s.close()
		return 0
	else:
		s = socket.socket()
		if s.connect_ex((host[use] , int(port[use]))) == 0:
			s.send(mes)
			recvdata = s.recv(1024)
			s.close()
			print 'Recived message from {}:{} is {}'.format(host[use] , port[use] , recvdata)
			return 0
		else:
			print 'Can not connect to {}:{}'.format(host[use] , port[use])
	return 'There is now computers in ready stat'
#-------------------End of SenderReciver function----------------------------	
		
		
	
		

#-----------------Read .cfg file with IP addresses and ports ----------------
a = os.path.exists("ControlPanel.cfg")
if a is True:
	f = open("ControlPanel.cfg", "r")
	ipfile = f.readlines()
	i = 0
	string = []
	HOST = []
	PORT = []
	for element in ipfile:                      
		string.insert(i , ipfile[i])
		(host , port) = string[i].split()
		HOST.insert(i , host)
		PORT.insert(i , port)
		i = i + 1
    
else:
    print "Couldn't load config file."
#--------------------The main cycle-------------------
print "Benchmark Control Panel"
print "***********************"

povt = True
while povt==True:
	mes = raw_input(">>")
	if len(mes) != 0:
		switch(mes, HOST , PORT)
		


