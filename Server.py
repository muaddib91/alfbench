#!/usr/bin/python

import socket, sys , subprocess , threading

class ServerThread(threading.Thread):
	def __init__(self, MESSAGE , conn , socket):
        	self.conn = conn
        	self.MESSAGE = MESSAGE
		self.socket = socket
        	threading.Thread.__init__(self)
	def run(self):
		ChooseOption(self.MESSAGE ,self.conn ,self.socket)



def Stftp(conn):
	global flag
	conn.send('STFTPACK')
	print 'Starting the FTP payload on server '
	flag = 'BUSY'
	while flag == 'BUSY':
		print 'busy ftp'	
def Stsmb(conn):
	global flag
	conn.send('STSMBACK')
	print 'Starting the SMB payload on server '
	flag = 'BUSY'
	while flag == 'BUSY':
		print 'busy smb'
def Sthttp(conn):
	global flag
	conn.send('STHTTPACK')
	print 'Starting the HTTP payload on server '
	flag = 'BUSY'
	while flag == 'BUSY':
		print 'busy http'
def Abort():
	global flag
	flag = 'READY'
	conn.send('ABORTACK')
	
	
#def Dnld():


def ChooseOption(MESSAGE , conn , socket):
	print MESSAGE
	if MESSAGE == 'STFTP': 
		Stftp(conn)
	if MESSAGE == 'STSMB': 
		Stsmb(conn)
	if MESSAGE == 'STHTTP': 
		Sthttp(conn)
	if MESSAGE == 'DNLD':
		Dnld(conn)
	return 

def ChooseOptionMain(MESSAGE , conn , socket):
	global flag
	if MESSAGE == 'ABORT':
		Abort()
	if MESSAGE == 'STATUS':
		conn.send(flag)
	if MESSAGE == 'EXIT':
		print 'now flag is EXIT'
		conn.send('EXIT')
		flag = 'EXIT'
		socket.close()
		sys.exit() 
	




HOST = sys.argv[1]
PORT = sys.argv[2]
s = socket.socket()
s.bind((HOST, int(PORT)))
flag = 'READY'


while flag != 0:
	s.listen(2)
	(conn, address)=s.accept()
	print 'connected by' , address
	MESSAGE = conn.recv(1024)
	print ' Recived MESSAGE =' , MESSAGE
	print MESSAGE
	if MESSAGE == 'STATUS' or MESSAGE == 'ABORT' or MESSAGE == 'EXIT':
		ChooseOptionMain(MESSAGE , conn , s)
	else:
		if flag != 'BUSY':
			ServerThread(MESSAGE , conn , s).start()
		else: 
			conn.send('The machin is BUSY now')
			
